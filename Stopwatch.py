#!/usr/bin/env python3

from tkinter import *
from time import *
from playsound import playsound

HOURS = 0
MINUTES = 0
SECONDS = 0
HUNDREDS = 0
TIME_CIRCLE = 2
CIRCLE_TIME_LABEL = []
RUN_TIME = False

def update():

    
    global HOURS, MINUTES, SECONDS, HUNDREDS, RUN_TIME

    HUNDREDS += 1

    if HUNDREDS == 10:
        SECONDS += 1
        HUNDREDS = 0

    if SECONDS == 60:
        MINUTES += 1
        SECONDS = 0

    if MINUTES == 60:
        HOURS += 1
        MINUTES = 0

    if HOURS == 24:
        HOURS = 0

    time_lable.config(text=f'{HOURS:02}:{MINUTES:02}:{SECONDS:02}.{HUNDREDS:1}')

    if RUN_TIME == True:
        update_time = time_lable.after(100, update)


def start():
    global RUN_TIME
    RUN_TIME = True

    playsound('/home/zule/Python_learning/Done Projects/Stopwatch/Start.mp3')
    start_button.config(text="Stop", command=stop)
    reset_button.config(state=DISABLED)
    circle_button.config(state=NORMAL)

    update()
    

def stop():

    global RUN_TIME
    RUN_TIME = False
    start_button.config(text="Start", command=start)
    reset_button.config(state=NORMAL)
    reset_all_button.config(state=NORMAL)
    circle_button.config(state=DISABLED)
    playsound('/home/zule/Python_learning/Done Projects/Stopwatch/Stop.mp3')


def circle():
    global HOURS, MINUTES, SECONDS, HUNDREDS, TIME_CIRCLE, CIRCLE_TIME_LABEL
    
    if TIME_CIRCLE == 7:
        TIME_CIRCLE = 2

    CIRCLE_TIME_LABEL_member = Label(counter_frame, font=("Arial", 30), text=f'{HOURS:02}:{MINUTES:02}:{SECONDS:02}.{HUNDREDS:1}')
    CIRCLE_TIME_LABEL.append(CIRCLE_TIME_LABEL)

    CIRCLE_TIME_LABEL_member.grid(row=TIME_CIRCLE, column=0, columnspan=4)
    
    TIME_CIRCLE += 1


def reset():
    global HOURS, MINUTES, SECONDS, HUNDREDS
    HOURS, MINUTES, SECONDS, HUNDREDS = 0, 0, 0, 0

    time_lable.config(text=f'{HOURS:02}:{MINUTES:02}:{SECONDS:02}.{HUNDREDS:1}')

def reset_all():
    global counter_frame

    stop()
    reset()

    counter = 0

    for label in counter_frame.winfo_children():
        
        counter += 1
        if counter > 5:
            label.destroy()


main_window = Tk()
main_window.title("Stopwatch")


counter_frame = Frame(main_window, bd=5, relief=RAISED)
counter_frame.pack()


time_lable = Label(counter_frame, font=("Arial", 30), text="00:00:00.0")
start_button = Button(counter_frame, font=("Arial", 14), text="Start", command=start)
circle_button = Button(counter_frame, font=("Arial", 14), text="Circle", state=DISABLED, command=circle)
reset_button = Button(counter_frame, font=("Arial", 14), text="Reset", command=reset)
reset_all_button = Button(counter_frame, font=("Arial", 14), text="Reset All", state=DISABLED, command=reset_all)

time_lable.grid(row=0, column=0, columnspan=4)


start_button.grid(row=1, column=0)
circle_button.grid(row=1, column=1)
reset_button.grid(row=1, column=2)
reset_all_button.grid(row=1, column=3)


main_window.mainloop()


#TO DO
#Add File menu
#Add key bindings
#Add save posiblility
#Create exe