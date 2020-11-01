# Twitter Sentiment Analysis
Sentimental analysis is a process of extracting the positive, negative, or neutral orientations of emotions and opinions conveyed by a text. It is also a kind of data mining where we measure the inclination of people’s opinions by using Natural Language Processing (NLP), text analysis, and computational linguistics. In other words, sentimental analysis is a way to find out whether the piece of text is positive, negative, or neutral. 
The purpose of this project is to perform a sentimental analysis on Twitter. Twitter is a microblogging and social networking service on which users post and interact with messages known as "tweets". In this project, we build models for classifying “tweets” into positive, negative, and neutral sentiment. 
The scope of the project is to provide a visual analysis of the social topics, user reviews on the products in the market, movie reviews market stock trends. The Sentimental analyzer uses a machine learning approach in parsing the tweets and categorizing them as either Positive, Negative, or Neutral opinion. 
The main objective of the project is to help businesses to understand customers’ feelings towards products or brands, how people respond to their campaigns or product launches, and why consumers do not buy some products. This will help them in building strategies to improve customers’ experiences. This also helps in keeping track of political views of people and detect consistencies and inconsistencies between statements and actions at the government level. This can also be useful to predict election results, product reviews, movie reviews, people's opinions on upcoming technology.  

## Getting Started
In order to fetch tweets from twitter programmatically, we must create a Twitter developer account and create a new app to generate the app keys and access tokens. The keys are stored in the TwitterLogin.csv.

## Usage
Once the app is created in the twitter developer portal, run the setup.py to install all the required dependencies. <br>
Update the API key, API secret key, Bearer token, Access token and Access token secret in the file TwitterLogin.csv. <br>
Run the file main.py. <br>
User will be prompted to enter Keyword/Tag to search about and number of tweets user wants to analyze.<br>
A pie chart will be generated to visualize the analysis. <br>
The analysed tweets are stored in a file in the same directory.<br>

## Modules
TwitterClient.py - is responsible to authenticate the user on twitter dev portal. Once the user is authenticated, user will be able to fetch tweets based on the search query. <br>
Tools.py - methods/functions which are required to manipulate the data. Functions like cleaning the data, tokenize the tweets, writing the data to a csv file and etc.
DataAnalysis.py - is responsible to analyse the data using a Natural Language processor <a href=https://textblob.readthedocs.io/en/dev/>TextBlob</a>. This class is also responsible to calculate the polarity of each tweet and categorise them as Positive, Negative and Neutral.<br>
main.py - is the main program. 

##### TODO:
1. Implement a method in TwitterClient class to support fetch tweets of past 7 days and generate a word cloud to determine most trending topic of the week.<br> 
2. Improve the cleaning algorithm to avoid any bad or un wanted data in Tools class<br>
3. Tokenize the data and reImplement sentiment analysis using Natural Language Toolkit (NLTK).<br>
4. Implement a wordcloud and display the trending topics in the part 7 days.

## Tools
<ul>
<li>Python 3.8</li>
<li>Tweepy</li>
<li>Textblob</li>
<li>Matplotlib</li>
</ul>

##Authors
Dominic Griffin <br>
Matt Joseph Berberich <br>
Poorna Chandra Gopal <br>
Zarina Hussain <br>