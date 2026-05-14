from tkinter import *
from tkinter import messagebox

#Registration Page
def open_register_window():
    reg_win = Toplevel(root) 
    reg_win.geometry("400x350")
    reg_win.title("Registration Page")
    reg_win.resizable(False, False)
    reg_win.grab_set()

    Label(reg_win, text="Registration Form", font=("Arial", 16, "bold")).pack(pady=10)

    Label(reg_win, text="Username").pack(pady=5)
    entry_reg_uname = Entry(reg_win, width=30)
    entry_reg_uname.pack()

    Label(reg_win, text="Email").pack(pady=5)
    entry_reg_email = Entry(reg_win, width=30)
    entry_reg_email.pack()
     
    Label(reg_win, text="Password").pack(pady=5)
    entry_reg_pass = Entry(reg_win, width=30, show="*")
    entry_reg_pass.pack()

    Label(reg_win, text="Confirm Password").pack(pady=5)
    entry_reg_cpass = Entry(reg_win, width=30, show="*")
    entry_reg_cpass.pack()

    def register():
        uname = entry_reg_uname.get()
        email = entry_reg_email.get()
        password = entry_reg_pass.get()
        cpass = entry_reg_cpass.get()

        if uname == "" or email == "" or password == "" or cpass == "":
            messagebox.showerror("Error","All fields are required.")
            return
       
        if password != cpass:
            messagebox.showerror("Error","Password do not matched.")
            return
       
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    saved_email = line.strip().split(", ")[1]
                    if email == saved_email:
                        messagebox.showerror("Error","Email already used.")
                        return
        except FileNotFoundError:
            pass

        with open("users.txt", "a") as file:
            file.write(f"{uname}, {email}, {password}\n")
        messagebox.showinfo("Success","Registration Successful!")
        reg_win.destroy()

    Button(reg_win, text="Register", width=15, bg="blue", fg="white", command=register).pack(pady=20)

#log in function
def login():
    uname = entry_login_uname.get()
    password = entry_login_pass.get()

    if uname == "" or password == "":
        messagebox.showerror("Error","All fields are required")
        return
   
    try:
        with open("users.txt") as file:
            for line in file:
                saved_uname = line.strip().split(", ")[0]
                saved_pass = line.strip().split(", ")[2]

                if uname == saved_uname and password == saved_pass:
                    messagebox.showinfo("Success", "Login Successful!")
                    #open_home_window(uname)
                    return
            messagebox.showerror("Error", "Invalid Username or Password")
    except FileNotFoundError:
        messagebox.showerror("Error", "No registered users found.")

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

Button(root, text="Login", width=15, bg="green", fg="white", command=login).pack(pady=10)
Button(root, text="Register", width=15, bg="pink", fg="white", command=open_register_window).pack()

root.mainloop()
