from tkinter import *

def log_in_table() -> None:
    additional = Tk()
    label_1 = Label(additional, text="Login")
    label_2 = Label(additional, text="Password")
    entry_1 = Entry(additional)
    entry_2 = Entry(additional, show="*")
    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)

    additional.mainloop()


def new_account_table() -> None:

    additional = Tk()
    label_1 = Label(additional, text="Name")
    label_2 = Label(additional, text="Surname")
    label_3 = Label(additional, text="Login")
    label_4 = Label(additional, text="Password")
    label_5 = Label(additional, text="Email")
    label_6 = Label(additional, text="Country")
    entry_1 = Entry(additional, cursor="arrow")
    entry_2 = Entry(additional, cursor="man")
    entry_3 = Entry(additional, cursor="spider", fg="pink")
    entry_4 = Entry(additional, cursor="target", show="*")
    entry_5 = Entry(additional, cursor="star")
    entry_6 = Entry(additional, cursor="heart")
    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    label_3.grid(row=2, sticky=E)
    label_4.grid(row=3, sticky=E)
    label_5.grid(row=4, sticky=E)
    label_6.grid(row=5, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    entry_3.grid(row=2, column=1)
    entry_4.grid(row=3, column=1)
    entry_5.grid(row=4, column=1)
    entry_6.grid(row=5, column=1)

    additional.mainloop()


def delete_an_account() -> None:
    additional = Tk()
    label_1 = Label(additional, text="Login")
    label_2 = Label(additional, text="Password")
    entry_1 = Entry(additional, cursor="arrow")
    entry_2 = Entry(additional, cursor="arrow", show="*")
    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    additional.mainloop()


root = Tk()

welcome_label = Label(root, text="Welcome to the very first app of my own",
                      bg="white", fg="black")

button1 = Button(text="Create an account", fg="purple", command=new_account_table)
button2 = Button(text="Update your email", fg="blue")
button3 = Button(text="Change your password", fg="green")
button4 = Button(text="Log in", fg="orange", command=log_in_table)
button5 = Button(text="Delete an account", fg="red", command=delete_an_account)
welcome_label.grid(row=0, sticky=E)
button1.grid(row=1, sticky=W)
button2.grid(row=2, sticky=W)
button3.grid(row=3, sticky=W)
button4.grid(row=4, sticky=W)
button5.grid(row=5, sticky=W)

root.mainloop()


#class basic_window:

 #   def __init__(self, master):
  #      frame = Frame(master)
   #     frame.pack()


# button1.bind("<Button-1>", create_an_account)
# def create_an_account(event)