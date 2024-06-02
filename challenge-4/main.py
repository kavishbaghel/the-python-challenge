# Challenge 4: http://www.pythonchallenge.com/pc/def/linkedlist.html --> http://www.pythonchallenge.com/pc/def/linkedlist.php

import challenge_4

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
x=challenge_4.url_iteration(url)
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(int(x)/2)
x=challenge_4.url_iteration(url)
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + x
print(challenge_4.next_challenge_url(url))