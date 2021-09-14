#Tweepy is an open source Python package that allows you to access the Python Twitter API in a very convenient manner. 
#Tweepy contains a range of Twitter models and API endpoints classes and processes and handles various implementation details in a transparent fashion like: encoding and decoding of data.

import tweepy

# authentication 
#for accessing the Twitter API firstly authentication needs to be done


consumerKey = '-----------------------------'  #get these keys from your twitter developer account
consumerSecret = '--------------------------'
accessToken = '-----------------------------'
accessTokenSecret = '------------------------'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)



# taking input from users
#will put the keyword that I want to search for tweets


search_tag = input("Enter keywords to search: ")
NoOfTerms = int(input("Enter how many tweets to search: "))

tweets = []
tweetText = []
# searching for tweets
tweets = tweepy.Cursor(api.search, q=search_tag+" -filter:retweets", lang = "en").items(NoOfTerms)
#the 'Cursor' function specifies the social and language
#the argument lang = 'en' specifies that here we are extracting data in English Language


tweetList = [tweet.text for tweet in tweets]  #creating a list the number of searched tweets
print(tweetList)
