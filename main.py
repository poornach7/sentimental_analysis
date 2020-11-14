from TwitterClient import TwitterClient
from Tools import Tools
from DataAnalysis import DataAnalysis


def main():
    print("|******************************************|")
    print("|Welcome to Sentimental Analysis on Twitter|")
    print("|******************************************|")
    # input for term to be searched and how many tweets to search
    searchTerm = input("Enter Keyword/Tag to search about: ")
    noOfTerms = int(input("Enter how many tweets to search: "))
    twitterClient = TwitterClient()
    tools = Tools()

    rawTweets = twitterClient.get_tweets(searchTerm, noOfTerms)
    # clean the tweets before adding to the dictionary
    cleanedTweets = tools.clean_tweet(rawTweets)
    dataAnalysis = DataAnalysis(cleanedTweets)
    tweetSentiment = dataAnalysis.sentimentAnalysis(searchTerm)

    tweetsDict = dict()
    for tweetId in cleanedTweets:
        tweetLst = list()
        tweetLst.append(rawTweets[tweetId])
        tweetLst.append(cleanedTweets[tweetId])
        tweetLst.append(tweetSentiment[tweetId])
        tweetsDict[tweetId] = tweetLst
    tools.write_csv(searchTerm + '.csv', 'w', tweetsDict)

    dataAnalysis.generatePieChart(searchTerm)


if __name__ == "__main__":
    # calling main function
    main()
