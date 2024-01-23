from tkinter import *

vos = Tk()
vos.geometry("400x400")

zf = Canvas(vos, bg="Pink", height="4000")
arc = zf.create_arc((5,10,90,250),start = 0 ,extent = 90, fill="RED")
zf.pack()
vos.mainloop()
