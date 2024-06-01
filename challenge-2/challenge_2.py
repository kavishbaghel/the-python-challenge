#Challenge 2: http://www.pythonchallenge.com/pc/def/ocr.html

import re

def read_data(file_path):
    with open(file_path, "r") as f:
        data=f.read()
    return data

def get_item_counts(data):
    item_count = {}
    for i in data:
        if i not in item_count:
            item_count[i] = 1
        else:
            item_count[i] += 1
    return item_count


#Updated solution taken from here for correct url - https://www.hackingnote.com/en/python-challenge-solutions/level-2/index.html
def get_next_challenge_url(data):
    next_page = "".join(re.findall("[A-Za-z]", data))
    return "http://www.pythonchallenge.com/pc/def/" + next_page + ".html"