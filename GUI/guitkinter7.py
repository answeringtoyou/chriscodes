import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def button_clicked():
    print('You have clicked the button')

button = ttk.Button(root, text='Please click here', command=button_clicked)
button.pack()

root.geometry('600x400+50+50')
root.mainloop()