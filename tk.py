from tkinter import *

#basic container -- imagine everything as widget
root = Tk()

#2 steps always:
#define the thing to create
#put it up on the screen

#creating a label widget
theLabel = Label(root, text="Hello World")

#putting it at first available spot
theLabel.pack()

#create an event loop
root.mainloop()