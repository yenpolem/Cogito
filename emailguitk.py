from tkinter import *

zee =Tk()
zee.geometry("400x250")
name = Label (zee, text = "NAME").place(x = 30, y = 110)
email = Label (zee, text = "Email").place(x = 30, y = 90)
password = Label (zee,text = "password").place(x = 20, y = 130)

e1 = Entry(zee).place(x = 80, y = 50)
e2 = Entry(zee).place(x = 80, y = 90)
e3 = Entry(zee).place(x = 80, y = 130)
zee.mainloop()
