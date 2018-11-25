import tkinter as tk
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mydatabase"
)

mycursor = mydb.cursor()

LARGE_FONT = ("Verdana", 11)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


def create_submit(e1, e2, e3, e4, e5, e6)-> None:

    user = {"Name": e1.get(), "Surname": e2.get(), "Nickname": e3.get(), "Password": e4.get(),
            "Email": e5.get(), "Country": e6.get()}

    values = (user["Name"], user["Surname"], user["Nickname"], user["Password"], user["Email"], user["Country"])

    sql_insert = "INSERT INTO users (name, surname, nickname, password," \
                 " email, country) VALUES (%s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql_insert, values)
    mydb.commit()


def delete_submit(e1, e2):

    values = (e1.get(), e2.get())

    mycursor.execute("DELETE FROM users WHERE nickname = %s \
         AND password = %s", values)
    mydb.commit()


def popupmsg(msg):

    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    button1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    button1.pack()
    popup.mainloop()

class ShelfApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        #tk.Tk.iconbitmap(self, default="logo.icon") to be updated
        tk.Tk.wm_title(self, "ShelfApp")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, CreateAccountPage, UpdateEmailPage,
                  ChangePasswordPage, LogInPage, DeleteAccountPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Let's get started and make out life easier",
                      font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        button1 = ttk.Button(self, text="Create an account",
                         command=lambda: controller.show_frame(CreateAccountPage))
        button2 = ttk.Button(self, text="Update your email",
                         command=lambda: controller.show_frame(UpdateEmailPage))
        button3 = ttk.Button(self, text="Change your password",
                         command=lambda: controller.show_frame(ChangePasswordPage))
        button4 = ttk.Button(self, text="Log in",
                         command=lambda: controller.show_frame(LogInPage))
        button5 = ttk.Button(self, text="Delete an account",
                         command=lambda: controller.show_frame(DeleteAccountPage))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()


class CreateAccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_1 = tk.Label(self, text="Name")
        label_2 = tk.Label(self, text="Surname")
        label_3 = tk.Label(self, text="Login")
        label_4 = tk.Label(self, text="Password")
        label_5 = tk.Label(self, text="Email")
        label_6 = tk.Label(self, text="Country")

        entry_1 = tk.Entry(self, cursor="arrow")
        entry_2 = tk.Entry(self, cursor="man")
        entry_3 = tk.Entry(self, cursor="spider")
        entry_4 = tk.Entry(self, cursor="target", show="*")
        entry_5 = tk.Entry(self, cursor="star")
        entry_6 = tk.Entry(self, cursor="heart")

        label_1.grid(row=0, sticky="e")
        label_2.grid(row=1, sticky="e")
        label_3.grid(row=2, sticky="e")
        label_4.grid(row=3, sticky="e")
        label_5.grid(row=4, sticky="e")
        label_6.grid(row=5, sticky="e")

        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)
        entry_3.grid(row=2, column=1)
        entry_4.grid(row=3, column=1)
        entry_5.grid(row=4, column=1)
        entry_6.grid(row=5, column=1)

        submit_button = ttk.Button(self, text="Apply Changes",
                                   command=lambda: create_submit(entry_1, entry_2, entry_3, entry_4, entry_5, entry_6))
        submit_button.grid(row=6, column=1)
        return_button = ttk.Button(self, text="Take me home", command= lambda: controller.show_frame(StartPage))
        return_button.grid(row=7, sticky="e")


class UpdateEmailPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_1 = tk.Label(self, text="Old email")
        label_2 = tk.Label(self, text="New email")
        label_3 = tk.Label(self, text="Confirm new email")
        label_4 = tk.Label(self, text="Password")

        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self)
        entry_3 = tk.Entry(self)
        entry_4 = tk.Entry(self, show="*")

        label_1.grid(row=0, sticky="e")
        label_2.grid(row=1, sticky="e")
        label_3.grid(row=2, sticky="e")
        label_4.grid(row=3, sticky="e")

        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)
        entry_3.grid(row=2, column=1)
        entry_4.grid(row=3, column=1)

        submit_button = ttk.Button(self, text="Apply Changes", command=lambda: popupmsg("Haven't been finished yet"))
        submit_button.grid(row=4, column=1)
        return_button = ttk.Button(self, text="Take me home", command=lambda: controller.show_frame(StartPage))
        return_button.grid(row=5, sticky="e")


class DeleteAccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_1 = tk.Label(self, text="Login")
        label_2 = tk.Label(self, text="Password")
        entry_1 = tk.Entry(self, cursor="arrow")
        entry_2 = tk.Entry(self, cursor="arrow", show="*")
        label_1.grid(row=0, sticky="e")
        label_2.grid(row=1, sticky="e")
        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)

        submit_button = ttk.Button(self, text="Apply Changes", command=lambda: delete_submit(entry_1, entry_2))
        submit_button.grid(row=2, column=1)
        return_button = ttk.Button(self, text="Take me home", command=lambda: controller.show_frame(StartPage))
        return_button.grid(row=3, sticky="e")


class ChangePasswordPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_1 = tk.Label(self, text="Login")
        label_2 = tk.Label(self, text="Old password")
        label_3 = tk.Label(self, text="New password")
        label_4 = tk.Label(self, text="Confirm new password")

        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self, show="*")
        entry_3 = tk.Entry(self, show="*")
        entry_4 = tk.Entry(self, show="*")

        label_1.grid(row=0, sticky="e")
        label_2.grid(row=1, sticky="e")
        label_3.grid(row=2, sticky="e")
        label_4.grid(row=3, sticky="e")

        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)
        entry_3.grid(row=2, column=1)
        entry_4.grid(row=3, column=1)

        submit_button = ttk.Button(self, text="Apply Changes", command=lambda: popupmsg("Haven't been finished yet"))
        submit_button.grid(row=4, column=1)
        return_button = ttk.Button(self, text="Take me home", command=lambda: controller.show_frame(StartPage))
        return_button.grid(row=5, sticky="e")


class LogInPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_1 = tk.Label(self, text="Login")
        label_2 = tk.Label(self, text="Password")

        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self, show="*")

        label_1.grid(row=0, sticky="e")
        label_2.grid(row=1, sticky="e")

        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)

        submit_button = ttk.Button(self, text="Apply Changes", command=lambda: popupmsg("Haven't been finished yet"))
        submit_button.grid(row=2, column=1)
        return_button = ttk.Button(self, text="Take me home", command=lambda: controller.show_frame(StartPage))
        return_button.grid(row=3, sticky="e")


app = ShelfApp()
app.mainloop()
