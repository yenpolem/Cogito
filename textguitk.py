from tkinter import *
parent = Tk ()
name = Label (parent, text = "name").grid (row = 0, column = 0)
e1 = Entry (parent).grid (row = 0, column = 1)
password = Label(parent).grid (row =1, column = 1)
submit = Button (parent, text = "submit").grid (row = 4, column = 0)
parent.mainloop()
