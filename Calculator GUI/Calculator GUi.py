from tkinter import *


def click(event):

    global value

    ip = event.widget.cget("text")

    if ip == "=":
        if value.get().isdigit():
            val = int(value.get())
        else:
            try:
                val = eval(output.get())
                value.set(val)
                output.update()
            except:
                value.set("Syntax Error") 
                output.update()
    elif ip == "AC":
        value.set("")
        output.update()
    elif ip == "BKSP":
        value.set(output.delete(0, (len(value.get()) - (len(value.get())-1))))
        output.update()
    else:
        value.set(value.get() + ip)
        output.update()


root = Tk()

root.title("Calculator")
root.wm_iconname("Calculator")
root.wm_iconbitmap("calc.png")
root.geometry("275x360")
root.maxsize(275, 360)
root.minsize(275, 360)

value = StringVar()
value.set("")
output = Entry(root, textvar=value, font="lucida 30 bold")
output.pack(padx=12, pady=5, fill="x")

f = Frame(root, bg="black")

b = Button(f, text="1/2", padx=5, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=9, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="AC", padx=5, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="BKSP", padx=5, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")

b = Button(f, text="7", padx=13, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=12, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=13, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=16, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")

b = Button(f, text="4", padx=13, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=12, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=13, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=15, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")

b = Button(f, text="1", padx=13, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=12, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=13, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=15, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")

b = Button(f, text=".", padx=13, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=12, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=13, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)
b.bind("<Key>", click)

b = Button(f, text="+", padx=14, pady=5, font="bold")
b.pack(padx=5, pady=5, side=LEFT)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()
