import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
import vimeapi
import pyperclip as clipboard
from tkinter import ttk

api = vimeapi.VimeApi("DFBS0Qnl34Z10tA6OTegx0a4zIhTmB7")

def what():
    result = showinfo("Что?","Для того чтобы получить api введите команду /api dev")

def getstaff():
    result = showinfo("Персонал",api.online_staff())


window = Tk()
window.title("vimetop")
window.geometry('450x300')
#txt = Entry(window, width=35)
#txt.grid(column=1, row=1)
btn = ttk.Button(window, text='?', command=what, cursor="hand2")
btn.grid(column=2, row=1)
btn1 = ttk.Button(window, text='персонал онлайн', command=getstaff, cursor="hand2")
btn1.grid(column=2, row=1)
#btn1 = ttk.Button(window, text='получить статистику', command=getinfo, cursor="hand2")
#btn1.grid(column=2, row=1)


window.mainloop()
