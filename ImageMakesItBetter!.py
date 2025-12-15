from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title("Image Example")
root.geometry("480x480")

upload=Image.open("spiderman.jpg")
image=ImageTk.PhotoImage(upload)

label=Label(root,image=image,height=350,width=300)
label.place(x=50,y=0)

label2=Label(root,text="This is how you add an image in Tkinter window")
label2.place(x=40,y=360)

root.mainloop()