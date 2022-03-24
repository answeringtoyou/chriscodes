import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#using keyword arguments
#ttk.Label(root, text="Tomorrow is Thursday").pack()

#Using a dictionary index after widget creation
#label = ttk.Label(root)
#label['text'] = "Tomorrow is Thursady"
#label.pack()
#3. Using the config( method with keyword attributes)
label = ttk.Label(root)
label['text'] = "Tomorrow is Thursady"
label.pack()
root.geometry('600x400+50+50')
root.mainloop()