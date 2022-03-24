#Tkinter entry widget example
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#Create the root window
root = tk.Tk()
root.geometry("600x400+50+50")
root.resizable(False, False)
root.title("Digikids Applicayion: Sign In")

#Store the email and the paasword
email = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    """
    Callback when the login button is clicked
    """
    msg = f'You entered email: {email()} and password:{password.get()}'
    showinfo(
        title = 'Information',
        message = msg
    )

    #The sign in Frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand = True)

    #The email label widget
email_label = ttk.Label(signin, text= "Email Address: ")
email_label.pack(fill = 'x' , expand = True)

email_entry = ttk.Entry(signin, textvariable = email)
email_entry.pack(fill= 'x', expand = True)
email_entry.focus()

    #The password label widget
password_label = ttk.Label(signin, text="password: ")
password_label.pack(fill = 'x', expand = True)

password_label = ttk.Entry(signin, textvariable = password, show="*")
password_label.pack(fill = 'x', expand = True)

    #Create login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill="x", expand = True, pady = 10)

root.mainloop()