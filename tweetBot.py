# bot.py

import tweepy
from tweetSecret import *

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

 #Construct the API instance
api = tweepy.API(auth) # create an API object

#show followers
#user = api.get_user('@PlipCo')
#for friend in user.friends():
#   print(friend.screen_name)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
