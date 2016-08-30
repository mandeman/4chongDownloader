import urllib.request
from bs4 import BeautifulSoup
import requests
import threading
import datetime                 #only to generate logname

#Downloader logic. Accepts Image URL and storage location
def downloader(addr, loc):
    name = addr[15:]
    urllib.request.urlretrieve('http:' + addr, loc + '\\' + name)
    return 1
    #Why return 1?

#Crawl logic
def crawler(urlname, res_val, loc):
    #Get source code from the webpage
    source_code = requests.get(urlname).text

    #Turn the source code into beautiful soup object
    #Really beautiful tbh
    soup = BeautifulSoup(source_code, "html.parser")

    logname = str(datetime.datetime.now()).replace('.', "-")
    logname = logname.replace(':', '-')

    #How many images have been downloaded?
    #Why 1? Because this has to at least download one image
    #The program doesn't suck that bad
    #But yeah, this seemed easier to implement
    i = 1

    #Find all links whose class is fileThumb
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        #Download only the images that are greater than/equal to the resume value
        if i >= res_val :
            #Get the address of the links
            address = link.get('href')
            name = address[15:]

            #log file writing
            fwr = open(loc + "\\" + logname + ".txt", 'w')
            if downloader(address, loc):
                print(i)
                fwr.write("\t" + str(i) + "\t" + name)
                i += 1
        else:
            i += 1


url = input("Enter the URL : ")
url = url.rstrip()
resume_val = int(input("""Did the program halt?
If yes, then at what point?
If no, just hit enter.""") or "1")
loc = input("Enter storage location : ")
crawler(url, resume_val, loc)
print("Done with the downloads!")