import requests
from connect import url, auth

tweet = {'status': input("What's happening today?\n")}

r = requests.post(url, params = tweet, auth=auth)
#print(r.status_code)
if r.status_code == 200:
    print("Your Tweet was successfully sent!")
else:
    print("Your Tweet was not sent!\n")
    print(r.text)


