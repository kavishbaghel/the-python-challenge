#Challenge 3: http://www.pythonchallenge.com/pc/def/equality.html

import challenge_3

file_path="data.txt"
data=challenge_3.read_data(file_path)
print("The next challenge url is - ", challenge_3.get_next_challenge_url(data))