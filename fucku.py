import re
import requests
from bs4 import BeautifulSoup
import json
#import facebook
import fbchat


'''
ffline_threading_id = _util.generateOfflineThreadingID()
        data["client"] = "mercury"
        data["author"] = "fbid:{}".format(self.user_id)
        data["timestamp"] = _util.now()
        data["source"] = "source:chat:web"
        data["offline_threading_id"] = offline_threading_id
        data["message_id"] = offline_threading_id
        data["threading_id"] = _util.generateMessageID(self._client_id)
        data["ephemeral_ttl_mode:"] = "0"
'''

Data={'client':'mercury','author':'fbid:{100011547033268}','timestamp':'','threading_id':'100045999454076','message':'hi urmi'}
e=requests.Session()

login_form_url = '/login/device-based/regular/login/?refsrc=https%3A'\
        '%2F%2Fmobile.facebook.com%2Flogin%2Fdevice-based%2Fedit-user%2F&lwv=100'

params = {'email':"01772803606", 'pass':"Try to hack $m@r(*)n"}
base_url='https://mobile.facebook.com'

logged_request = e.post(base_url+login_form_url, data=params)
print("Loged in ")
'''tp="/messaging/send/"
'''
tp=input("Enter the Url : ")
req=e.get(tp)

bef=BeautifulSoup(req.text)
pa=["Like","React","Reply","More"]
#p=bef.find_all("input")
##inp=bef.find_all("textarea")
#rep=str(req).replace('<textarea class="ch ci cj ck" cols="15" id="composerInput" name="body" rows="2"></textarea>','<textarea class="ch ci cj ck" cols="15" id="composerInput" name="body" rows="2">Hi there</textarea>')
#mmr=BeautifulSoup(rep)
##ss=e.post("https://mobile.facebook.com/messages/read/?fbid=100011547033268&entrypoint=profile_message_button&_rdr",data=mmr.encode())


for i in bef.find_all("a"):
    #print(i.text)
    if "profile.php?" in i["href"]:
        print(i["href"])
        print(i.text)
        print(re.findall('\d+',i["href"])[0])




'''#msg=input("Enter the message: ")
mg={"threading_id":100045999454076,"message":"Hi there"}
import fbchat

cli=fbchat.Client(params["email"],params["pass"])
cli.send("hi there","100011547033268")
print("Message sent")'''
'''
print(req[req.find("Nur")-100:req.find("Nur")+100])

t="/profile.php?id=100025305635145&refid=18&__tn__=C-R"
'''
