from tkinter import *

root = Tk()

# Create label Widget
myLabel = Label(root, text="Hello World")
myLabel2 = Label(root, text="Test 2")

# Show on Screen
myLabel.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)


root.mainloop()