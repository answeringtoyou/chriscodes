import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text="Today is Wednesday").pack()
ttk.Label(root, text="Today is Thursday").pack()

root.geometry('600x400+50+50')
root.mainloop()