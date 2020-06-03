import requests
import json
from requests_oauthlib import OAuth1
import time

url = 'https://api.twitter.com/1.1/statuses/update.json'
tweet = {'status': 'Whatever happens, happens. #amorfati'}

#Authentication process
with open("C:\\Users\Ajax Russell\\amorfati\Twitter-Client\Twitter-Client\data\\twitter_credential.json") as json_file:
    auth_codes = json.load(json_file)
auth = OAuth1(auth_codes['CONSUMER_KEY'], auth_codes['CONSUMER_SECRET'], auth_codes['ACCESS_TOKEN'], auth_codes['ACCESS_SECRET'])

#Assume you want to send at 20:00
while True:
    if time.strftime("%H:%M") == "20:03":
        r = requests.post(url, params = tweet, auth = auth)
        if r.status_code == 200:
            print("Your Tweet was successfully sent!")
            break
        else:
            print("Your Tweet was not sent!")
    else:
        print("The time now is ")
        print(time.strftime("%H:%M"))
        time.sleep(60)
