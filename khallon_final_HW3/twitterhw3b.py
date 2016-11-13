# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "3130934385-gDd3f3OmqoexWKfc3fClMiA3wey0YsPckRA0nu7"
access_token_secret = "LL9QdMC9nolUMc21eZasKDN7OPDzXMb6lAr9OnfK1Q1RN"
consumer_key = "Uk1TOFZERWQCZUrtBKpqEcawO"
consumer_secret = "IR74uIa0rSksuLAGQhU4Y5wOr97v3Ma6iNo9qAGB67o9ROHbae" 

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

#thing = input(["Type in a search item"])

public_tweets = api.search('trump')     #I wanted to use input but I keep getting unicode encoding errors for most any other string

list1 = []

list2 = []
for tweet in public_tweets:
	
	print(tweet.text.encode("ascii", "ignore").decode("utf-8"))
	analysis = TextBlob(tweet.text)
	pol = analysis.polarity
	list1.append(pol)
	sub= analysis.subjectivity
	list2.append(sub)
	#print(analysis.sentiment)
	print ("\n")

finalpol = sum(list1)/len(list1)

finalsub = sum(list2)/len(list2) 
print ("The average polarity is " + str(finalpol))
print ("The average subjectivity is " + str(finalsub))
#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data

# Be prepared to change the search term during demo.


