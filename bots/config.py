# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:18:57 2021

@author: User
"""

# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

CONSUMER_KEY = "INPUTKEYHERE"  
CONSUMER_SECRET = "INPUTKEYHERE"  
ACCESS_TOKEN = "INPUTKEYHERE"  
ACCESS_TOKEN_SECRET = "INPUTKEYHERE"  


def create_api():
    # consumer_key = os.getenv("CONSUMER_KEY")
    # consumer_secret = os.getenv("CONSUMER_SECRET")
    # access_token = os.getenv("ACCESS_TOKEN")
    # access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_TOKEN_SECRET


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api