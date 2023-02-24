import tweepy
import time
# Narcisst_Bot:
# Liking a tweet based on the keyword:

auth = tweepy.OAuthHandler('secret', 'secret key')
auth.set_access_token('access_token', 'secret_Access_token')

api = tweepy.API(auth)
user = api.me()


def limit_handling(cursor):              # for handling rate_limit_error
    try:
        while True:
            yield next(cursor)
    except tweepy.RateLimitError:
        time.sleep(200)    # whenever ratelimit exceeds the limit, hold for 200ms and execute


search_string = 'Thalapathy_vijay'
Number_of_tweets = 11000000

for tweet in limit_handling(tweepy.Cursor(api.search, search_string).items(Number_of_tweets)):
    try:
        tweet.favorite()              # used for liking the tweets
        print('I liked that tweet')    # Used for retweets
        tweet.retweet('Hey That was awesome, Keep inspiring')
        print('I retweeted')
    except tweet.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
