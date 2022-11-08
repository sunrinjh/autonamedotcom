import requests
import json

username = input("Username : ")
token = input("Token : ")
domain = input("Domain Name : ")
id = None

session = requests.Session()
session.auth = (username, token)

response = session.get('https://api.name.com/v4/domains/'+domain+'/records')
try:
    id = json.loads(response.text)['records'][0]['id']
    with open('settings.txt', 'w') as f:
        f.write(username+'\n'+token+'\n'+domain+'\n'+str(id))
        print("Setting Saved")
except KeyError:
    print("Please Re-try")