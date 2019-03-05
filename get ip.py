#writed by moein
from tkinter import *
from socket import *

win = Tk()
win.geometry("170x300")
win.title("get ip")
win.resizable(0,0)
win.configure(background="black")

def ip():

		ip = n.get()
		try:
			l2.configure(text=gethostbyname(ip),fg="green")
		except:
			l2.configure(text="your website adres is false!!",fg="yellow")


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

def color():

		color_ = rad1.get()
		if color_ ==1:
				win.configure(background="red")
				r.configure(bg="red")
				r1.configure(bg="red")
				r2.configure(bg="red")
		elif color_==2:
				win.configure(background="blue")
				r.configure(bg="blue")
				r1.configure(bg="blue")
				r2.configure(bg="blue")
		elif color_==3:
				win.configure(background="yellow")
				r.configure(bg="yellow")
				r1.configure(bg="yellow")
				r2.configure(bg="yellow")

rad1 = IntVar()

l = Label(win , text="select your background ",fg="red",bg="black")
l.grid()


r = Radiobutton(win , text="red",variable=rad1,value=1,command=color)
r.grid()


r1 = Radiobutton(win , text="blue",variable=rad1,value=2,command=color)
r1.grid()


r2 = Radiobutton(win , text="yellow",variable=rad1,value=3,command=color)
r2.grid()




win.mainloop()
#thise is python's power
