from TwitterClient import TwitterClient
from Tools import Tools
from DataAnalysis import DataAnalysis


def main():
    # input for term to be searched and how many tweets to search
    tools = Tools()
    while True:
        print("|******************************************|")
        print("|Welcome to Sentimental Analysis on Twitter|")
        print("|******************************************|")
        searchTerm = input("Enter Keyword/Tag to search about: ").replace(" ", "")
        if not searchTerm.isalpha():
            print("Please enter a valid keyword")
            continue
        elif len(searchTerm) <= 3:
            print("Please enter a keyword with more than 3 characters")
            continue

        while True:
            noOfTerms = input("Enter how many tweets to search: (< 500): ")
            if noOfTerms.isnumeric():
                if int(noOfTerms) > 500:
                    print("Defaulting to number of tweets to 500")
                    noOfTerms = int(500)
            else:
                print("Please enter a numeric value < 500.")
                continue

            twitterClient = TwitterClient()

            rawTweets = twitterClient.get_tweets(searchTerm, int(noOfTerms))
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
            break

        while True:
            ch = int(input("Choose from the below options:\n\t1. Pie Chart\n\t2. Word Cloud\n\t3. Search another "
                           "keyword\n\t4. Exit\n Enter your choice: "))
            if ch == 1:
                print("Data visualisation in Pie Chart")
                dataAnalysis.generatePieChart(searchTerm)
            elif ch == 2:
                print("Data visualisation in Word Cloud")
                dataAnalysis.generateWordCloud()
            elif ch == 3:
                break
            elif ch == 4:
                print("Thank You. Good Bye!")
                exit(0)
            else:
                print("Incorrect choice. Please re enter your choice.\n")
                continue


if __name__ == "__main__":
    # calling main function
    main()
