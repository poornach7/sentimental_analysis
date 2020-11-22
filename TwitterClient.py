import tweepy
from tweepy import OAuthHandler
import pandas as pd


class TwitterClient(object):
    def __init__(self):
        loginFile = 'TwitterLogin.csv'
        val = pd.read_csv(loginFile)
        # keys and tokens from the Twitter Dev Console
        consumerKey = val['API key'][0]
        consumerSecret = val['API secret key'][0]
        accessToken = val['Access token'][0]
        accessTokenSecret = val['Access token secret'][0]
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumerKey, consumerSecret)
            # set access token and secret
            self.auth.set_access_token(accessToken, accessTokenSecret)
            # create tweepy API object to fetch tweets
            print("Authentication Success.")
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def get_tweets(self, searchTerm, tweetCount=10):
        tweetsDict = dict()
        fetchedTweetsObj = tweepy.Cursor(self.api.search, q=searchTerm, lang="en",
                                         tweet_mode="extended", result_type="mixed").items(tweetCount)
        for tweet in fetchedTweetsObj:
            tweetsDict[tweet.id] = tweet.full_text
        return tweetsDict

    # TODO: Implement a method to fetch tweets from past 7 days and process them to identify the trending topic
    # TODO: Implement a method to fetch tweets from past 7 days in a specific location and process them to identify the
    #  trending topic at a particular location
