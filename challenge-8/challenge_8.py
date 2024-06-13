# Challenge 8 - http://www.pythonchallenge.com/pc/def/integrity.html

import bz2
import requests
from requests.auth import HTTPBasicAuth

def get_username_password(un, pw):
    username = bz2.decompress(un).decode("utf-8")
    password = bz2.decompress(pw).decode("utf-8")
    return [username, password]

def get_next_challenge_url(un, pw, login_url):
    response = requests.get(login_url, auth=HTTPBasicAuth(un, pw))
    print("Next challenege URL is - ", response.url)