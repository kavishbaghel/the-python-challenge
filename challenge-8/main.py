# Challenge 8 - http://www.pythonchallenge.com/pc/def/integrity.html

import challenge_8

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
login_url = "http://www.pythonchallenge.com/pc/return/good.html"

creds=challenge_8.get_username_password(un, pw)
challenge_8.get_next_challenge_url(creds[0], creds[1], login_url)