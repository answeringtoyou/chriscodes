from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        #Widget can take all widow
        self.pack(fill=BOTH, expand=1)

        #Create button and link it toclickExitButton()
        EscapeButton = Button(self, text="Escape", command=self.clickedEscapeButton)

        #Location of the button(x,  y)
        EscapeButton.place(x=0, y=0)

    def clickedEscapeButton(self):
        exit()

root = Tk()
app = Window()
root.wm_title("Button Example")
root.geometry("400x200")
root.mainloop()