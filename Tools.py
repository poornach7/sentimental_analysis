import re
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Tools(object):

    def clean_tweet(self, tweets):
        cleaned_tweets = dict()
        for tweet_id in tweets:
            # remove @mentions
            cleanTweet = re.sub(r'@_*[A-Za-z0-9]+', '', tweets[tweet_id])
            # remove links
            cleanTweet = re.sub(r'https?:\/\/\S+', '', cleanTweet)
            # remove RT's
            cleanTweet = re.sub(r'RT[\s]+', '', cleanTweet)
            # remove # tags
            cleanTweet = re.sub(r'#[A-Za-z]+', '', cleanTweet)
            # remove any special characters
            cleanTweet = re.sub(r'[^A-Za-z\ ]+', ' ', cleanTweet)
            # remove multiple spaces
            cleanTweet = re.sub(r'[ ]+', ' ', cleanTweet)
            cleanTweet = re.sub(r'^[ ]+', '', cleanTweet)

            # TODO: look for anymore special patterns to clean the tweet
            #shortword = re.compile(r'\W*\b\w{1,3}\b')
            #cleanTweet = shortword.sub('', cleanTweet)
            cleanTweet.lower()
            cleaned_tweets[tweet_id] = cleanTweet
        return cleaned_tweets

    def write_csv(self, file_name, method, tweets):
        try:
            file = open(file_name, method, newline='', encoding='utf-8')
            writer = csv.writer(file)
            writer.writerow(['Tweet ID', 'Raw Tweet', 'Cleaned Tweet'])
            # write dict_tweets to file. dict_tweets = {tweet_id: [raw_tweet, cleaned_tweets]}
            for tweet_id, tweet in tweets.items():
                writer.writerow([tweet_id, tweet[0], tweet[1]])
        except:
            print("Error: Unable to write to csv")

    #TODO: Tokenize the cleaned tweet using NLTK for better natural language processing