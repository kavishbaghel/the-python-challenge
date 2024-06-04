#Challenge 5: http://www.pythonchallenge.com/pc/def/peak.html

import challenge_5

url="http://www.pythonchallenge.com/pc/def/banner.p"
file = challenge_5.download_file(url)
data=challenge_5.read_data(file)
challenge_5.show_banner(data)
challenge_5.next_challenge_url()