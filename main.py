import tweepy
import time

auth = tweepy.OAuthHandler('dgNDWDpdpwYoLEICzhEPkUcYz', 'wnH02UE0eX5BCta9LS821XqfjSB1mgDhKYRsJXyGOkRTzhY4rU')
auth.set_access_token('1248870514568728582-3Yy1F2B3yu3vzIbv8OIJnIkTSZjyyz', 'ZMJXtCfc2YCElXq4lgbi6gOgbDlrwSol0iqJBTCEN55LZ')

api = tweepy.API(auth)

def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name)


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
query = 'python'
numberOfTweets = 2
for tweet in tweepy.Cursor(api.search, query).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break