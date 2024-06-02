# Challenge 4: http://www.pythonchallenge.com/pc/def/linkedlist.html --> http://www.pythonchallenge.com/pc/def/linkedlist.php 

import requests
import re

def url_iteration(url):
    n=0
    while True:
        response = requests.get(url)
        nothing = "".join(re.findall("[0-9]", response.text))
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
        if not nothing.isnumeric():
            break
        n=nothing
    return n

def next_challenge_url(url):
    response = requests.get(url)
    return "http://www.pythonchallenge.com/pc/def/" + response.text