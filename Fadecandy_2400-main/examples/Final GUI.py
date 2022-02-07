import tkinter as tk
import opc
from animations import *

from multiprocessing import Process
from threading import Thread

#function that i can call upon once it comes time to create an animation
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
    window.geometry('450x200')# size of Tkinter box

    var_lbl_main = tk.StringVar()
    lbl_main = tk.Label(textvariable=var_lbl_main,
                        font=('Arial', 18),
                        justify=tk.CENTER, #setting the size and locatiion of 
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
        if answer in ['bulgaria', 'america', 'spain']:# checks the users input against the three countries that I have entered to be my favourite countries
            var_lbl_reply.set(
                'How amazing is that, we have matching tastes when it comes to countries, these are my favorite countries: ' # response if the country appears to be one of my favourite three
            )
        else:
            var_lbl_reply.set(
                'It appears that we do not have the same taste when it comes to countries, these are my favourite countries' # response if the country appears not to be one of my favourite three
            )

        lbl_main.place_forget()
        lbl_reply.place(x=50, y=10)

        # at the same time the appropriate text appears on the Tkinter window , the 3 animations for the countries will begin in the simulations window
        animate(animation_process, flags, client)

        def end_animation():#end of participation notice appears on Tkinter while the end animation plays at the same time 
            time.sleep(20)
            var_lbl_reply.set('Thank you for participating in this quiz.')
            animate(animation_process, end, client)
            time.sleep(5)
            reset()

        # play final animation
        Thread(target=end_animation).start()

    def reset(): #overall reset of both Tkinter window and the simulation window
        btn_enter.place_forget() 
        txt_answer.place_forget()
        lbl_reply.place_forget()
#previous buttons disapear and new buttons appear (initial buttons)
        var_lbl_main.set('Hello')
        lbl_main.place(x=50, y=10)

        btn_ready.configure(text='Try again')#for the process to start again the user has to press this button because otherwise the process will just stop here and wait for a human response
        btn_ready.place(x=50, y=100)

        animate(animation_process, globe, client) #similar to the Tkinter window , the animations that appear in the simulation window are also all reset 
                                                                                  #therefore  the animations cycle begins again with the globe 
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

