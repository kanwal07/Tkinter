from tkinter import *

root = Tk()

def btnClick():
    theLabel = Label(root, text="You clicked the button").pack()


theButton = Button(root, text="Click Me!", command=btnClick, fg="white", bg="#000000").pack()

root.mainloop()