'''import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import quote
import datetime
import json

base_url = "https://sg.carousell.com"
query_url = "https://sg.carousell.com/search/products/?query="




def crawl(query, min_price, max_price):
    min = int(min_price)
    max = int(max_price)
    #fi=open('C:\\Users\\Manik Chandra Biswas\\Desktop\\jj.txt','w')
    query = quote(query)
    print(query)
    #url = query_url + query
    url="https://www.carousell.sg/search/"+query+"?addRecent=true&searchId=bH-4y9&sort_by=3"
    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, "html5lib")
    #print(soup)
    #se=soup.find("D_eS D_eC D_eT D_eW D_eY D_fb D_ff D_eO")
    #print(se)
    print(soup.find_all("a"))

    for i in soup.find_all("div", class_="D_xW"):
        #print(i)
        
        name=i.find("p",class_="D_eS M_eV D_eA M_ci D_eT M_eW D_eW M_eZ D_eY M_fb D_fb M_ff D_ff M_fi D_eP").string
        her=i.find("a",class_="D_fE M_cF").get("href")
        href=base_url+her

        
        price=i.find("p",class_="D_eS M_eV D_eA M_ci D_eT M_eW D_eW M_eZ D_eY M_fb D_fb M_ff D_fe M_fh D_eO")
        p=price.string
        #D_eS M_eV D_et M_bZ D_eT M_eW D_eW M_eZ D_eY M_fb D_fb M_ff D_fe M_fh D_nI M_ig D_eQ
        #D_eS M_eV D_et M_bZ D_eT M_eW D_eW M_eZ D_eY M_fb D_fb M_ff D_fe M_fh D_nI M_ig D_eQ
        try:
            try:
                da=i.find("p",class_="D_eS M_eV D_eA M_ci D_eT M_eW D_eW M_eZ D_eY M_fb D_fb M_ff D_fe M_fh D_nI M_ig D_eQ").string
                day=da.split(" ")
            except:

                da=i.find("p",class_="D_eS M_eV D_et M_bZ D_eT M_eW D_eW M_eZ D_eY M_fb D_fb M_ff D_fe M_fh D_nI M_ig D_eQ").string
                day=da.split(" ")
        except:
            pass
        tod =  datetime.date.today()
        

        try:
            if (int(p[2:])>=min)and(int(p[2:])<=max):
                print("\033[92m {}\033[00m" .format("Name: "+name))
                print("\033[91m {}\033[00m" .format("Day: "+str(da)))
                print("\033[91m {}\033[00m" .format("Price: "+p[1:]))
                print("\033[93m {}\033[00m" .format("Url: "+href))
                print("\n")
                try:
                    file=open(query,"r")
                    li=file.readlines()
                    if (day[1]!="days") or (day[1]!="months") or (day[1]!="month"):
                        if (name+"\n") not in li:
                        #print(tod)
                            print("\033[92m {}\033[00m" .format("Name: "+name))
                            print("\033[91m {}\033[00m" .format("Day: "+str(da)))
                            print("\033[91m {}\033[00m" .format("Price: "+p[1:]))
                            print("\033[93m {}\033[00m" .format("Url: "+href))
                            print("\n")
                        #print(a)
                            fi=open(query,"a")
                            fi.write(name+"\n")
                            fi.close()
                    file.close()
                except:
                    file=open(query,"a+")
                    file.write(name+"\n")
                    file.close()
                    pass
                
                
                    print("\033[92m {}\033[00m" .format("Name: "+name))
                    print("\033[91m {}\033[00m" .format("Day: "+da))
                    print("\033[91m {}\033[00m" .format("Price: "+p[1:]))
                    print("\033[93m {}\033[00m" .format("Url: "+href))
                    print("\n")
                #fi.write(f"Name: {name}\n Price: {p[1:]} \n Url: {href} \n")
        except:
            pass
    #print("\033[92m Done \033[37m")
    #fi.close()
    #print(soup)

        

if __name__ == '__main__':

    print("\033[01m \033[04m \033[92m { - - WELCOME - - } \033[00m")
    print("\n")
    if(len(sys.argv) < 2):
        pass

    query = sys.argv[1]
    #print(query)
    if(len(sys.argv) == 2):
        crawl(query, 0, sys.maxsize)
    else:
        crawl(query, sys.argv[2], sys.argv[3])
    query=input("\033[93m Enter the Query => ")
    max=input("\033[92m Enter the max price => ")
    min=input("\033[92m Enter the min price => ")
    crawl(query,min,max)
    print("\033[92m Done \033[37m")
'''


import requests
import sys
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


def eml(l,name,url):

    title = 'My title'
    msg_content = (f"Name: {name} \n Url: {url}")
    message = MIMEText(msg_content, 'html')

    message['From'] = 'Reminder <sender@server>'
    message['To'] = 'Receiver Name <receiver@server>'
    message['Cc'] = 'Receiver2 Name <receiver2@server>'
    message['Subject'] = 'New Product Arived'

    msg_full = message.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login("newproductremind@gmail.com","sbis28330")
    
    server.sendmail('newproductremind@gmail.com',l,
                    msg_full)



name=[]
Url=[]
price=[]
day=[]
base_url = "https://sg.carousell.com"
def sc(query):
    url="https://www.carousell.sg/search/"+query+"?addRecent=true&searchId=bH-4y9&sort_by=3"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup=BeautifulSoup(plain_text,"html5lib")
    for i in soup.find_all("a"):
        s=str(i.get("href"))
        if s.startswith("/p/"):
            w=(i.find_all("img"))[-1].get("alt")
            #print(w)
            Url.append(base_url+s)
            
            name.append(w)
            nxt=i.find_all("p")
            for o in nxt:
                o1=str(o.string)
                #print(o1)
                if o1.startswith("S$"):
                    #print(o1)
                    price.append(o1)
            #print(i.find_all("p"))
        if s.startswith("/u/"):
            for n in i.find_all("p"):
                o2=str(n.string)
                if o2.endswith("ago"):
                    day.append(o2)
    return name,price,day,Url

#print(price)
def crawl(query, min_price, max_price):
    min = int(min_price)
    max = int(max_price)
    d=0
    while d<len(day):
        a=day[d].split(" ")
        try:
            if ((int(price[d][2:])>=min)and(int(price[d][2:]))<=max):
                try:
                        file=open(query,"r")
                        li=file.readlines()
                        if (a[1]!="days") or (a[1]!="months") or (a[1]!="month"):
                            if (name[d]+"\n") not in li:
                                print(f"Name: {name[d]}\n Day: {day[d]}\n Price: {price[d]}\n Url: {Url[d]}")
                                l="manikchandrabiswas72@gmail.com"
                                eml(l,name[d],Url[d])
                                fi=open(query,"a")
                                fi.write(name+"\n")
                                fi.close()
                        file.close()
                except:
                    file=open(query,"a+")
                    file.write(name[d]+"\n")
                    file.close()
        except:
            pass
        d=d+1
#print(len(name

if __name__ == '__main__':

    print(" { - - WELCOME - - } ")
    print("\n")
    if(len(sys.argv) < 2):
        pass

    query = sys.argv[1]
    #print(query)
    if(len(sys.argv) == 2):
        name,price,day,Url=sc(query)
        crawl(query, 0, sys.maxsize)
    else:
        name,price,day,Url=sc(query)
        crawl(query, sys.argv[2], sys.argv[3])