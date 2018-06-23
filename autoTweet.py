# tweepy will allow us to communicate with Twitter, time will allow us to set how often we tweet
import tweepy, time
from tweetSecret import *

# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# access Twitter!
api = tweepy.API(auth)

# open our content file and read each line
filename=open('autoTweet.txt')
f=filename.readlines()
filename.close()

# for each line in our contents file, lets tweet that line out except when we hit a error
for line in f:
    try:
        api.update_status(line)
        print("Tweeting!")
    except tweepy.TweepError as err:
        print err.message[0]['code']  # prints 34
        print err.args[0][0]['code']  # prints 34
    time.sleep(15) #Tweet every 15 seconds
print("All done tweeting!")
