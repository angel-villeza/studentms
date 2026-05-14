from tkinter import *

#Login Page
root = Tk()
root.title("Login Page")
root.geometry("350x250")
root.resizable(False, False)

Label(root, text="Login Form", font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Username").pack(pady=5)
entry_login_uname = Entry(root, width=30)
entry_login_uname.pack()

Label(root, text="Password").pack(pady=5)
entry_login_pass = Entry(root, width=30, show="*")
entry_login_pass.pack()

Button(root, text="Login", width=15, bg="green", fg="white", command="").pack(pady=10)
Button(root, text="Register", width=15, bg="blue", fg="white", command="").pack()

root.mainloop()