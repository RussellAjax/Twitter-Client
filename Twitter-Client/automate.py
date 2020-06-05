import requests
import time
from connect import url, auth

tweet = {'status': input("What's happening today? \n")}
post_time = str(input("What time do you want to post? "))
while True:
    if time.strftime("%H:%M") == post_time:
        automate = requests.post(url, params = tweet, auth = auth)
        if automate.status_code == 200:
            print("Your Tweet was successfully sent!")
            break
        else:
            print("Your Tweet was not sent!")
            print(automate.text)
    else:
        print("The time now is ")
        print(time.strftime("%H:%M"))
        time.sleep(60)
