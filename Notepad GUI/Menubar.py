from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from subprocess import call
import tkinter.font as tkf

fontoption = "lucida"
fontstyle = "normal"
fontsize = 12


def new():
    global file
    root.title("Notepad")
    textarea.delete(1.0, END)


def new_p():
    call(["python", "Menubar.py"])


def f_open():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file))
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read)
        f.close()


def save():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Notepad.txt", defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def save_as():
    global file
    file = asksaveasfilename(initialfile=f"{file}.txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
                             defaultextension=".txt")
    f = open(file, "w")
    f.write(textarea.get(1.0, END))
    f.close()


def f_print():
    os.startfile(textarea, "print")


def stop():
    global file
    if file is None:
        e = msg.askyesno("Exit ", "Do you want to Save you File ?")
        if e == YES:
            save()
            exit()
        else:
            exit()
    else:
        exit()


def undo():
    textarea.event_generate("<<Undo>>")


def redo():
    textarea.edit_redo()


def select_all():
    textarea.tag_add("sel", 1.0, END)


def cut():
    textarea.event_generate("<<Cut>>")


def copy():
    textarea.event_generate("<<Copy>>")


def paste():
    textarea.event_generate("<<Paste>>")


def delete():
    textarea.delete(1.0, END)


def font():
    font_ls = list(tkf.families())

    def set_op():
        textarea.config(font=f"{font_ls[font.curselection()[0]]} {fontsize} {fontstyle}")

    font_root = Toplevel(root)
    font_root.title("Font")
    font_root.geometry("480x360")

    font_label = Label(font_root, text="Font\n\n", font="ariel 25")
    font_label.place(x=3, y=3)
    font = Listbox(font_root, font="lucida 11")
    font.place(x=21, y=51)

    for i in tkf.families():
        font.insert(END, i)

    Button(font_root, text="Ok", font="lucida 11", command=set_op).place(x=151, y=151)

    font_root.mainloop()


def style():
    style_ls = ["normal", "bold", "italic", "roman", "underline"]

    def set_style():
        textarea.config(font=f"{fontstyle} {fontsize} {style_ls[style.curselection()[0]]}")

    style_root = Toplevel(root)
    style_root.title("Style")
    style_root.geometry("480x360")

    style_label = Label(style_root, text="Font Style\n\n")
    style_label.place(x=3, y=3)
    style = Listbox(style_root)
    style.place(x=21, y=51)

    style.insert(END, "normal")
    style.insert(END, "bold")
    style.insert(END, "italic")
    style.insert(END, "roman")
    style.insert(END, "underline")

    Button(style_root, text="Ok", font="lucida 11", command=set_style).place(x=151, y=151)
    style_root.mainloop()


def size():
    size_ls = list(range(8, 73))

    def set_size():
        textarea.config(font=f"{fontoption} {size_ls[size.curselection()[0]]} {fontstyle}")

    size_root = Toplevel(root)
    size_root.title("Size")
    size_root.geometry("480x360")

    size_label = Label(size_root, text="Font Size\n\n")
    size_label.place()
    size = Listbox(size_root)
    size.place(x=21, y=51)

    for i in range(8, 73):
        size.insert(END, i)

    Button(size_root, text="Ok", font="lucida 11", command=set_size).place(x=151, y=151)
    size_root.mainloop()


def f_help():
    msg.showinfo("Notepad",
                 "1) You can Write the information in the text area \n"
                 "2) The option to Save , Make new file is available in the File menu section \n"
                 "3) You can Exit whenever you want to Exit and we will ask you if any problem or warning is there \n"
                 "4) Fonts option will be available in the next iteration \n"
                 "5) For some queries Visit Contact Us section in the Help menu\n")


def contact():
    msg.showinfo("Notepad",
                 "Creator : Om Londhe\n"
                 "Contact no. : 7276594467\n"
                 "E-mail id : oplondhe@gmaiil.com\n")


def about():
    msg.showinfo("Notepad",
                 "This is the Notepad .\n"
                 "It is made by Om Londhe using the tKinter package in the Python ......\n"
                 "The version of python used is the Python 3.7.4\n")


root = Tk()
root.title("Notepad")
root.geometry("720x480")
root.wm_iconbitmap("ntpd.png")

m = Menu(root)
m1 = Menu(m, tearoff=0)
m1.add_command(label="New", command=new)
m1.add_command(label="New Window", command=new_p)
m1.add_separator()
m1.add_command(label="Open", command=f_open)
m1.add_separator()
m1.add_command(label="Save", command=save)
m1.add_command(label="Save as", command=save_as)
m1.add_command(label="Print", command=f_print)
m1.add_separator()
m1.add_command(label="Exit", command=stop)
root.config(menu=m)
m.add_cascade(label="File", menu=m1)

m1 = Menu(m, tearoff=0)
m1.add_command(label="Undo", command=undo)
m1.add_command(label="Redo", command=redo)
m1.add_command(label="Select all", command=select_all)
m1.add_separator()
m1.add_command(label="Cut", command=cut)
m1.add_command(label="Copy", command=copy)
m1.add_command(label="Paste", command=paste)
m1.add_command(label="Delete", command=delete)
root.config(menu=m)
m.add_cascade(label="Edit", menu=m1)

m1 = Menu(m, tearoff=0)
m1.add_checkbutton(label="Wordwrap")
# fm = Menu(m1, tearoff=0)
m1.add_command(label="Font", command=font)
# m1.add_command(label="Font Style", command=style)
# m1.add_command(label="Text Size", command=size)
# m1.add_cascade(label="Font", menu=fm)
root.config(menu=m)
m.add_cascade(label="Format", menu=m1)

m1 = Menu(m, tearoff=0)
m1.add_command(label="View Help", command=f_help)
m1.add_command(label="Contact Us", command=contact)
m1.add_separator()
m1.add_command(label="About Notepad", command=about)
root.config(menu=m)
m.add_cascade(label="Help", menu=m1)

bary = Scrollbar(root)
bary.pack(side=RIGHT, fill=Y)

barx = Scrollbar(root, orient=HORIZONTAL)
barx.pack(side=BOTTOM, fill=X)

textarea = Text(root, yscrollcommand=bary.set, xscrollcommand=barx.set, undo=True,
                font=f"{fontoption} {fontsize} {fontstyle}")
file = None
textarea.pack(fill=BOTH, expand=True)

bary.config(command=textarea.yview)
barx.config(command=textarea.xview)

root.mainloop()
