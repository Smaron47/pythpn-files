'''import itertools


for i in range(4,10):
    for k in itertools.permutations("11111111222222223333333344444444555555556666666677777777888888889999999900000000",i):
        
        k=str(k)
        k=k.replace("'","")
        k=k.replace("(","")
        k=k.replace(")","")
        k=k.replace(",","")
        k=k.replace(" ","")
        print(k)
        
        f=open("passlist.txt","wb")
        f.write(k)
from itertools import permutations as p
from hashlib import sha1
def co(tup): 

    str =  ''.join(tup) 

    return str
s='11111111222222223333333344444444555555556666666677777777888888889999999900000000'

for i in range(1,len(s)+1):
	k=list(p(s,i))
	t=0
	while (t<len(k)):
		result = sha1(co(k[t]).encode())
		print(co(k[t]))
		t=t+i'''
import playsound

playsound.playsound("rocku.mp4")