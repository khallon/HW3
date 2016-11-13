# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# MY TWITTER IS HALLON.KAR

import tweepy

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

img = "photo.png"
api.update_with_media(img, status="#UMSI-206 #Proj3")






	



# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")