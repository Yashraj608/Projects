import tkinter as tk #This library is used for the Gui purpose in the python#
from time import strftime  #This will give us the time and date#

root = tk.Tk() #This is used to make the initial gui window#
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p \n %D")
    label.config(text = string)
    label.after(1000,time)  #This will show the current time#

label = tk.Label(root,font = ('calibri',50,'bold'), background='Black',foreground='white')
label.pack(anchor='center')

time()
root.mainloop()

