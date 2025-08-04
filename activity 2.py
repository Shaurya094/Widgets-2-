from tkinter import Tk, Label, Button, Entry, Frame, Text, END

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, eidth=360, bg="#de0efff")

lbl1 = Label(frame, text = "Full Name", bg="#3895D3", fg = "white", width = 12)
lbl2 = Label(frame, text = "Email ID", bg="#3895D3", fg = "white", width = 12)
lbl1 = Label(frame, text = "Passoword", bg="#3895D3", fg = "white", width = 12)

nameE = Entry(frame)
emailE= Entry(frame)
passE = Entry(frame, show="*")

textbox = Text(bg="blue", fg="black")
def display():
    name = nameE.get()
    intro = "Hey "+name
    msg = "\nAccount created."
    textbox.insert(END, intro)
    textbox.insert(END, msg)

