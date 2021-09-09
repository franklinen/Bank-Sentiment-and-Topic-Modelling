#import dependencies and packages
import numpy as np 
import pandas as pd
from copy import deecopy
from bertopic import BERTopic

#load data
df = pd.read_csv(" ")

#Creating Topics
model = BERTopic(language="english")
topics, probs = model.fit_transform(docs)

#Extract the most frequent topics
model.get_topic_freq()

#Get Individual Topics
model.get_topic(0)

model.get_topic(2)

#Visualize Topics
model.visualize_topics()



