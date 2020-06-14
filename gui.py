import tkinter as tk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('My Income Predictor')
arr1 = [0]
arr2 = [0]
x = tk.IntVar()
y = tk.IntVar()


def submit():
    num1 = x.get()
    num2 = y.get()
    global arr1
    global arr2
    arr1 = np.append(arr1, num1)
    arr2 = np.append(arr2, num2)
    tk.Label(root, text="Record submitted sucessfully", bg="green", fg='white').grid(row=7, column=2)
    print(arr1)
    print(arr2)
    return arr1, arr2
labelDay = tk.Label(root, text="Days").grid(row=1, column=0)
labelincome = tk.Label(root, text = 'Income').grid(row = 2, column= 0)

def getplt():
    slope, intercept, r, p, std_err = stats.linregress(arr1, arr2)
    def myfunc(arr1):
        return slope * arr1 + intercept

    mymodel = list(map(myfunc, arr1))

    plt.scatter(arr1, arr2)
    plt.plot(arr1, mymodel)
    plt.xlabel('Days')
    plt.ylabel('Income')
    plt.show()
plotbtn=Button(root, text="Click here for plot pridiction", bg="red", fg='white', command = getplt).grid(row=11, column=0)

btn = Button(root, text="Submit Record", bg="green", fg='white', command=submit).grid(row=3, column=0)
entry1 = tk.Entry(root, textvariable=x).grid(row=1, column=2)
entry2 = tk.Entry(root, textvariable=y).grid(row=2, column=2)

def close_window ():
    root.destroy()

button = Button ( text = "Quit!",bg="red",fg='white' ,command = close_window).grid(row=16,column=0)
root.mainloop()

