from tkinter import *
import cv2 as cv

root = Tk()

e = Entry(root, width=50)
e.pack()


def openCamera():
    cam_port = 1
    cam = cv.VideoCapture(cam_port)
    while True:

        result, frame = cam.read()

        if result:

            cv.imshow('frame', frame)

            cv.waitKey(0)

            cam.release()


myButton = Button(root, text="Click For Photo", padx=10, pady=10, activebackground="Blue", command=openCamera,
                  fg="white", bg="black")
myButton.pack()

root.mainloop()
