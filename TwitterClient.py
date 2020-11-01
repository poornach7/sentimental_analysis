import tweepy
from tweepy import OAuthHandler
import pandas as pd


class TwitterClient(object):
    def __init__(self):
        login_file = 'TwitterLogin.csv'
        val = pd.read_csv(login_file)
        # keys and tokens from the Twitter Dev Console
        consumer_key = val['API key'][0]
        consumer_secret = val['API secret key'][0]
        access_token = val['Access token'][0]
        access_token_secret = val['Access token secret'][0]
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            print("Authentication Success.")
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def get_tweets(self, search_term, count=10):
        tweets = dict()
        fetched_tweets_obj = tweepy.Cursor(self.api.search, q=search_term, lang="en",
                                           tweet_mode="extended", result_type="mixed").items(count)
        for tweet in fetched_tweets_obj:
            tweets[tweet.id] = tweet.full_text
        return tweets
