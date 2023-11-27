'''import pandas as pd
from email_validator import validate_email, EmailNotValidError
import smtplib

server = smtplib.SMTP()
server.connect()
server.set_debuglevel(True)


def eml(em):
    email = em

    try:
    # Validate.
        valid = validate_email(email)

        # Update with the normalized form.
        email = valid.email
        server.verify(email)
        print(f"{email} is valid .... ")
    except EmailNotValidError as e:
    # email is not valid, exception message is human-readable
        print(str(e))

p=input("Enter The Path of File => ")

p=p.replace("'","").replace(" ","")
ou=pd.read_csv(p)
of=ou["email_first"].tolist()

ofe=ou["email_second"].tolist()
#print(ou["email_first"])
for i in of:
    eml(str(i))
for i in ofe:
    eml(str(i))
'''

'''import re

addressToVerify ='info@scottbrady91.com'
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

if match == None:
	print('Bad Syntax')
	raise ValueError('Bad Syntax')

import dns.resolver

records = dns.resolver.query('scottbrady91.com', 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)


import socket
import smtplib

# Get local server hostname
host = socket.gethostname()

# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(host)
server.mail('me@domain.com')
code, message = server.rcpt(str(addressToVerify))
server.quit()

# Assume 250 as Success
if code == 250:
	print('Success')
else:
	print('Bad')'''

text=int(input("Enter the number of text: "))
min=int(input("Enter the number of min: ")) 
text_cost=0 
min_cost=0
if text>250: 
    text_cost=(text-250)*7 
if min>75:
    min_cost=(min-75)*12
total= text_cost+min_cost
print((total+1000),"p")