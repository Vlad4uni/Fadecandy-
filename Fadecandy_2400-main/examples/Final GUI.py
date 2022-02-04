import tkinter as tk
import opc
from animations import *

from multiprocessing import Process
from threading import Thread


def animate(process, animation_func, client):
    if process:
        process.terminate()
    clear(client)
    process = Process(target=animation_func, args=(client, ))
    process.start()
    return process


def main():
    client = opc.Client('localhost:7890')
    animation_process = None
    window = tk.Tk()
    window.title('Welcome to Vlad\'s World quiz')
    window.geometry('450x200')

    var_lbl_main = tk.StringVar()
    lbl_main = tk.Label(textvariable=var_lbl_main,
                        font=('Arial', 18),
                        justify=tk.CENTER,
                        width=25,
                        height=2,
                        bg='blue')

    txt_answer = tk.Entry()
    btn_ready = tk.Button(text='Are you ready to start the quiz?')
    btn_enter = tk.Button(text='Enter')

    var_lbl_reply = tk.StringVar()
    lbl_reply = tk.Label(textvariable=var_lbl_reply,
                         font=('Arial', 12),
                         justify=tk.CENTER,
                         width=40,
                         height=3,
                         bg='blue',
                         wraplength=350)

    def submit_answer():
        answer = txt_answer.get().lower()
        if answer in ['bulgaria', 'america', 'spain']:
            var_lbl_reply.set(
                'How amazing is that, we have matching tastes when it comes to countries, these are my favorite countries: '
            )
        else:
            var_lbl_reply.set(
                'It appears that we do not have the same taste when it comes to countries, these are my favourite countries'
            )

        lbl_main.place_forget()
        lbl_reply.place(x=50, y=10)

        # show countries
        animate(animation_process, flags, client)

        def end_animation():
            time.sleep(20)
            var_lbl_reply.set('Thank you for participating in this quiz.')
            animate(animation_process, end, client)
            time.sleep(5)
            reset()

        # play final animation
        Thread(target=end_animation).start()

    def reset():
        btn_enter.place_forget()
        txt_answer.place_forget()
        lbl_reply.place_forget()

        var_lbl_main.set('Hello')
        lbl_main.place(x=50, y=10)

        btn_ready.configure(text='Try again')
        btn_ready.place(x=50, y=100)

        animate(animation_process, globe, client)

    def start():
        btn_ready.place_forget()

        var_lbl_main.set('What is your favorite country?')
        btn_enter.place(x=50, y=150)
        txt_answer.place(x=50, y=100)

        animate(animation_process, question, client)

    btn_enter.config(command=submit_answer)
    btn_ready.config(command=start)

    lbl_main.place(x=50, y=10)

    reset()
    btn_ready.configure(text='Are you ready to start the quiz?')
    window.mainloop()


if __name__ == '__main__':
    main()
