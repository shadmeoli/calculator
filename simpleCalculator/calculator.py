import math
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk

calc = tk.Tk()
calc.title("simple math")
calc.geometry('300x400')
calc.resizable(False, False)

#functionality of the numbers
def numberRows():
    print("NUmbers")

# tree view style
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold'))
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
tree=ttk.Treeview(calc,style="mystyle.Treeview")

#display window
numDisp = ttk.Treeview(calc, height=6)
numDisp.place(x=1, y=1)
#first number row
numb1 = Button(calc, text = '1', width=3, height=2, command=numberRows)
numb1.place(x=1, y=150)
numb2 = Button(calc, text = '2', width=3, height=2, command=numberRows)
numb2.place(x=55, y=150)
numb3 = Button(calc, text = '3', width=3, height=2, command=numberRows)
numb3.place(x=110, y=150)

#second number row
numb4 = Button(calc, text = '4', width=3, height=2, command=numberRows)
numb4.place(x=1, y=200)
numb5 = Button(calc, text = '5', width=3, height=2, command=numberRows)
numb5.place(x=55, y=200)
numb6 = Button(calc, text = '6', width=3, height=2, command=numberRows)
numb6.place(x=110, y=200)

#last number row
numb7 = Button(calc, text = '7', width=3, height=2, command=numberRows)
numb7.place(x=1, y=250)
numb8 = Button(calc, text = '8', width=3, height=2, command=numberRows)
numb8.place(x=55, y=250)
numb9 = Button(calc, text = '9', width=3, height=2, command=numberRows)
numb9.place(x=110, y=250)

#float button
floatButton = Button(calc, text = '00', width=10, height=2, command=math)
floatButton.place(x=1, y=300)

#percentage
percentage = Button(calc, text = '%', width=3, height=2, command=math)
percentage.place(x=110, y=300)

#addition
add = Button(calc, text = '+', width=13, height=2, command=math)
add.place(x=165, y=150)
#subtraction
sub = Button(calc, text = '-', width=13, height=2, command=math)
sub.place(x=165, y=200)
#division
div = Button(calc, text = '/', width=13, height=2, command=math)
div.place(x=165, y=250)
#multiplication
multi = Button(calc, text = 'x', width=13, height=2, command=math)
multi.place(x=165, y=300)

#equlas
answer = Button(calc, text = 'ans' , width=30, height=2, command=math)
answer.place(x=15, y=350)

calc.mainloop()
