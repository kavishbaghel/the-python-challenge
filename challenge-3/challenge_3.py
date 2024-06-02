#Challenge 3: http://www.pythonchallenge.com/pc/def/equality.html

import re

# This function reads the data from the given file
def read_data(file_path):
    with open(file_path, "r") as f:
        data=f.read()
    return data

def get_next_challenge_url(data):
    next_page = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))
    return "http://www.pythonchallenge.com/pc/def/" + next_page + ".html"
