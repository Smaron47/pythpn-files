#from numpy.lib.arraysetops import _isin_dispatcher
import pytesseract
import PIL
import re
import os
import threading 

from tkinter import *
from tkinter import filedialog
import pdf2image

#globals
sd=[]
root=Tk()
pytesseract.pytesseract.tesseract_cmd="tesseract"
root.geometry("400x400")
def browse():
    p=filedialog.askdirectory()
    fpa.set(p)
    
    #print(p)
    return p
def cl():
    root.destroy()

def clear():
    label2 = Label(root, text = f"                                                                      ", font = ("arial", 16, "bold"))
    label2.place(x = 0, y = 250)

def pr(erw):
    label2 = Label(root, text = f"   File : {erw} done ", font = ("arial", 16, "bold"))
    label2.place(x = 0, y = 200)


def th():
    t=threading.Thread(target=any_file)
    t.start()
def th1():
    t1=threading.Thread(target=pdf_1)
    t1.start()
def th2():
    t2=threading.Thread(target=image_1)
    t2.start()
def th3():
    t3=threading.Thread(target=clear)
    t3.start()
def any_file():
    sdfr=1
    pat=fpa.get()+"/"
    qw=len(os.listdir(pat))
    for i in os.listdir(pat):
        u=pat+i
        yu=str(sdfr)+"\\"+str(qw)
        try :
            if u.endswith(".pdf"):

                pdf(u)
                pr(yu)
            else:
                image(u)
                pr(yu)
            sdfr = sdfr+1
        except :
            pass
    label2 = Label(root, text = f"    Total : {sum(sd)} ", font = ("arial", 16, "bold"))
    label2.place(x = 0, y = 250)
    sd.clear()
def pdf_1():
    sdfr=1
    pat=fpa.get()+"/"
    qw=len(os.listdir(pat))
    for i in os.listdir(pat):
        u=pat+i
        try :
            if u.endswith(".pdf"):
                yu=str(sdfr)+"\\"+str(qw)
                pdf(u)
                pr(yu)
                sdfr=sdfr+1
        except :
            pass
    label2 = Label(root, text = f"    Total : {sum(sd)} ", font = ("arial", 16, "bold"))
    label2.place(x = 0, y = 250)
    sd.clear()
def image_1():
    sdfr=1
    pat=fpa.get()+"/"
    qw=len(os.listdir(pat))
    for i in os.listdir(pat):
        u=pat+i
        try:
            if  not u.endswith(".pdf"):
                yu=str(sdfr)+"\\"+str(qw)
                image(u)
                pr(yu)
                sdfr=sdfr+1
        except:
            pass
    label2 = Label(root, text = f"    Total : {sum(sd)} ", font = ("arial", 16, "bold"))
    label2.place(x = 0, y = 250)
    sd.clear()

def lo(sw):
        
        try:
            o=re.findall("\d\d\d+\.\d\d",sw)
            w=float(o[-1])
            sd.append(w)
            #print(sd)
        except:
            try:
                o=re.findall("\$\d+",sw)
                #print(o)
                m=(o[-1])
                m=m.replace("$","")
                #print(m)
                sd.append(int(m))
            except:
                try:
                    o=re.findall("\d\d+\,\d\d",sw)
                    #print(o)
                    m=(o[-1])
                    m=m.replace(",",".")
                    #print(m)
                    sd.append(float(m))
                except:
                    try:
                        o=re.findall("\$\d+\.\d\d",sw)
                        #print(o)
                        m=(o[-1])
                        m=m.replace(",",".")
                        #print(m)
                        sd.append(float(m))
                    except:
                        pass
        print(sd)

        
            



def image(rs):
    img=PIL.Image.open(f"{rs}")
    r=pytesseract.image_to_string(img)
    #print(r)
    #print(type(r))
    
    lo(r)
#print hello world
    #print(rs,w,sd)
def pdf(es):
        #m=filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
    d=pdf2image.convert_from_path(es)
    for s in d:
        s2="sdf"+".jpg"
        s.save(s2, "JPEG")

        wp=PIL.Image.open(s2)
        sf=pytesseract.image_to_string(wp)
        lo(sf)
    
    #print(rs)
#print(sum(sd))


b1=Button(root, text = "Browse", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = browse)
b1.place(x = 290, y = 50)
fpa = StringVar()
fpa.get()
textBox1 = Entry(root, textvar = fpa, width = 35, font = ("arial", 11, "bold"))
textBox1.place(x = 5, y = 55)
any1=Button(root, text = "Image", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = th2)
any1.place(x = 90, y = 160)
pdf1=Button(root, text = "Pdf", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = th1)
pdf1.place(x = 195, y = 160)
image1=Button(root, text = "Any File", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = th)
image1.place(x = 120, y = 120)
close1=Button(root, text = "Close", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = cl)
close1.place(x = 290, y = 300)
clear1=Button(root, text = "Clear", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = th3)
clear1.place(x = 10, y = 300)
root.mainloop()


'''from re import A
from bs4 import BeautifulSoup

import requests
import re 

#File = open("out.csv", "a")
url=input("Enter ther Url: ")
HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
URL=url
webpage = requests.get(URL, headers=HEADERS)
li=[]
soup = BeautifulSoup(webpage.content, "lxml")
it=soup.find_all("a",class_="a-link-normal")
o=0
bs="https://www.amazon.com/"
while o<len(it):
    if str(it[o]['href']).startswith("/product-reviews") :
        pass
   
    
    else:
        li.append(bs+it[o]["href"])
    o=o+1

sm=0
row=0
while sm<len(li):
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    URL=li[sm]
    wbpg=requests.get(URL,headers=HEADERS)
    soup = BeautifulSoup(wbpg.content, "lxml")
    
    try:
        e=soup.find('div', id=('detailBulletsWrapper_feature_div')).text
        #print("".join(e.text.strip().replace("\n"," ").replace('                                 ', ' ')))
        if 'Dimensions' in e:
                        dimension = re.split(r"Dimensions", e)
                        a = dimension[1].strip().replace(' ', '')
                        b = re.split(r'[B]', a)
                        c = b[0]
                        dimension_original = re.split(r'\n|Dimensions', c)
                        #print(dimension_original)
                        dimension_original = dimension_original[-2]
        if 'Weight' in e:
                        weight = re.split(r"Weight", e)
                        a = weight[1].strip().replace(' ', '')
                        b = re.split(r'[D]', a)
                        c = b[0]
                        weight_original = re.split(r'\n|Dimensions', c)
                        weight_original = weight_original[-1]
        if 'Best Sellers Rank' in e:
                        rank = re.split(r"Best", e)
                        a = rank[1].strip().replace(' ', '')
                        rank = a.replace('\n', ' ')
                        rank = re.split(r"Customer", rank)
                        rank = rank[0]
        if 'Publisher' in e:
                        date = re.split(r"[()]", e)
                        date = date[1].strip().replace(' ', '')
                        manufacturer = re.split(r"[:(]", e)
                        manufacturer = manufacturer[1].strip().replace('\n', '')
                        manufacturer = manufacturer.replace('                         ', '')
                        manufacturer = manufacturer.replace('    ', '')

        print(manufacturer,rank,weight_original,dimension_original)
        e=soup.find("a", {"class": "a-size-small a-link-normal authorNameLink a-text-normal"})
        print(e.text)
        q=soup.find("img",{"class":"a-dynamic-image image-stretch-horizontal frontImage"})
        print(q["src"])
        e=soup.find("span", {"data-hook": "rating-out-of-text"})
        print(e.text)


        overview = soup.find('div',class_='a-expander-collapsed-height a-row a-expander-container a-spacing-base a-expander-partial-collapse-container').text.strip().replace('\n', ' ')
        overview = overview.replace('                          ', ' ')
        sold_by = soup.find('div', class_='tabular-buybox-text a-spacing-none').text.strip()
        ships_from = soup.find('div', class_='tabular-buybox-text a-spacing-none').text.strip()
        category_structrure = 'Best Sellers>Books'
        category = 'Best Sellers>Books'
        questions = ' NA '
        front_image_url = soup.find("img",{"class":"a-dynamic-image image-stretch-horizontal frontImage"})['src']
        back_image_url = ''
        prime = ' '
        discontinued = ' '
        item_model_number = ' '
        department = ' '
        asin = ' '
        sellers_and_name = ' '
        titl=soup.find("span", {"id": "productTitle"}).text
        subtitle=soup.find("span", {"id": "productSubtitle"}).text
        review=soup.find("span", {"id": "acrCustomerReviewText"}).text
        artor=soup.find("a", {"class": "a-size-small a-link-normal authorNameLink a-text-normal"}).text
        reting=soup.find("span", {"data-hook": "rating-out-of-text"}).text
        price=soup.find("span",class_="a-size-base a-color-secondary").text
        publisher=manufacturer

        video=len(soup.find_all('div', class_='vse-video-content'))
        print(titl+"\n"+li[sm]+"\n"+reting+"\n"+review+"\n"+questions+"\n"+price+"ETC")
        break
    except:
        pass
    sm=sm+2

'''


'''
                '''

'''

print(dimension_original,manufacturer,rank,weight_original)'''
'''
Title - Atlas of the Heart: Mapping Meaningful Connection and the Language of Human Experience
Url - https://www.amazon.com/Atlas-Heart-Meaningful-Connection-Experience/dp/0399592555/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=&sr=
Stars - 4.8 out of 5
rating -  5,114 ratings
qustion answered
price-$18
product over view
font image url
back image url 
ships from
sold by
New
Used
prime?
product description
Discontunued 
product 
item model number - 0399592555
department
date first - November 30, 2021
seller name
category
'''
#print(n,len(n))
'''url="https://www.amazon.com//Stop-Overthinking-Techniques-Declutter-Emotional/dp/B08XLLF3PG/ref=zg_bs_3_30/141-3327487-0769010?pd_rd_i=B08XLLF3PG&psc=1"

w=requests.get(url,HEADERS)
print(w.text)'''
#while o<len(n):

'''from requests import get
import cv2
import numpy as np 




url="https://localhost:1232/shot.jpg"

while True:
    imgre=get(url)
    imgar=np.array(bytearray(imgre.content),dtype=np.uint8)
    img=cv2.imdecode(imgar,-1)
    cv2.imshow("Try",img)

    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()'''

k=float(input())
o=int(int(k)/10)
print("["+"+"*o+"."*(10-o)+"]")
