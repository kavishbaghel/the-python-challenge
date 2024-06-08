import PIL.Image
import requests
import re


def download_image(url, image):
    f=open(image, "wb")
    f.write(requests.get(url).content)
    f.close()

def extract_data_from_image(image):
    img = PIL.Image.open(image)
    height=img.height
    width=img.width
    row=[img.getpixel((i, height/2)) for i in range(width)]
    row=row[::7]
    ords = [r for r, g, b, a in row if r==g==b]
    chrs = "".join(map(chr, ords))
    data = "".join(re.findall("[\[1-9][\,][\" \"]]", chrs))
    print(data)

def get_next_challenge_url(ords):
    #code
    return None


extract_data_from_image("oxygen.png")