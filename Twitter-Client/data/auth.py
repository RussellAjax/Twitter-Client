import json

#Import your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = #Write your API Consumer key
credentials['CONSUMER_SECRET'] = #Write your API Consumer secret
credentials['ACCESS_TOKEN'] = #Write your Access Token
credentials['ACCESS_SECRET'] = #Write your Access Secret

#Save the credential object to file
with open("twitter_credential.json", "w") as file:
    json.dump(credentials, file)

#Run this Python file afterward to create a .json credentials file
