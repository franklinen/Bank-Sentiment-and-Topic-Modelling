# Bank Sentiment and Topic Modelling  (work in Progress)
### Sentiment Analysis and Topic modelling of Five Major Banks in Canada ###

Analysis of Twitter
Read about this project in Medium:

-How to build a PostgreSQL database to store tweets
-Keras Challenges the Avengers
-Visualizing interactions with NetworkX

Introduction
Twitter is used every day by people to express their feelings or thoughts, specially about something that it is happening at the moment or has just occurred; by companies to promote products or services; by journalists to comment on events or write news; and the list can go on. There is no doubt that analyzing twitter and tweets is a powerful tool that can give us a sense on the public opinion about a topic that we are interested in. Fortunately, Twitter provides us with an API (that stands for ‘Application Programming Interface’) which we can interact with creating an app and in that way, access and filter public tweets. Of particular interest to me is knowing what people are feeling about the Avengers. So I will use “avengers” as my term of interest and analyze the public opinion on this.

Neural networks will be used to perform the sentiment analysis. Check my repository and my medium post to learn more about how neural networks work.

Purpose
The goal of this project is to:

To build a PostgreSQL database in order to store tweets about 'Avengers' streamed from Twitter API
Analyse word co-ocurrence with the term 'Avengers'
Develop a neural network to perform a sentiment analysis
Build a network to visualize interactions between users tweeting about 'Avengers'
Data Set Information
There are two ways to capture tweets with Tweepy. The first one is using the REST search API, tweepy.API, which searches against a sampling of recent public tweets published in the past 7 days. The second one is streaming realtime tweets by using the Twitter streaming api that differs from the REST api in the way that this one pull data from twitter while the streaming api pushes messages to a persistent session. In this project, the last option was used to capture realtime tweets.

Twitter APIs always return tweets encoded using JavaScript Object Notation (JSON), an unstructured and flexible type which is based on key-value pairs with attributes and associated values that describe objects. Each tweet contains an author, message, unique ID, a timestamp and creation date when it was posted, among others; each user has a name, id and number of followers. Relational databases such as PostgreSQL has a great performance handling JSON so a relational database and specifically, PostgreSQL db was built to store the tweets streamed from Twitter API.

Analysis
This repository contains three files:

DatabaseStoreStreaming.ipybn answers to the goal #1. Connects to a database, creates tables and store tweets in them, overload tweepy class to listen and capture realtime tweets.
Cleaning DB.ipybn cleans the database by removing any duplicated tweet that was collected.
Analysis of Twitter.ipybnanswer to goals #2 and #3. Retrieve tweets stored in the previous step and handle them in a pandas DataFrame, preprocess the tweet text, visualize the data and build a neural network to analyse the sentiment.
Interaction Network.ipybn answers to goal #4. Gets interaction (retweets, replies and mentions) between Twitter users who have tweet about Avengers and generates a Graph to visualize those interactions.
The whole analysis was done using JupyterLab and Python, using libraries such as: psycopg2, tweepy, pandas, matplotlib, networkx, scikit-learn and keras.

























* Contributing to the project
	* Make sure pre-commit hooks are installed by running pre-commit install in the root directory (one time set up).
	* Obtain Twitter developer credentials here.
	* Database URL = <dialect>+<driver>://<user>:<password>@host:port/database.
	* Create and fill secrets file using cp **.envrc.example .envrc**
	* Give direnv permission to read .envrc by running **direnv allow**
	* Install all dependencies using **pip install -r requirements.txt**
	
Start the Docker container by running sh ./start_app.sh.
