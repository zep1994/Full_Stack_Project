from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name")

def myClick():
    hello = "Hello, " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", padx=50, pady=50, activebackground="Blue", command=myClick, fg="white", bg="black")  # state=DISABLED
myButton.pack()

root.mainloop()
