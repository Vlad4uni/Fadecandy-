from tkinter import *

window = Tk()

window.title("Welcome to Vlad's World quiz")

window.geometry('600x300')

lbl = Label(window, text="Hello", font=("Arial Bold", 40))

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="What is your favourite country ?",font=("Arial Bold", 20))

btn = Button(window, text="Shaw we begin ?", bg="green", fg="orange" ,command=clicked)

btn.grid(column=1, row=2)

window.mainloop()
