#Challenge 2: http://www.pythonchallenge.com/pc/def/ocr.html

import challenge_2
from os import name


file_path="data.txt"
data=challenge_2.read_data(file_path)
item_count=challenge_2.get_item_counts(data)
print("The next challenge url is - ", challenge_2.get_next_challenge_url(item_count))
