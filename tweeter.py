# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:03:57 2021

@author: User
"""

import tweepy
from bots.config import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET



# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)



# Create API object
api = tweepy.API(auth,wait_on_rate_limit = True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    
def send_tw(text):    # Create a tweet
    api.update_status(text)
    print("just tweeted")
    
def recent_home_tws_timeline():
    #last 20 tweets
    timeline = api.home_timeline()
    for tweet in timeline:
        print("___________________________________________________")
        print(f"{tweet.user.name} said {tweet.text}")

def home_tws_timeline(count=100):
    for tweet in tweepy.Cursor(api.home_timeline).items(count):
        print(f"{tweet.user.name} said: {tweet.text}")
            
def get_user_info(username):
    """
    ex. 
    get_user_info("senol_isci")

    """
    
    user = api.get_user(username)
    
    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)
    
    print("Last 20 Followers:")
    for follower in user.followers():
        print(follower.name)
            
def follow_user(username):
    api.create_friendship(username)

def set_profile_name(name):
    api.update_profile(name=name)
    
def set_profile_desc(description):
    api.update_profile(description=description)
    
def set_profile_url(url):
    api.update_profile(url=url)
    
def set_profile_location(location):
    a=api.update_profile(location=location)
    print(a)

def like_most_recent_home_tw():
    tweets = api.home_timeline(count=1)
    tweet = tweets[0]
    print(f"Liking tweet {tweet.id} of {tweet.author.name}")
    api.create_favorite(tweet.id)

#set_profile_location("peru")
    
def unlike_most_recent_home_tw():
    tweets = api.home_timeline(count=1)
    tweet = tweets[0]
    print(f"Unliking tweet {tweet.id} of {tweet.author.name}")
    api.destroy_favorite(tweet.id)
    
def create_block_user(identifier):
    """
    identifier:     (id/screen_name/user_id)
    """

    api.create_block(identifier)
    
def decstroy_block_user(identifier):
    """
    identifier:     (id/screen_name/user_id)
    """

    api.destroy_block(identifier)
    
def blocked_users():
    busers=api.blocks()
    for block in busers:    
        print(block.name)
    return busers

def trend_locations():
    return api.trends_available()
    
def trends(loc_id=1):
    """
    1: WOEID. location: worldwide trends

    """
    trends_result = api.trends_place(loc_id)
    for trend in trends_result[0]["trends"]:
        print(trend["name"])

def search_tw_simple(text):
    for tweet in api.search(q=text, lang="en", count=10,result_type="recent" ):
        print(f"{tweet.user.name}:{tweet.text}")
        

def search_tw(search_word,count=100,verb=True):
    """
    * mixed : Include both popular and real time results in the response.
    * recent : return only the most recent results in the response
    * popular : return only the most popular results in the response.
    """
    import pandas as pd
    import json
    import time
    
    print("search word: %s" % search_word)
    tweepyapicontent=pd.DataFrame({},columns=['text'])    
 
    try:  
        #for tweet in tqdm(tweepy.Cursor(api.search, q=search_word, count=100,lang='en',result_type='recent',until=dt.date.today().isoformat()).items()):  
        for tweet in tweepy.Cursor(api.search, q=search_word,lang='en',result_type='recent').items(count):  
                        tweet_text = tweet.text  
                        timex = tweet.created_at  
                        tweeter = tweet.user.screen_name  
                        tweet_dict = {"tweet_text" : tweet_text.strip(), "timestamp" : str(timex), "user" :tweeter}  
                        #tweet_dict = {":": tweet_text.strip()}  
                        tweet_json = json.dumps(tweet_dict)  
                        tweepyapicontent=tweepyapicontent.append({'text':tweet_json},ignore_index=True)
                        print(tweet_json)  if verb==True else None
    except tweepy.TweepError:  
        time.sleep(1)
    tweepyapicontent=tweepyapicontent.dropna()
    return tweepyapicontent
    
def follower_count(username=""):
    if username:
        user=api.get_user(username)
    else:
        user=api.me()
    
    return user.followers_count

def mentionlike_and_follow():
    """
    fetch every tweet in which you are mentioned, 
    and then mark each tweet as Liked and follow its author. 
    """    
    tweets = api.mentions_timeline()
    for tweet in tweets:
        tweet.favorite()
        tweet.user.follow()