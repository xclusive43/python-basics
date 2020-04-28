from tkinter import *
root = Tk()
root.title("app")

e = Entry(root, width=100 )

#e.insert(0, "enter your name")
my = Button(root, text="click")

my.pack()
e.pack()

root.mainloop()

