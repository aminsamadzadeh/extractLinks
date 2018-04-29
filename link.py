from bs4 import BeautifulSoup
from urllib.parse import unquote
import requests
import sys


def create_url(mainurl, link):
    if 'http' not in link:
        return mainurl+link
    else:
        return link

url = sys.argv[1]
ext = None
if len(sys.argv) == 3:
    ext = sys.argv[2]

print(ext)
print(url)
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
atags = soup.find_all('a')

path = url.split('/')[-1]
if path == '':
    path = url.split('/')[-2]
path = unquote(path)
print(path)

file = open(path, 'w+')
for a in atags:
    link = a['href']
    if link != '../':
        if ext != None:
            if ext in link:
                file.write(create_url(url, link)+'\n')
                print(create_url(url, link))
        else:
            file.write(create_url(url, link)+'\n')
            print(create_url(url, link))

file.close()
    

