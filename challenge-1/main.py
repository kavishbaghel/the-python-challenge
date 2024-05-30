#Challenge 1 - http://www.pythonchallenge.com/pc/def/map.html
import challenge_1
from os import name

if name=="__main__":
    given_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    current_page="map"

    print("The transformed text will be - ", challenge_1.transform_string(given_text))
    print("\n The next page url will be - ", challenge_1.get_next_challenge_url(current_page))