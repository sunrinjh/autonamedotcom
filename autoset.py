import requests

def readSetting():
    try:
        with open('settings.txt', 'r') as f:
            settings = f.read().splitlines()
            return settings
            
    except FileNotFoundError:
        print("run gettoken.py first")
        quit()

def getip():
    _ip = requests.get('https://api.ipify.org').text
    return _ip

def isChange(currentIp):
    try:
        with open('ip.txt', 'r') as f:
            return not (f.read() == currentIp)
    except FileNotFoundError:
        with open('ip.txt', 'w') as f:
            return True
    
def saveip(currentIp):
    with open('ip.txt', 'w') as f:
        f.write(currentIp)
    
def updateRecord(setting):
    username, token, domain, id = setting
    session = requests.Session()
    session.auth = (username, token)
    headers = {'Content-Type': 'application/json'}
    payload = '{"host":"","type":"A","answer":"'+ip+'","ttl":300}'
    response = session.put("https://api.name.com/v4/domains/"+domain+"/records/"+id ,headers=headers, data=payload)
    print(response.text)

ip = getip()

if isChange(ip):
    print("Changed")
    saveip(ip)
    updateRecord(readSetting())
else:
    print("UnChanged, Terminating the program.")
    quit()



