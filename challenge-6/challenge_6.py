import zipfile
import re
import requests

def read_files(zip_file, next_file):
    f = zipfile.ZipFile(zip_file)
    comment = f.read(next_file).decode("utf-8")
    return comment

def get_file_info(zip_file, next_file):
    f = zipfile.ZipFile(zip_file)
    com = f.getinfo(next_file).comment.decode("utf-8")
    f.close()
    return com


def collect_comments(zip_file, next_file):
    comments = []
    while True:
        comment = read_files(zip_file, next_file)
        comments.append(get_file_info(zip_file, next_file))
        next_file = "".join(re.findall("[0-9]", comment))
        if next_file.isnumeric():
            next_file = next_file + ".txt"
        else:
            break
    return "".join(comments)

def get_next_challenge_url():
    solution = requests.get("http://www.pythonchallenge.com/pc/def/hockey.html").content.decode("utf-8")
    print(solution)
    return "http://www.pythonchallenge.com/pc/def/oxygen.html"