import urllib.request
from bs4 import BeautifulSoup
import requests
import datetime


def downloader(addr, loc):
    name = addr[15:]
    #print(addr)
    ##print(name)
    urllib.request.urlretrieve('http:' + addr, loc + '\\' + name)
    return 1


def crawler(urlname, res_val):
    source_code = requests.get(urlname)
    plain_text = source_code.text

    logname = str(datetime.datetime.now()).replace('.', "-")
    logname = logname.replace(':', '-')
    #logname.replace(':', '-')
    print (logname)

    i = 1
    soup = BeautifulSoup(plain_text, "html.parser")
    loc = input("Enter storage location : ")

    for link in soup.findAll('a', {'class': 'fileThumb'}):
        if i >= res_val :
            address = str(link.get('href'))
            name = address[15:]
            fwr = open(loc + "\\" + logname + ".txt", 'w')
            if downloader(address, loc):
                print(i)
                fwr.write("\t" + str(i) + "\t" + name)
                i += 1
        else:
            i += 1


url = input("Enter the URL : ")
resume_val = int(input("""Did the program halt?
If yes, then at what point?
If no, just hit enter.""") or "1")
crawler(url, resume_val)