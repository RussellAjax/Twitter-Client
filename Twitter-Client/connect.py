import requests
import json
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/statuses/update.json'
with open("C:\\Users\Ajax Russell\\amorfati\Twitter-Client\Twitter-Client\data\\twitter_credential.json") as json_file:
    auth_codes = json.load(json_file)

auth = OAuth1(auth_codes['CONSUMER_KEY'], auth_codes['CONSUMER_SECRET'], auth_codes['ACCESS_TOKEN'], auth_codes['ACCESS_SECRET'])
