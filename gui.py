import tkinter as tk
from tkinter import *
import numpy as np
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('My Income Predictor')
arr1 = [0]

x = tk.IntVar()


def submit():
    num1 = x.get()
    global arr1
    arr1 = np.append(arr1, num1)
    tk.Label(root, text="Record submitted sucessfully", bg="green", fg='white').grid(row=7, column=2)
    print(arr1)
    return arr1
labelDay = tk.Label(root, text="Days").grid(row=1, column=0)
plotbtn=Button(root, text="Click here for plot pridiction", bg="red", fg='white').grid(row=11, column=0)

btn = Button(root, text="Submit Record", bg="green", fg='white', command=submit).grid(row=3, column=0)
entry1 = tk.Entry(root, textvariable=x).grid(row=1, column=2)




def close_window ():
    root.destroy()

button = Button ( text = "Quit!",bg="red",fg='white' ,command = close_window).grid(row=16,column=0)
root.mainloop()

