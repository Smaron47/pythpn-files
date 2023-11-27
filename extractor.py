import os
import xlsxwriter

p=os.getcwd()
workbook=xlsxwriter.Workbook(f"{p}\\list.xlsx")
worksheet=workbook.add_worksheet('linked2')
row=1
col=1
file=open("C:\\Users\\Manik Chandra Biswas\\Desktop\\namelist.txt","r")
print(file)
for i in file.readlines():
    e=i.split("-")
    print(e)
    worksheet.write(row,col,e[0])
    worksheet.write(row,col+1,e[1])
    worksheet.write(row,col+2,e[2])
    row=row+1
workbook.close()

'''
from zipfile import ZipFile
from tkinter import *
import os
from tkinter import filedialog
p=os.getcwd()
print(os.getcwd())
print(os.getcwdb())
print(os.path.dirname(p))
out=os.path.dirname(p)


root = Tk()

root.geometry('400x250')
root.maxsize(400,250)

def browse():
    p=filedialog.askopenfilename(title = "Select file",filetypes = (("Zip File",".zip")))
    fpa.set(p)
    

labal=Label(root,text="Zip File", fg = "gray", font = ("new times roman",  16, "bold"), bg="black")
labal.place(x=0,y=50)
fpa = StringVar()
fpa.get()
textBox1 = Entry(root, text="hi", textvar = fpa, width = 30, font = ("arial", 11, "bold"))
textBox1.place(x = 90, y = 50)
def dwn():
    pat=fpa.get()
    print(type(pat))
    print(pat)
    print(out)
    z=ZipFile(pat,mode='r')
    z.printdir()
    z.extractall(out)
    z.close()
    labal2=Label(root,text="Done")
    labal2.place(x=100,y=90)
button=Button(root, text = "   Extract  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = dwn)
button.pack(anchor="center")
b1=Button(root, text = "Browse", fg = "black", bg = "white", relief = "raised", font = ("arial", 11, "bold"), command = browse)
b1.place(x = 305, y = 50)



root.mainloop()
'''