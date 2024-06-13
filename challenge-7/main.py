#Challenge 5: http://www.pythonchallenge.com/pc/def/oxygen.html

import challenge_7

image_url="http://www.pythonchallenge.com/pc/def/oxygen.png"
image="oxygen.png"
data=[105, 110, 116, 101, 103, 114, 105, 116, 121]

challenge_7.download_image(image_url, image)
challenge_7.extract_data_from_image(image)
challenge_7.get_next_challenge_url(data)