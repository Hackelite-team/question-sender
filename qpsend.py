from tkinter import *
import random

window=Tk()
window.title("Question paper Setter")
window.geometry("865x620+0+0")
window.config(bg="#9B59B6")
frame1=LabelFrame(window,text="number of students",padx=60,pady=10,bg="#9B59B6")
frame1.grid(row=0,column=0,padx=5,pady=10)

frame2=LabelFrame(window,text="Mail id of students",padx=5,pady=10,bg="#9B59B6")
frame2.grid(row=0,column=1,padx=5,pady=10)

frame3=LabelFrame(window,text="Selection",padx=5,pady=10,bg="#9B59B6")
frame3.grid(row=1,column=1,padx=5,pady=10)

frame4=LabelFrame(window,text="TEACHER'S MAIL",padx=10,pady=10,bg="#9B59B6")
frame4.grid(row=1,column=0,padx=5,pady=10)

def fun():
    global a,but1
    a=int(e1.get())
    b1.config(state=DISABLED,bg="black",fg="white")
    but1.config(state=ACTIVE,bg="white",fg="black")
    

l1=Label(frame1,text="Enter Number of students : ",font=(" Verdana",12,"bold italic"),bg="#9B59B6")
e1=Entry(frame1,width=50,borderwidth=7)
b1=Button(frame1,text="submit",command=fun,state=ACTIVE,bg="white",fg="black")
l1.grid(row=0,column=0,pady=10)
e1.grid(row=1,column=0,pady=10)
b1.grid(row=2,column=0,pady=10)

global count,l,lab1,but1

l=[]


def enter():
    global count,l,but1
    l.append(enty1.get())
    enty1.delete(0,END)
    count+=1
    if count<=a:
        lab1.config(text=f"Please Enter the mail id of student {count}",font=("Verdana",12,"bold italic"),bg="#9B59B6")
    if count>a:
        but1.config(state=DISABLED,bg="black",fg="white")
   
count=1
lab1=Label(frame2,text="Please Enter the mail ID of student 1",font=("Verdana",12,"bold italic"),bg="#9B59B6")
enty1=Entry(frame2,width=60,borderwidth=7)
but1=Button(frame2,text="Submit",command=enter,state=DISABLED,bg="black",fg="white")
lab1.grid(row=0,column=0,pady=10)
enty1.grid(row=1,column=0,pady=10)
but1.grid(row=2,column=0,pady=10)


window.mainloop()