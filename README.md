# Bank Sentiment and Topic Modelling  #
### Twitter Sentiment Analysis and Topic Modelling of Five Major Banks in Canada ###

Introduction

There is no doubt that analyzing Twitter and tweets is a powerful tool that can give us a sense of public opinion about a topic we are interested in. I am particularly interested in understanding how people feel about the major banks in Canada at any moment in time. 

Purpose

The goal of this project is to:

To build a PostgreSQL database to store tweets about five major banks in Canada streamed from Twitter API
Analyse word co-occurrence with the term 'RBC', 'CIBC', 'TD', 'BMO', "Scotiabank'
Develop a neural network to perform a sentiment analysis
Build a front end to visualize interactions between users tweeting with keywords about the banks

Data Set Information

We stream real-time tweets by using the Twitter streaming API which differs from the REST API in the way that this one pulls data from Twitter while the streaming API pushes messages to a persistent session. 

Twitter APIs always return tweets encoded using JavaScript Object Notation (JSON), an unstructured and flexible type that is based on key-value pairs with attributes and associated values that describe objects. Each tweet contains an author, message, unique ID, a timestamp, and creation date when it was posted, among others; each user has a name, id and number of followers. Relational databases such as PostgreSQL have a great performance handling JSON so a relational database and specifically, PostgreSQL db was built to store the tweets streamed from Twitter API.

Analysis

This repository contains four files:

* Pipeline

	* data pipeline
	
	* model pipeline
* Dependencies
* App
* Requirements



























* Contributing to the project
	* Make sure pre-commit hooks are installed by running pre-commit install in the root directory (one time set up).
	* Obtain Twitter developer credentials here.
	* Database URL = <dialect>+<driver>://<user>:<password>@host:port/database.
	* Create and fill secrets file using cp **.envrc.example .envrc**
	* Give direnv permission to read .envrc by running **direnv allow**
	* Install all dependencies using **pip install -r requirements.txt**
	
Start the Docker container by running sh ./start_app.sh.
