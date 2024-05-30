#Challenge 2: http://www.pythonchallenge.com/pc/def/ocr.html

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

def get_next_challenge_url(item_count):
    next_page=""
    for k in item_count:
        if item_count[k] <= 1:
            next_page = next_page + k
    return "http://www.pythonchallenge.com/pc/def/" + next_page + ".html"