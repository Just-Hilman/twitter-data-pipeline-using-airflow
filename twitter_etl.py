import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""

# Twitter authentication 
auth = tweepy.OAuth1UserHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Creating an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = '@elonmusk',
                        #    200 is the maximum allowed count
                        count = 200,
                        include_rts = False,
                        tweet_mode = 'extended'
                        )

tweet_list = []
for tweet in tweets:
    text = tweet._json["full_text"]

    refined_tweet = {'user': tweet.user.screen_name,
                     'text': text,
                     'favorite_count': tweet.favorite_count,
                     'retweet_count': tweet.retweet_count,
                     'created_at': tweet.created_at}
    
    tweet_list.append(refined_tweet)