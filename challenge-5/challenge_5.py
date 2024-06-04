#Challenge 5: http://www.pythonchallenge.com/pc/def/peak.html

import requests
import pickle


def download_file(url):
    response = requests.get(url)
    f = open("peakhell", "wb")
    f.write(response.content)
    f.close()
    return "peakhell"
    
def read_data(file_path):
    ph = open(file_path, "rb")
    data=pickle.load(ph)
    ph.close()
    return data

def show_banner(data):
    print("Banner is -\n\n\n")
    for i in data:
        print("".join([x*y for x,y in i]))

def next_challenge_url():
    print("Next challenge - http://www.pythonchallenge.com/pc/def/channel.html")
