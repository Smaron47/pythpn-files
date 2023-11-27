'''from tkinter import *
from tkinter import messagebox

def passwordCheck():
    try:
        
                if usernameEntry.get() == "Smaron" and passwordEntry.get() == "Babu khaicho":
                    messagebox.showinfo('SUCCESS', 'LOGGED IN!') #creates a message box
                    exit()
                else:
                    messagebox.showerror('ERROR', 'INCORRECT LOGIN!') #Creates an error message
                    exit()

    except FileNotFoundError:
        messagebox.showerror('ERROR', 'USERS.TXT WAS NOT FOUND') #Creates an error message
        exit()

root = Tk()

usernameLabel = Label(root, text = 'USERNAME:') #Creates a label in the GUI
usernameLabel.grid(column = 0, row = 0) #Puts the previously created label in column 0, row 0
usernameEntry = Entry(root) #Creates an input box in the GUI
usernameEntry.grid(column = 1, row = 0) #Puts the previously created entry box in column 1, row 0

passwordLabel = Label(root, text = 'PASSWORD:')
passwordLabel.grid(column = 0, row = 1)
passwordEntry = Entry(root)
passwordEntry.grid(column = 1, row = 1)

submitButton = Button(root, text = 'SUBMIT', command = passwordCheck) #Creates a button that says 'SUBMIT' and when clicked it runs the function passwordCheck()
submitButton.grid(column = 2, row = 1) #Puts the button into column 2, row 1

root.mainloop() #Runs the actual GUI'''
'''from tkinter import *
#from PIL import Image,ImageTk
from time import sleep

#--------------------------------------------------------------------------------------------------------------
#create the window and add size and title to it
window = Tk()
window.geometry("800x500+300+100")
#set size permanently   #or you can use window.resizabld(false, false)
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("Stry")
#window.iconbitmap("C:\Python\Python Projects\TKINTER/login Sys/lock_v2W_icon.ico")
window1 = Tk()
window1.geometry("800x500+300+100")
#set size permanently   #or you can use window.resizabld(false, false)
window1.minsize(800, 500)
window1.maxsize(800, 500)
window1.title("Stry")
#---------------------------------------------------------------------------------------------------------------
#first get the picture then save it in pic and set as background
image = Image.open("shot.jpg")
pic = ImageTk.PhotoImage(image)
#build pic and add it to window
label0 = Label(image = pic)
label0.pack(fill = BOTH, expand = 'yes')
lbl=Label(window1, text = ("It is working"),width = 25, font = ("arial", 40, "bold"))
lbl.place(x=0,y=410)
#-------------------------------------------------------------------------------------------------------------
#functions for the buttons to perform
def login():
    users = {'admin': '1000', 'dev': '2000', 'client': '3000', 'employee': '4000'}
    username = userName.get()
    Pass = password.get()
    if username in users :
        if (users[username] == Pass):
            label4 = Label(window, text = ("Welcome " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)

            sleep(4)
            window.destroy()
            window1.mainloop()
            
            
        else:
            label4 = Label(window, text = ("Incorrect Password for " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)

    else:
        label4 = Label(window, text = (username + " does not exist"),width = 25, font = ("arial", 40, "bold"))
        label4.place(x = 0, y = 400)

#----------------------------------------------------------------------------------------------------------------
#first lable
label1 = Label(window, text = " Login System ", fg = "black", font = ("new times roman", 40, "bold"))
label1.place(x = 200, y = 15)

label2 = Label(window, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(window, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 290, y = 250)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 335, y = 340)

#display window
window.mainloop()

li = {"a":"/home/smaron/Downloads/man/A.wav",
"b":"/home/smaron/Downloads/man/B.wav",
"v":"/home/smaron/Downloads/man/Bb.wav",
"c":"/home/smaron/Downloads/man/C.wav",
"k":"/home/smaron/Downloads/man/C1.wav",
"x":"/home/smaron/Downloads/man/C_s.wav",
"l":"/home/smaron/Downloads/man/C_s1.wav",
"d":"/home/smaron/Downloads/man/D.wav",
"j":"/home/smaron/Downloads/man/D1.wav",
"w":"/home/smaron/Downloads/man/D_s.wav",
"p":"/home/smaron/Downloads/man/D_s1.wav",
"e":"/home/smaron/Downloads/man/E.wav",
"i":"/home/smaron/Downloads/man/E1.wav",
"f":"/home/smaron/Downloads/man/F.wav",
"u":"/home/smaron/Downloads/man/F.wav",
"r":"/home/smaron/Downloads/man/F_s.wav",
"g":"/home/smaron/Downloads/man/G.wav",
"n":"/home/smaron/Downloads/man/G_s.wav"}
print(li['a'])'''
from tkinter import filedialog
p=filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
print(p)
    