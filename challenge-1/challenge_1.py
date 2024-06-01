#Challenge 1 - http://www.pythonchallenge.com/pc/def/map.html

""" This function adds 2 to the ascii value if the character is an alphabet and then checks if the resulting character is an alphabet then appends it to the transformed_text string variable, 
if the character is not an alphabet it subtracts 26 from the ascii value of the character and appends the resulting character to the transfomed text string.

If the initial character is not an alphabet it is directly appended to the transformed text string."""

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

# This function takes the current page name as input and transforms it to the next page and returns the value of the next page url as asked in the problem.
def get_next_challenge_url(current_page):
    next_page=""
    for x in current_page:
        next_page = next_page + chr(ord(x) + 2)
    return "http://www.pythonchallenge.com/pc/def/" + next_page + ".html"
