import requests
import json
from requests_oauthlib import OAuth1

#Enters the API URL to send out POST request to,
#Asks user for input to Tweet.
url = 'https://api.twitter.com/1.1/statuses/update.json'
ask_tweet = input("What's happening today?\n")
tweet = {'status': ask_tweet}

#Using the credential files in twitter_credential, turn into
#temporary variable, json_file.
#The contents of json_file will then be placed as the value
#of another variable named auth_codes
with open("data\\twitter_credential.json") as json_file:
    auth_codes = json.load(json_file)

#Using auth_codes as a dictionary reference point, create another
#variable named auth that will have the OAuth1() method, which
#we will use to send our authorization to Twitter
auth = OAuth1(auth_codes['CONSUMER_KEY'], auth_codes['CONSUMER_SECRET'], auth_codes['ACCESS_TOKEN'], auth_codes['ACCESS_SECRET'])

#Create variable r which will run the POST method.
r = requests.post(url, params = tweet, auth=auth)

#print(r.status_code)
if r.status_code == 200:
    print("Your Tweet was successfully sent!")
else:
    print("Your Tweet was not send!")

