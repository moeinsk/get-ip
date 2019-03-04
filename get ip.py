#writed by moein
from tkinter import *
from socket import *

win = Tk()
win.geometry("155x120")
win.title("get ip")
win.resizable(0,0)
win.configure(background="black")

def ip():

		ip = n.get()
		try:
			l2.configure(text=gethostbyname(ip),fg="green")
		except:
			l2.configure(text="name website is false",fg="yellow")


l = Label(win , text="writed by moein",fg="yellow",bg="black")
l.grid()

l = Label(win , text="enter website:",fg="red",bg="black")
l.grid()

n = StringVar()
e = Entry(win , width=20,textvariable=n)
e.grid()

b = Button(win , text="Check",bg="orange",command=ip)
b.grid()

l2 = Label(win , text="",fg="green",bg="black")
l2.grid()



win.mainloop()
#thise is python's power
