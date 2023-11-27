from PyPDF2 import PdfFileReader
import pytesseract
from PIL import Image

import os
from tkinter import *
from tkinter import filedialog

#screen
# set screen size
window = Tk()
window.geometry("800x500+300+100")
#set size permanently   #or you can use window.resizabld(false, false)
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("Stry")

pytesseract.pytesseract.tesseract_cmd = r'E:\\usb\\tesseract.exe'

def pdf():
        m=filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        f=open(m,'rb')
        l=m.split('\\')
        print(l)

        t=l[-1].split('.')
        p=PdfFileReader(f)
        print(p)
        info=p.getFormTextFields()
        print(info)
        text=open(f'{t[0]}.txt','a+')
        
        text.write(str(p))
        
        text.close()
        lbl=Label(window, text = "PDF CONVERTED", width = 25, font = ("Z003", 40, "bold"))
        lbl.place(x=60, y=400)
def withfolder():
        p=filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        files=os.listdir(p)
        print(files)
        for f in files:
                s=f.split('.')
                print(f)
                img=Image.open(s+"\\"+f)
                r= pytesseract.image_to_string(img)
                text=open(f"{s[0]}.txt","a+")
                text.write(r)
        text.close()

def withfile():
        p=filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        l=p.split('\\')
        print(l)

        t=l[-1].split('.')
        print(t)
        img=Image.open(p)
        
        r=pytesseract.image_to_string(img)
        
        text=open(f'{t[0]}.txt','a+')
        
        text.write(r)
        
        text.close()
        
def qu():
        window.destroy()
'''k=int(input("Press 1 to do with a file\nPress 2 for do with a Folder\nPress 3 for read pdf file\n>>"))
print(type(k))
if k==1:
        p=input("Enter the file Path : ")
        withfile(p)
elif k==2:
        p=input("Enter the folder paht : ")
        withfolder(p)
elif k==3:
        p=input("Enter the path of the pdf folder: ")'''
button1 = Button(window, text = "Image folder2text", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = withfolder)
button1.place(x = 290, y = 340)

button1 = Button(window, text = "Image to text", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = withfile)
button1.place(x = 290, y = 150)

button1 = Button(window, text = "PDF to Word", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = pdf)
button1.place(x = 290, y = 250)
lbl=Label(window, text = "Welcome", width = 25, font = ("arial", 40, "bold"))
lbl.place(x=80, y=400)
lbl1=Label(window, text = "Converter", width = 25, font = ("arial", 40, "bold"))
lbl1.place(x=50, y=70)

window.mainloop()
