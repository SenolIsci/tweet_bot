# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:53:40 2021

@author: User
"""



import tweepy
from bots.config import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET




class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        try:
            print(f"{tweet.user.name}:{tweet.extended_tweet['full_text']}\n______________________________________")
        except AttributeError:
            print(f"{tweet.user.name}:{tweet.text}\n______________________________________")
            
        

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)

stream.filter(track=['Python'], languages=["en"])