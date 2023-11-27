'''import os
import datetime
from time import sleep

from tkinter import * 
#from tkinter.ttk import *
  
# importing strftime function to
# retrieve system's time
from time import strftime

d=datetime.datetime.today().date()
dt= datetime.datetime.today().strftime("%A")

# creating tkinter window
print(d)
window = Tk()
window.geometry("300x200")
#set size permanently   #or you can use window.resizabld(false, false)
window.minsize(1000, 200)
window.maxsize(1000, 300)
window.title("ALARM")
#window.iconbitmap("E:\\downloads\\icon.ico")


# This function is used to 
# display time on the label
def time():
    string = strftime(' %I:%M:%S %p ')
    lbl.config(text = string)

    lbl.after(1000, time)
# Styling the label widget so that clock
# will look more attractive
lbl = Label(window, font = ('Z003', 120, 'bold'),
            background = 'black',
            foreground = 'lightblue')
  
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')

lbl2= Label(window, font = ('Z003', 30, 'bold'),
            background = 'black',
            foreground = 'red')
lbl2.place(x=370,y=120)
lbl3= Label(window, font = ('Z003', 25, 'bold'),
            background = 'black',
            foreground = 'lightgreen')
lbl3.place(x=100,y=120)
def dat():
	lbl3.config(text=f"{dt}")	
	lbl2.config(text=f"---{d}---")
	



time()
dat()

def login():
	
	alh= userName.get()
	alm= password.get()
	time()
	while True:
		sleep(60)
		hour = int(datetime.datetime.now().hour)
		min = int(datetime.datetime.now().minute)
		
		if hour==int(alh) and min==int(alm):
			os.system("shutdown -p")

label1 = Label(window, text = " Alarm ", fg = "blue", font = ("new times roman", 25, "bold"), bg="red")
label1.place(x = 120, y = 300)

label2 = Label(window, text = "HOUR :", font = ("arial", 16, "bold"))
label2.place(x = 0, y = 110)

userName = StringVar()
textBox1 = Entry(window, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 150, y = 110)

label3 = Label(window, text = "MINUTE :", font = ("arial", 16, "bold"))
label3.place(x = 0, y = 150)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 150, y = 150)

button1 = Button(window, text = "   SET ALARM   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 0, y = 210)'''



'''
hour = int(datetime.datetime.now().hour)
print(hour)
alh= input("Enter the time of hour:>")
alm= input("enter the time if min:>")
while True:
	time.sleep(60)
	hour = int(datetime.datetime.now().hour)
	min = int(datetime.datetime.now().minute)
	
	if hour==int(alh) and min==int(alm):
		os.system("shutdown -p")

'''
