import math
from tkinter import *
import tkinter.font
from playsound import playsound
import pyglet, os

PINK = "#e2979C"
RED = "#d61d1d"
GREEN = "#97c447"
YELLOW = "#f7f5dd"
FONT = "#Courier"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
rep = 0
timer=None

def resettimer():
    window.after_cancel(timer)
    label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    global  rep
    rep=0



def play():
    playsound('alarm.mp3')
def start_timer():
    global rep
    rep += 1
    print(rep)



    if (rep % 8 == 0):
        label.config(text="Take A Break!")
        countdown(LONG_BREAK * 60)
        print("Over")
    elif rep % 2 == 0:
        label.config(text="Take A Break!")
        countdown(SHORT_BREAK * 60)

    else:
        label.config(text="Work Work Work!",fg=RED)
        countdown(WORK_MIN * 60)



def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer= window.after(1000, countdown, count - 1)
    else:
        marks=""
        for _ in range(math.floor(rep/2)):
            marks+="✔"

        check.config(text=marks)
        play()
        start_timer()



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=512, height=512, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(250, 250, image=tomato_img)
timer_text = canvas.create_text(250, 300, text="00:00", fill="white", font=(FONT, 43, "bold"))
canvas.grid(column=2, row=1)
Desired_font = tkinter.font.Font(family="Comic Sans MS",
                                 size=20,
                                 weight="bold"
                                 )

label = Label(text="TIMER", font=("Comic Sans MS",
                                  55,
                                  "bold"), fg=GREEN)
label.config(bg=YELLOW)
label.grid(column=2, row=0)

button = Button(text="Start", font=Desired_font, fg=GREEN, highlightthickness=0, command=start_timer)
button.config(bg=YELLOW)
button.grid(column=1, row=3)

button2 = Button(text="Reset", font=Desired_font, fg=GREEN, highlightthickness=0,command=resettimer)
button2.config(bg=YELLOW)
button2.grid(column=3, row=3)

check = Label(text="", font=("Comic Sans MS",
                              30,
                              "bold"), fg=GREEN)
check.config(bg=YELLOW)
check.grid(column=2, row=4)

window.mainloop()
