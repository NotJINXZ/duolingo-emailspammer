import requests, os, uuid, secrets, threading, time
os.system('title DUOLINGO SPAMMER / 0 CREATED' )

class Duolingo:
    def __init__(self, email):
        self.session = requests.Session()
        self.email, self.domain = email.split('@')
        self.accounts = 0

    def register(self):
        json = {
            "distinctId": str(uuid.uuid4()),
            "fromLanguage": "en",
            "initialReferrer": "$direct",
            "landingUrl": "https://www.duolingo.com/learn",
            "learningLanguage": "es",
            "timezone": "America/Vancouver"
        }
        response = self.session.post('https://www.duolingo.com/2017-06-30/users?fields=id', json=json)
        return response.cookies['jwt_token'], response.json()['id']

    def profile(self):
        account = self.register()
        jwt = account[0]
        id = account[1]
        headers = {
            "authorization": "Bearer %s" % jwt
        }
        json = {
            "age": "18",
            "email": f"{self.email}+%s@{self.domain}" % secrets.token_hex(8),
            "identifier": "",
            "name": "",
            "password": secrets.token_hex(4),
            "username": None
        }
        response = self.session.patch('https://www.duolingo.com/2017-06-30/users/%s?fields=adsConfig,email,identifier,name,privacySettings,trackingProperties,username' % id, headers=headers, json=json)
        with self.lock:
            print("SUCCESSFULLY MADE USER : %s" % response.json()['username'])
        self.accounts += 1
        os.system('title DUOLINGO / %s CREATED' % self.accounts)

    def start(self):
        os.system('cls;clear')
        input("PRESS ENTER WHEN YOU'RE READY")
        os.system('cls;clear')
        while True:
            threading.Thread(target=self.profile).start()
            time.sleep(0.33) # lower this all u want
            
email = input("EMAIL : ")
Duolingo(email).start()
