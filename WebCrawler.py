import urllib.request
from bs4 import BeautifulSoup
import requests


def downloader(addr, loc):
    name = addr[15:]
    #print(addr)
    ##print(name)
    urllib.request.urlretrieve('http:' + addr, loc + '\\' + name)
    return 1


def crawler(urlname, res_val):
    source_code = requests.get(urlname)
    plain_text = source_code.text
    i = 1
    soup = BeautifulSoup(plain_text, "html.parser")
    loc = input("Enter storage location : ")
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        if i >= res_val :
            address = str(link.get('href'))
            if downloader(address, loc):
                print(i)
                i += 1
        else:
            i += 1


url = r"http://boards.4chan.org/a/thread/146430368"
resume_val = int(input("Did the program halt? If yes, then at what point? If no, enter 1.") or "1")
crawler(url, resume_val)
