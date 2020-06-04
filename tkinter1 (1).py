from tkinter import *
from playsound import playsound
from PIL import ImageTk, Image
import os
def onclick():
    playsound("Sound.mp3")
    root.destroy()
    os.system('python tkinter2.py')
    

root = Tk()
root.title('Rock Paper Scissors Game')
width=600
height=400
s_width=root.winfo_screenwidth()
s_height=root.winfo_screenheight()
x_cood=(s_width/2)-(width/2)
y_cood=(s_height/2)-(height/2)
root.geometry("%dx%d+%d+%d"%(width,height,x_cood,y_cood))
root.resizable(width=False,height=False)
canvas=Canvas(root,width=600,height=400)
canvas.pack()
image=ImageTk.PhotoImage(Image.open("canvas1.png"))
canvas.create_image(0,0,anchor=NW,image=image)
b=Button(root,text="PLAY",command=onclick)
img = PhotoImage(file="button_play.png") 
b.config(image=img)
b.pack()
b.place(x=240,y=305)
root.mainloop()
