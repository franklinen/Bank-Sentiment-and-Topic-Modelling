from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, ARRAY


Base = declarative_base()


class Tweets(Base):
    __tablename__ = 'tweets'
    tweet_id = Column(String(20), nullable=False, primary_key=True)
    date = Column(DateTime, nullable=False)
    text = Column(String(2000), nullable=False)
    user_name = Column(String(20), nullable=True)
    user_location = Column(String(8), nullable=True)
    user_followers_count = Column(ARRAY(8), nullable=True)
    user_statuses_count = Column(ARRAY(8), nullable=True)
    x = Column(ARRAY(8), nullable=True)
    label = Column(String(8), nullable=True)
    annotated_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return(f'Tweet {self.tweet_id} created @ {self.date}:\n\n{self.tweet}')