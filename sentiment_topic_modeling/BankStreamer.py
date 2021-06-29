import sys
sys.path

import psycopg2
import tweepy 
import json

#Importing postgres credentials
from postgres_credentials import *

#Importing twitter credentials
from twitter_credentials import *


from os import environ #print(environ)

#import environ.env
from models import Base, Tweets
from utils import session_scope

from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



def twitter_auth():
    ''' 
    Authenticate credentials for Twitter API, Builds an OAuthHandler from environment variables, Returns auth 
    '''
    auth = OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
    auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')
    
    return auth
    

def create_tweets_table(term_to_search):
    """
    This function open a connection with an already created database and creates a new table to
    store tweets related to a subject specified by the user
    """
    #Connect to Twitter Database created in Postgres
    conn_twitter = psycopg2.connect(dbname=dbnametwitter, user=usertwitter, password=passwordtwitter, host=hosttwitter, port=porttwitter)

    #Create a cursor to perform database operations
    cursor_twitter = conn_twitter.cursor()

    #with the cursor now, create two tables, users twitter and the corresponding table according to the selected topic
    cursor_twitter.execute("CREATE TABLE IF NOT EXISTS twitter_users (user_id VARCHAR PRIMARY KEY, user_name VARCHAR);")
    
    query_create = "CREATE TABLE IF NOT EXISTS %s (id SERIAL, created_at timestamp, tweet text NOT NULL, user_id VARCHAR, user_name VARCHAR, retweetstatus_user int, retweetstatus_name VARCHAR, PRIMARY KEY(id), FOREIGN KEY(user_id) REFERENCES twitter_users(user_id));" %("tweets_predict_"+term_to_search)
    cursor_twitter.execute(query_create)
    
    #Commit changes
    conn_twitter.commit()
    
    #Close cursor and the connection
    cursor_twitter.close()
    conn_twitter.close()
    return


def store_tweets_in_table(term_to_search, created_at, tweet, user_id, user_name, retweetstatus_user, retweetstatus_name):
    """
    This function open a connection with an already created database and inserts into corresponding table 
    tweets related to the selected topic
    """
    
    #Connect to Twitter Database created in Postgres
    conn_twitter = psycopg2.connect(dbname=dbnametwitter, user=usertwitter, password=passwordtwitter, host=hosttwitter, port=porttwitter)

    #Create a cursor to perform database operations
    cursor_twitter = conn_twitter.cursor()

    #with the cursor now, insert tweet into table
    cursor_twitter.execute("INSERT INTO twitter_users (user_id, user_name) VALUES (%s, %s) ON CONFLICT(user_id) DO NOTHING;", (user_id, user_name))
    
    cursor_twitter.execute("INSERT INTO %s (created_at, tweet, user_id, user_name, retweetstatus_user, retweetstatus_name) VALUES (%%s, %%s, %%s, %%s, %%s, %%s);" %('tweets_predict_'+term_to_search), 
                           (created_at, tweet, user_id, user_name, retweetstatus_user, retweetstatus_name))
    
    #Commit changes
    conn_twitter.commit()
    
    #Close cursor and the connection
    cursor_twitter.close()
    conn_twitter.close()
    return


class BankListener(StreamListener):

    def on_data(self, data):

        tweet_data = json.loads(data)

        # Exclude retweets
        if 'retweeted_status' not in tweet_data:
            
            
            #Define and extract tweet objects
            if 'extended_tweet' in tweet_data:
                try:
                    date = tweet_data['created_at']
                    tweet_id = tweet_data['id_str']
                    user_name = tweet_data['user']['screen_name']
                    user_location = tweet_data['user']['location']
                    user_followers_count = tweet_data['user']['followers_count']
                    user_statuses_count = tweet_data['user']['statuses_count']
                    text = tweet_data['extended_tweet']['full_text']
                    beginning = tweet_data['extended_tweet']['display_text_range'][0]
                    end = tweet_data['extended_tweet']['display_text_range'][1]
                    # Determine if a bank name is in the tweet and put a value to it
                    # Add as many items to the list that you think people might use to refer to the bank
                    if any(x in text.casefold() for x in ['bmo', 'bank of montreal']):
                        x = 1
                    elif any(x in text.casefold() for x in ['rbc', 'royal bank of canada']):
                        x = 2
                    elif any(x in text.casefold() for x in ['cibc', ' cibc bank']):
                        x = 3
                    elif any(x in text.casefold() for x in ['td', 'td bank', 'toronto dominion bank']):
                        x = 4
                    elif any(x in text.casefold() for x in ['scotia', 'scotiabank']):
                        x = 5
                    else:
                        x = 0
                    tweet = text[beginning:end]
                    
                    
                except AttributeError:
                    text = tweet_data['text']
                    
                
                # Filter records to update to database
                  
                if 'bank' in tweet and any(x in tweet for x in keyword_list):
                    
                    #Store them in the corresponding table in the database
                    store_tweets_in_table(term_to_search, created_at, tweet, user_id, user_name, retweetstatus_user, retweetstatus_name, date=date, tweet_id=tweet_id, text=text, user_name=user_name, user_location=user_location, user_followers_count=user_followers_count, user_statuses_count=user_statuses_count, x=x) 
                    
                          
        return True
            
            
    def on_error(self, status_code):
        if status_code == 420:
            return False



# For realtime streaming
if __name__ == "__main__": 
    #Creates the table for storing the tweets
    keyword_list = ['bmo', 'bank of Montreal', 'rbc', 'royal bank of Canada',  'cibc', 'cibc bank', 'td', 'td bank', 'toronto dominion bank', 'scotiabank', 'scotia']
    create_tweets_table(keyword_list)
    
    #Connect to the streaming twitter API
    api = tweepy.API(wait_on_rate_limit_notify=True)
    
    #Stream the tweets
    streamer = tweepy.Stream(auth=twitter_auth(), listener=BankListener(api=api))
    streamer.filter(languages=["en"], track=[keyword_list])
 
    
