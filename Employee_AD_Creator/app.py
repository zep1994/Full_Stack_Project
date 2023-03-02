from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look, It turns Blue")
    myLabel.pack()


myButton = Button(root, text="Click Me", padx=50, pady=50, activebackground="Blue", command=myClick)  # state=DISABLED
myButton.pack()

root.mainloop()
