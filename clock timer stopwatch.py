from tkinter import *
import time
from datetime import datetime

def display_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label['text'] = current_time
    root.after(1000, display_time)

def start_timer():
    given_time = entry_timer.get()
    try:
        time.strptime(given_time, '%H:%M')
    except ValueError:
        label_timer['text'] = 'Incorect input. Please try again.'
    temp = datetime.strptime(given_time, '%H:%M')
    seconds_left = temp.hour*3600 + temp.minute*60
    countdown(seconds_left)

def countdown(seconds_left):
    if seconds_left > 0:
        label_timer.configure(text=seconds_left)
        seconds_left = seconds_left - 1
        root.after(999, countdown(seconds_left)) 
    else:
        label_timer.configure(text='Time is up!')

def stop_timer():
    return

def reset_timer():
    timer.set('00:00')

root = Tk()
root.title('CLOCK')
root.geometry('300x500')
root.resizable(False, False)

# Top part - displaying time
frame_clock = LabelFrame(root, text='Clock', padx=20, pady=20)
frame_clock.pack(padx=10, pady=10)
clock_label = Label(frame_clock, font='ariel 40')
clock_label.pack()
display_time()

# Middle part - timer
frame_timer = LabelFrame(root, text='Timer', padx=20, pady=20)
frame_timer.pack(padx=10, pady=10)
timer = StringVar()
timer.set('00:00')
label_timer = Label(frame_timer, width=30, font='Arial 10', text='Input time in HH:MM format:', justify=CENTER)
entry_timer = Entry(frame_timer, width=10, font='arial 20', textvariable=timer, justify=CENTER)
timer_start = Button(frame_timer, text='Start', font='Arial 15', command=start_timer)
timer_stop = Button(frame_timer, text='Stop', font='Arial 15', command=stop_timer)
timer_reset = Button(frame_timer, text='Reset', font='Arial 15', command=reset_timer)
label_timer.grid(row=0, column=0, columnspan=3, pady=10)
entry_timer.grid(row=1, column=0, columnspan=3, pady=10)
timer_start.grid(row=2, column=0)
timer_stop.grid(row=2, column=1, padx=5)
timer_reset.grid(row=2, column=2)

# Bottom part - stopwatch
frame_stopwatch = LabelFrame(root, text='Stopwatch', padx=20, pady=20)
frame_stopwatch.pack(padx=10, pady=10)

mainloop()