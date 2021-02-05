from tkinter import ttk  
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
root=tk.Tk()
root.geometry("330x250+350+300")
root.resizable(0,0)
root.title('Password Generator')

def weak():
    a = ['1','2','3','4','5','6','7','8','9','0']
    b = random.choice(a)
    c =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z']
    d = random.choice(c)
    e = str(b)+str(d)
    f = random.choice(a)+random.choice(c)
    g = random.choice(a)+random.choice(c)
    h = random.choice(a)+random.choice(c)
    i = e+f+g+h
    lab.config(text=i)
def strong():
    global lab,k
    a = ['1','2','3','4','5','6','7','8','9','0']
    b = random.choice(a)
    c =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z']
    d = random.choice(c)
    e = ['!','#','@','$']
    f = random.choice(e)
    g =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N',
        'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
    h = random.choice(g)
    i= str(b)+str(d)+str(f)+str(h)
    j= random.choice(a)+random.choice(c)+random.choice(e)+random.choice(g)
    k=i+j
    
    lab.config(text=k)

lab1 =Label(root,text="Password Generator",bg="grey",fg="orange",font=("bold",18),width=50,height=2)
lab1.pack()
lab2 = Label(root, 
        text="Select a Password Type:",bg="grey",font=("bold"),width=50,height=1,
        justify = LEFT,)
lab2.pack(pady=10)

bt  =Frame(root)
bt.pack(pady=10)
btn = Button(bt,text="weak Password",command=weak)
btn.pack(side=LEFT)
btn = Button(bt,text="Strong Password",command=strong)
btn.pack(padx=10,pady=10)

lab = Label(root,text="see your password here.",bg="grey",font=('bold',18),width=50,height=15)
lab.pack(pady=0)
root.mainloop()
