import requests
import json
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/statuses/update.json'
ask_tweet = input("What's happening today?\n")
tweet = {'status': ask_tweet}

with open("data\\twitter_credential.json") as json_file:
    auth_codes = json.load(json_file)

auth = OAuth1(auth_codes['CONSUMER_KEY'], auth_codes['CONSUMER_SECRET'], auth_codes['ACCESS_TOKEN'], auth_codes['ACCESS_SECRET'])

r = requests.post(url, params = tweet, auth=auth)
#print(r.status_code)
if r.status_code == 200:
    print("Your Tweet was successfully sent!")
else:
    print("Your Tweet was not send!")

