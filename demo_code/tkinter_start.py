from tkinter import *

LARGE_FONT = ("Verdana", 11)

class ShelfApp(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Let's get started and make out life easier",
                      font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        button1 = Button(self, text="Create an account", fg="purple")
        button2 = Button(self, text="Update your email", fg="blue")
        button3 = Button(self, text="Change your password", fg="green")
        button4 = Button(self, text="Log in", fg="orange")
        button5 = Button(self, text="Delete an account", fg="red")

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()


app = ShelfApp()
app.mainloop()