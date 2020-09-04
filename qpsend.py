from tkinter import *
import random

window=Tk()
window.title("Question paper Setter")
window.geometry("850x600+0+0")
window.config(bg="#9B59B6")
frame1=LabelFrame(window,text="number of students",padx=60,pady=10,bg="#9B59B6")
frame1.grid(row=0,column=0,padx=5,pady=10)

frame2=LabelFrame(window,text="Mail id of students",padx=5,pady=10,bg="#9B59B6")
frame2.grid(row=0,column=1,padx=5,pady=10)

window.mainloop()