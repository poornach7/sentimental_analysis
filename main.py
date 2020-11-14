from TwitterClient import TwitterClient
from Tools import Tools
from DataAnalysis import DataAnalysis


def main():
    print("|******************************************|")
    print("|Welcome to Sentimental Analysis on Twitter|")
    print("|******************************************|")
    # input for term to be searched and how many tweets to search
    search_term = input("Enter Keyword/Tag to search about: ")
    no_of_terms = int(input("Enter how many tweets to search: "))
    client = TwitterClient()
    tools = Tools()

    raw_tweets = client.get_tweets(search_term, no_of_terms)
    print(raw_tweets)

    cleaned_tweets = tools.clean_tweet(raw_tweets)
    print(cleaned_tweets)

    # clean the tweets before adding to the dictionary
    tweets = dict()
    for tweet_id in cleaned_tweets:
        tweetLst = list()
        tweetLst.append(raw_tweets[tweet_id])
        tweetLst.append(cleaned_tweets[tweet_id])
        tweets[tweet_id] = tweetLst
    tools.write_csv(search_term + '.csv', 'w', tweets)

    analysis = DataAnalysis(cleaned_tweets)
    analysis.sentimentAnalysis(search_term)
    analysis.generatePieChart(search_term)


if __name__ == "__main__":
    # calling main function
    main()
