from tkinter import *
dd = Tk()

dd.title("class")
e = Entry(dd, width=100 )




class ajay:
    x = 3
    y = "MY name is python...."


obj1 = ajay()

print(obj1.x)
print(obj1.y)
my = Button(dd, text=obj1.y)
 
my.pack()
e.pack()
dd.mainloop()
