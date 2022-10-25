from tkinter import *
import random, string

User = Tk()
User.geometry("400x280")
User.title("Password Generator")
User.attributes("-toolwindow", 1)
User.resizable(width=FALSE, height=FALSE)

title = StringVar()

label = Label(User, textvariable=title, anchor=N, pady=10).pack()

title.set("Password strength:")

                    # 3 choises Basic Medium or Plus  #
                    # Basic just str #
                    # Medium str and int #
                    # Plus str, int and symbols #


def sel():
    selection = choice.get()

choice = IntVar()
l1 = Radiobutton(User, text="BASIC", variable=choice, value=1, command=sel).pack(anchor=CENTER)
l2 = Radiobutton(User, text="MEDIUM", variable=choice, value=2, command=sel).pack(anchor=CENTER)
l3 = Radiobutton(User, text="PLUS", variable=choice, value=3, command=sel).pack(anchor=CENTER)
labelchoice = Label(User)
labelchoice.pack()

                    # pass lenght information #
lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(User, textvariable=lenlabel).pack()

                    # pass lenght number #
val = IntVar()
spinlenght = Spinbox(User, from_=8, to_=16, textvariable=val, width=13).pack()

                    # passprint #


def call_back():
    lsum.config(text=passgen())


                    #  button #
passgenButton = Button(User, text="Generate Your Password", relief=RIDGE, bd=5, height=2, command=call_back, pady=3)
passgenButton.pack()
password = str(call_back)

                    #  result message #
lsum = Label(User, text="")
lsum.pack(side=BOTTOM)


lownum = string.ascii_uppercase + string.ascii_lowercase + string.digits
lowupp = string.ascii_uppercase + string.ascii_lowercase
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
everything = lowupp + lownum + symbols


def pwdgen():
    if choice.get() == 1:
        return "".join(random.sample(lowupp, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(lownum, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(everything, val.get()))


User.mainloop()
