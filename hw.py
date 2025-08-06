from tkinter import Tk, Label, Button, Entry, Text, END
from datetime import datetime

screen = Tk()
screen.title("Age")
screen.geometry('600x400')

dayl = Label(text="What day were you born in (in numbers)?", fg="white", bg="grey", height=1, width=50)
daye = Entry()
monthl = Label(text="What month were you born in (in numbers)?", fg="white", bg="grey", height=1, width=50)
monthe = Entry()
yearl = Label(text="What year were you born in (in numbers)?", fg="white", bg="grey", height=1, width=50)
yeare = Entry()

tb = Text(height=3)

def age():
    tb.delete('1.0', END)
    day = int(daye.get())
    month = int(monthe.get())
    year = int(yeare.get())
    birth_date = datetime(year, month, day)
    today = datetime.now()

    age_years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1
    if age_years < 0 or age_years == 0:
                tb.insert(END, f"You are not born.")
    else:
                tb.insert(END, f"You are {age_years} years old.")
dayl.pack()
daye.pack()
monthl.pack()
monthe.pack()
yearl.pack()
yeare.pack()
Button(text="Calculate", command=age, height=1, bg="#1261A0", fg='white').pack()
tb.pack()

screen.mainloop()
