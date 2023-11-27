import requests
import youtube_dl
from os import system as c
ydl_opts = {'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]}
s=input("Enter the name of Song : ")
s.replace(' ','+')
r=requests.get(f"https://www.youtube.com/results?search_query={s}").text
k=r.find('watch?v=')
c(f'youtube-dl https://www.youtube.com/{r[k:k+19]}')
input()

import re 
import requests

l=requests.get('https://www.google.com/search?q=weather+in+faridpur+bangladesh').text
p=(l.find('<div class="BNeawe iBp4i AP7Wnd">'))
fil.write(l[p+71:p+74])
response = requests.get(f"https://ipinfo.io/103.78.254.10/json").json()
fil.write(response)


from pytube import YouTube 
import requests
# where to save 
SAVE_PATH = "/home/smaron/Desktop/python files" #to_do 
  
# link of the video to be downloaded 
s=input("Enter the name of Song : ")
s.replace(' ','+')
r=requests.get(f"https://www.youtube.com/results?search_query={s}").text
k=r.find('watch?v=')

link=f"https://www.youtube.com/{r[k:k+19]}"
  
yt = YouTube(link)

# filters out all the files with "mp4" extension 
fil.write(yt.title)
stream = yt.streams.first() 
stream.download(SAVE_PATH) 

fil.write('Task Completed!')
 
import requests

def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open("/home/smaron/Desktop/python files"+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: 
                f.write(chunk)
                

earl = f"https://i.pinimg.com/originals/8f/ad/12/8fad125b8f6082bdb7deb0aa593dfb49.jpg"
download_file(earl)
fil.write('Done')

import requests
import pytube
s=input("Enter the name of Song : ")
s=s.replace(' ','+')
r=requests.get(f"https://www.youtube.com/results?search_query={s}").text
k=r.find('watch?v=')
link=f"https://www.youtube.com/{r[k:k+19]}"
pytube.YouTube(link).streams.get_by_itag(251).download()

import pygame

pygame.mixer.init()
pygame.mixer.music.load("/home/smaron/Desktop/songs/Baby-Justin Bieber ft Ludacris[www.soundbd24.tk].mp3")
pygame.mixer.music.play()
fil.write("playing")












'''
from bs4 import BeautifulSoup as bs
import requests
import json



#res=requests.get("https://www.daraz.com.bd/products/avita-magus-2-in-1-celeron-n3350-122-inch-4gb-64gb-emmc-windows-10-home-charcoal-grey-laptop-i181129564-s1122669923.html?spm=a2a0e.searchlist.list.11.26927463FkKBGL&search=1").text


span=bs(res,"html.parser")
sp=span.find("span",class_=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl")
fil.write("\n")
fil.write(sp.get_text())
fil.write("\n")

li=[]
w=requests.get("https://www.daraz.com.bd/traditional-laptops/?spm=a2a0e.pdp.breadcrumb.3.406f682aSVizZB").text
#fil.write(w)
fil=open("daraz.txt","w")
fil.write("20 pages and porducts in 20 seconds")
k=bs(w)
k=k.find_all("script",type="application/ld+json")
a_dict=json.loads(k[1].get_text())
for i in a_dict:
    
    if i == "itemListElement":
        for k in a_dict[i]:
            li.append(k["url"])
    print("First Step Done")

qwer=1
errt=len(li)-20
for u in li:
    res=requests.get(u).text
    span=bs(res,"html.parser")
    sp=span.find("span",class_="breadcrumb_item_anchor breadcrumb_item_anchor_last")
    wew=res.find("salePrice")
    your_string=(res[wew:wew+100])

    an=json.loads(your_string[your_string.find("{") : your_string.find("}")+1])
    fil.write("\n")
    fil.write("\n")
    fil.write(f'Product Name:{sp.get_text()}')
    fil.write("\n")
    fil.write(f'Price : {an["text"]}')
    fil.write("\n")
    fil.write("\n")
    fi=res.find("<ul class=''>")
    sm=(res[fi:fi+3000])
    fi2=sm.find("</ul>")
    resu=(sm[:fi2+5])
    res1=bs(resu,"html.parser")
    for l in res1.find_all("li"):
        fil.write(f"Details:{l.get_text()}")
    
    print(f"{qwer}/{errt} Url Done")
    if qwer==20:
        break
    qwer=qwer+1


fil.close()
#fil.write(f)
#fil.write(len(f))

e=k.find_all("div",id="root")
fil.write(len(e))
fil.write(e)
f=bs(str(e))
fil.write(f.find_all("div"))
for i in e:
    
    try:
        req=requests.get(i["href"]).text
        sp=bs(req)
        spa=sp.find("span",class_="pdp-mod-product-badge-title")
        fil.write(spa)
    except:
        pass
    fil.write(i["href"])
    time.sleep(1)
fil.write(len(e))'''
