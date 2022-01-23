from tkinter import *

window = Tk()

window.title("Welcome to Vlad's World quiz")

window.geometry('600x300')

lbl = Label(window, text="Hello", font=("Arial Bold", 40))

lbl.grid(column=0, row=0)

def start():

    lbl.configure(text="What is your favourite country ?",font=("Arial Bold", 20))

btn = Button(window, text="Are you ready to start ?", bg="green", fg="orange" ,command=start)
btn.grid(column=1, row=2)

def enter():
    lbl.confiigure(text="Please enter your favorite country in full capitals !",font=("Arial Bold", 20))

btn2 = Button(window, text="Enter", bg="green", fg="orange" ,command=enter)
btn2.grid(column=1, row=4)

window.mainloop()
