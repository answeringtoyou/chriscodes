import tkinter as tk

root = tk.Tk()
root.title('Centering the Tkinter window')

window_width = 600
window_height = 400

#Get the screen dimension
screen_width =  root.winfo_screenwidth()
screen_height =  root.winfo_screenheight()

#Finding the centre of the screen
centre_x = int(screen_width/2 - window_width/2)
centre_y = int(screen_width/2 - window_width/2)

#set the position of the 
root.geomtry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')

root.mainloop()