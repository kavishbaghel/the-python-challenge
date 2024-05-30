#Challenge 1 - http://www.pythonchallenge.com/pc/def/map.html

def transform_string(given_text):
    transformed_text = ""
    for x in given_text:
        b = chr(ord(x) +2)
        if x.isalpha():
            if b.isalpha():
                transformed_text = transformed_text + b
            else:
                transformed_text = transformed_text + chr(ord(b)-26)
        else:
            transformed_text = transformed_text + x
    return transformed_text

def get_next_challenge_url(current_page):
    next_page=""
    for x in current_page:
        next_page = next_page + chr(ord(x) + 2)
    return "http://www.pythonchallenge.com/pc/def/" + next_page + ".html"
