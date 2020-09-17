from tkinter import *

root = Tk()

#normal button
theButton1 = Button(root, text="Click Me!").grid(row=0, column=0)

#disabled button
theButton2 = Button(root, text="Click me also", state="disabled").grid(row=1, column=0)

#change size of button
theButton3 = Button(root, text="I'm a longer button", padx=50).grid(row=1, column=1)
theButton4 = Button(root, text="I'm a taller button", pady=50).grid(row=2, column=0)
theButton5 = Button(root, text="I'm a square button", padx=50, pady=50).grid(row=2, column=2)

root.mainloop()

