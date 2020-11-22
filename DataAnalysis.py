from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


class DataAnalysis(object):

    def __init__(self, tweets):
        self.polarity = 0
        self.positive = 0
        self.weak_positive = 0
        self.strong_positive = 0
        self.negative = 0
        self.weak_negative = 0
        self.strong_negative = 0
        self.neutral = 0
        self.tweets = tweets
        self.NoOfTerms = len(tweets)

    def sentimentAnalysis(self, searchTerm):
        # creating some variables to store info
        # iterating through tweets fetched
        tweetSentiment = dict()
        for tweetId in self.tweets:
            analysis = TextBlob(self.tweets[tweetId])

            self.polarity += analysis.sentiment.polarity

            if analysis.sentiment.polarity == 0:
                self.neutral += 1
                tweetSentiment[tweetId] = "Neutral"
            elif 0 < analysis.sentiment.polarity <= 0.3:
                self.weak_positive += 1
                tweetSentiment[tweetId] = "Weakly Positive"
            elif 0.3 < analysis.sentiment.polarity <= 0.6:
                self.positive += 1
                tweetSentiment[tweetId] = "Positive"
            elif 0.6 < analysis.sentiment.polarity <= 1:
                self.strong_positive += 1
                tweetSentiment[tweetId] = "Strongly Positive"
            elif -0.3 < analysis.sentiment.polarity <= 0:
                self.weak_negative += 1
                tweetSentiment[tweetId] = "Weakly Negative"
            elif -0.6 < analysis.sentiment.polarity <= -0.3:
                self.negative += 1
                tweetSentiment[tweetId] = "Negative"
            elif -1 < analysis.sentiment.polarity <= -0.6:
                self.strong_negative += 1
                tweetSentiment[tweetId] = "Strongly Negative"

        # finding average of how people are reacting
        self.positive = self.percentage(self.positive, self.NoOfTerms)
        self.weak_positive = self.percentage(self.weak_positive, self.NoOfTerms)
        self.strong_positive = self.percentage(self.strong_positive, self.NoOfTerms)
        self.negative = self.percentage(self.negative, self.NoOfTerms)
        self.weak_negative = self.percentage(self.weak_negative, self.NoOfTerms)
        self.strong_negative = self.percentage(self.strong_negative, self.NoOfTerms)
        self.neutral = self.percentage(self.neutral, self.NoOfTerms)

        # finding average reaction
        self.polarity = self.polarity / self.NoOfTerms

        # printing out data
        print("How people are reacting on " + searchTerm + " by analyzing " + str(self.NoOfTerms) + " tweets.")
        print("Sentiment Analysis Report: ")

        if self.polarity == 0:
            print("Neutral")
        elif 0 < self.polarity <= 0.3:
            print("Weakly Positive")
        elif 0.3 < self.polarity <= 0.6:
            print("Positive")
        elif 0.6 < self.polarity <= 1:
            print("Strongly Positive")
        elif -0.3 < self.polarity <= 0:
            print("Weakly Negative")
        elif -0.6 < self.polarity <= -0.3:
            print("Negative")
        elif -1 < self.polarity <= -0.6:
            print("Strongly Negative")

        print("Detailed Report: ")
        print(str(self.positive) + "% people thought it was positive")
        print(str(self.weak_positive) + "% people thought it was weakly positive")
        print(str(self.strong_positive) + "% people thought it was strongly positive")
        print(str(self.negative) + "% people thought it was negative")
        print(str(self.weak_negative) + "% people thought it was weakly negative")
        print(str(self.strong_negative) + "% people thought it was strongly negative")
        print(str(self.neutral) + "% people thought it was neutral")

        return tweetSentiment

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def generatePieChart(self, searchTerm):
        labels = ['Positive [' + str(self.positive) + '%]', 'Weakly Positive [' + str(self.weak_positive) + '%]',
                  'Strongly Positive [' + str(self.strong_positive) + '%]', 'Neutral [' + str(self.neutral) + '%]',
                  'Negative [' + str(self.negative) + '%]', 'Weakly Negative [' + str(self.weak_negative) + '%]',
                  'Strongly Negative [' + str(self.strong_negative) + '%]']

        sizes = [self.positive, self.weak_positive, self.strong_positive, self.neutral, self.negative,
                 self.weak_negative, self.strong_negative]
        colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(self.NoOfTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    # TODO : generate wordcloud for trending keywords
    def generateWordCloud(self):
        comment_words = ''
        stopwords = set(STOPWORDS)
        tokenlst = list()

    # TODO : Implement a method to Tokenize the tweets and eliminate stopwords in cleanedTweet
        for tweetId in self.tweets:
            tokens = self.tweets[tweetId].split()
            tokenlst.append(tokens)

        for tokens in tokenlst:
            for i in range(len(tokens)):
                tokens[i] = tokens[i].lower()
            comment_words += " ".join(tokens) + " "

        wordcloud = WordCloud(width=640, height=480,
                              background_color='white',
                              stopwords=stopwords,
                              min_font_size=10).generate(comment_words)
        # plot the WordCloud image
        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()
