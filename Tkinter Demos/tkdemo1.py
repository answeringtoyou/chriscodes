from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

#Code ti initialize the tkinter
root =Tk()
app = Window(root)

#Add the window title
root.wm_title("Digikids Application")

#To show the window and retain it on the screen 
root.mainloop()