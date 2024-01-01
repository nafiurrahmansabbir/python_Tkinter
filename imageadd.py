from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("1200x1900")
num=Label(text="Nafiur Rahman\nThis is my pixture!")
num.pack()
# Tkinter
# photo = PhotoImage(file="1.png")
# img1=Label(image=photo)
# img1.pack()

# using PIL image add
image=Image.open("sabbir.jpg")
photo=ImageTk.PhotoImage(image)
img2=Label(image=photo)
img2.pack()

root.mainloop()