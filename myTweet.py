# tweepy will allow us to communicate with Twitter, time will allow us to set how often we tweet
import tweepy, time

#enter the corresponding information from your Twitter application management:
CONSUMER_KEY = 'O8myKfGZ1CIdZQMQqwqS9Op2m' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'wJlltMybsVELEdyCVrmZgLkPmUNAcSv7iFfnmTOdUZmtHL1bdY' #keep the quotes, replace this with your consumer secret key
ACCESS_TOKEN = '495603342-ZvVn4eFWcUfwwGlEa6h6QXDBaZo0rOw3saTKGlUe' #keep the quotes, replace this with your access token
ACCESS_SECRET = '81LEmvUFSx1Fb2rLxuJeDrYCHpcfZWGPjKhsCRWMQSJVw' #keep the quotes, replace this with your access token secret


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# access Twitter!
api = tweepy.API(auth)

# open our content file and read each line
filename=open('tweet.txt')
f=filename.readlines()
filename.close()

# for each line in our contents file, lets tweet that line out except when we hit a error
for line in f:
    try:
        api.update_status(line)
        print("Tweeting!")
    except tweepy.TweepError , err:
        print(err)
    time.sleep(60) #Tweet every 2 minutes
print("All done tweeting!")
