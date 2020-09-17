from tkinter import *

root = Tk()

#normal way of doing things*****
theLabel1 = Label(root, text="Hello World!")
theLabel2 = Label(root, text="My name is Kanwal")

#imagine a matrix(grid) and give row and column number
theLabel1.grid(row=0, column=0)
theLabel2.grid(row=1, column=1)

#object oriented way of doing things
theLabel3 = Label(root, text="Hello World of oops!").grid(row=2, column=0)
theLabel4 = Label(root, text="object oriented programming").grid(row=3, column=1)

#the rows and columns are relative to each other

root.mainloop()