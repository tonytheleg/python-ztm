import tweepy
import time

auth = tweepy.OAuthHandler('qs2LhZm2mk9fjfmP7OVCxDeHF', '9nw9qBQWI2AbmR5xRj87UGpwGuRTIotTNxCfJ4JgbJqOq6MZxr')
auth.set_access_token('155331181-rpeOcpP4OfHokUMsXAlC4MIILnuawWJqt5gK72V9', '3wyM9Mn8Zkfn42MDxpClQr82RAQb0BVYHdjulvx4PsLMs')

api = tweepy.API(auth)
user = api.me()

# cursors are a target for tweepy
def limit_handle(cursor):
    try:
        while True:
            # grabs the next
            yield cursor.next()
    # if we hit Twitters API rate limit, give it some time        
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'python'
numbersOfTweets = 2

# like numberOfTweets with search_string in it
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# print my followers
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    try:
        print(follower.name)
    except StopIteration:
        break