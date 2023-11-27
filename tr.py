'''


from collections import Counter
import json
from pyspark.sql import SparkSession
 
def mktm(l):
    words = l
    word_counts = Counter(words)
    word_counts = str(word_counts).replace("Counter(","")
    word_counts=word_counts.replace(")","").replace(","," ,").replace("'","\"")
    #print(type(word_counts),word_counts)

    word= json.loads(word_counts)
    #print(type(word_counts))
    word=word.fromkeys(word,0)
    #print(word)
    return word
spark = SparkSession.builder.appName('Read Multiple CSV Files').getOrCreate()
 
path ="/home/smaron/Desktop/season-1415_csv.csv"
spark.conf.set("spark.debug.maxToStringFields",100000)
#spark.debug.maxToStringFields=100
files = spark.read.csv(path, sep=',',
                       inferSchema=True, header=True)

df1 = files.toPandas()
#print(df1["HomeTeam"])


teams=mktm(df1["HomeTeam"])
for i,c in zip(df1["HomeTeam"],df1["FTHG"]):
    if i in teams:
        teams[i]=teams[i]+c

teams1=mktm(df1["AwayTeam"])
for k,p in zip(df1["AwayTeam"],df1["FTAG"]):
    if k in teams:
        teams1[k]=teams1[k]+p
z = dict(Counter(teams)+Counter(teams1))
print(z)



'''

'''
from apscheduler.schedulers.background import BackgroundScheduler



sched = BackgroundScheduler(daemon=True)
sched.start()'''


'''import docx
import pandas as pd

# i am not sure how you are getting your data, but you said it is a
# pandas data frame
df = pd.read_excel("Ex1.xls")

# open an existing document
doc = docx.Document()

# add a table to the end and create a reference variable
# extra row is so we can add the header row
t = doc.add_table(df.shape[0]+1, df.shape[1])

# add the header rows.
for j in range(df.shape[-1]):
    t.cell(0,j).text = df.columns[j]

# add the rest of the data frame
for i in range(df.shape[0]):
    for j in range(df.shape[-1]):
        t.cell(i+1,j).text = str(df.values[i,j])

# save the doc
doc.save('mf.docx')'''
'''from openpyxl import load_workbook
wb = load_workbook(filename='Ex1.xlsx', read_only=True)
worksheet = wb.active
print(worksheet['A1'].font.color)
'''
'''import fbchat


cli=fbchat.Client("01772803606","Try to hack $m@r(*)n")
cli.send("Ekta Pic daw. Tomar na.","100045999454076")
print("message Sent")
'''

'''from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
usernam=str(input('Enter your username: '))
password=str(input('Enter your Password: '))
frndId = str(input('Enter your friend or Group Id: '))
message = str(input('Enter your text message here: '))
#this is where i open a new window
driver = webdriver.Chrome(ChromeDriverManager().install())
#this is where i open facebook
driver.get ('https://www.facebook.com/')
# this is where i start entering my username and password.
driver.find_element_by_id("email").send_keys(usernam)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_name("login").click() # I click login button
# login process done I am now on facebook
sleep(1)
# i start navigating to message and click on the friend i wanna messsage
mesgAdd='https://www.facebook.com/messages/t/'
mesgLink=mesgAdd+frndId
driver.get(mesgLink)
sleep (1)
#This is Where I clicked the Send Message '
driver.find_element_by_xpath('//div[@class="_1mf _1mj"]').send_keys(message, Keys.ENTER)
'''
# This is where I entered the keys and Did Enter
'''
this is how it should look like

<span data-lexical-text="true">aaassssddd</span>



Enter your username abdahi.oladejo.10
Enter your Password 9ad3e22
Enter your friend or Group Id100016740336536/
Enter your text message here how are you doing



from email.message import Message
import fbchat


session = fbchat.login("01772803606","Try to hack $m@r(*)n")
listener = fbchat.Listener(session=session, chat_on=False, foreground=False)

for event in listener.listen():
    if isinstance(event, fbchat.MessageEvent):
        print(f"{event.message.text} from {event.author.id} in {event.thread.id}")
        # If you're not the author, echo
        if event.author.id == session.user.id:
            event.thread.send_text(event.message.text)

'''

params = {'email':"01772803606", 'pass':"Try to hack $m@r(*)n"}




import bs4
from django.template import base
import requests
import fbchat

session=requests.Session()
base_url='https://m.facebook.com'
login_form_url = '/login/device-based/regular/login/?refsrc=https%3A'\
        '%2F%2Fmobile.facebook.com%2Flogin%2Fdevice-based%2Fedit-user%2F&lwv=100'

suburl="/messages/send/?icm=1&entrypoint=jewel&surface_hierarchy=unknown&refid=12"
print(base_url+suburl)
logged_request = session.post(base_url+login_form_url, data=params)
"/messages/send/?icm=1&entrypoint=jewel&surface_hierarchy=unknown&refid=12"

def find_input_fields(html):
    return bs4.BeautifulSoup(html, "html.parser", parse_only=bs4.SoupStrainer("input"))



def _do_send_request(da):
        #now = 
        data={}
        offline_threading_id = "0"
        data["client"] = "mercury"
        data["author"] = f"fbid:{100011547033268}"
        #data["timestamp"] = 
        data["source"] = "source:chat:web"
        data["offline_threading_id"] = "0"
        data["message_id"] = "0"
        data["threading_id"] = "100027035268267"
        data["ephemeral_ttl_mode:"] = "0"
        data["message"]=da
        j = session.post(base_url+suburl, data)
        


_do_send_request("Hi there")

soup = find_input_fields(session.get(base_url+login_form_url).text)



data = dict(
            (elem["name"], elem["value"])
            for elem in soup
            if elem.has_attr("value") and elem.has_attr("name")
        )
print(data)




#print(session.get("https://www.facebook.com/messaging/send/").text)
#session.post('https://m.facebook.com/messages/read/?tid=cid.c.100011547033268%3A100055049989323&surface_hierarchy=unknown',data=data)