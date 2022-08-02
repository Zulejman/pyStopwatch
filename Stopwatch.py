#!/usr/bin/env python3

from tkinter import *
from time import *

hours = 0
minutes = 0
seconds = 0
hundreds = 0
time_circle = 2
circle_time_lable = []
run_time = False

def update():

    
    global hours, minutes, seconds, hundreds, run_time

    hundreds += 1

    if hundreds == 10:
        seconds += 1
        hundreds = 0

    if seconds == 60:
        minutes += 1
        seconds = 0

    if minutes == 60:
        hours += 1
        minutes = 0

    if hours == 24:
        hours = 0

    time_lable.config(text=f'{hours:02}:{minutes:02}:{seconds:02}.{hundreds:1}')

    if run_time == True:
        update_time = time_lable.after(100, update)


def start():
    global run_time
    run_time = True

    start_button.config(text="Stop", command=stop)
    reset_button.config(state=DISABLED)
    circle_button.config(state=NORMAL)

    update()
    

def stop():
    global run_time
    run_time = False

    start_button.config(text="Start", command=start)
    reset_button.config(state=NORMAL)
    reset_all_button.config(state=NORMAL)
    circle_button.config(state=DISABLED)


def circle():
    global hours, minutes, seconds, hundreds, time_circle, circle_time_lable
    
    if time_circle == 7:
        time_circle = 2

    circle_time_lable_member = Label(counter_frame, font=("Arial", 30), text=f'{hours:02}:{minutes:02}:{seconds:02}.{hundreds:1}')
    circle_time_lable.append(circle_time_lable)

    circle_time_lable_member.grid(row=time_circle, column=0, columnspan=4)
    
    time_circle += 1


def reset():
    global hours, minutes, seconds, hundreds
    hours, minutes, seconds, hundreds = 0, 0, 0, 0

    time_lable.config(text=f'{hours:02}:{minutes:02}:{seconds:02}.{hundreds:1}')

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
