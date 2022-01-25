import tkinter as tk

window = tk.Tk()

window.title("Welcome to Vlad's World quiz")

window.geometry('450x200')

lbl = tk.Label(window, text="Hello", font=("Arial Bold", 40))

lbl.place(x=95, y=10)

def start():

    lbl.configure(text="What is your favourite country ?",font=("Arial Bold", 20))
    lbl.place(x=0, y=10)

btn = tk.Button(window, text="Are you ready to start the quiz ?", bg="green", fg="orange" ,command=start)
btn.place(x=80, y=100)


txtfld=tk.Entry(window, text="Country typed in here", bd=5)
txtfld.place(x=100, y=170)


def Enter():
    lbl.confiigure(text="Please enter your favorite country in full capitals !",font=("Arial Bold", 20))
    lbl.place(x=0, y=0)


btn2 = tk.Button(window, text="Enter", bg="green", fg="orange" ,command=Enter)
btn2.place(x=140, y=130)

window.mainloop()
