import tkinter as tk
from tkinter import messagebox
import time
import datetime
import pygame

def set_alarm():
    global alarm_time, alarm_period
    alarm_time, alarm_period = time_var.get().split()
    alarm_hour, alarm_minute = alarm_time.split(":")
    alarm_hour = int(alarm_hour)
    alarm_minute = int(alarm_minute)
    if alarm_period == "PM" and alarm_hour == 12:
        alarm_hour = 0
    if alarm_period == "AM" and alarm_hour != 12:
        alarm_hour += 12
    alarm_time = f"{alarm_hour:02d}:{alarm_minute:02d}"

def start_alarm():
    global alarm_time, alarm_period
    current_time = time.strftime("%H:%M")
    while current_time != alarm_time:
        time.sleep(1)
        current_time = time.strftime("%H:%M")
    pygame.init()
    pygame.mixer.music.load("C:\\Users\\DELL\\Downloads\\music.mp3")
    pygame.mixer.music.play()
    result = messagebox.askokcancel("Alarm", "Time to wake up!!!!!!!\nClick OK to snooze or Cancel to stop the alarm.")
    while result:
        time.sleep(60)
        pygame.mixer.music.play()
        result = messagebox.askokcancel("Alarm", "Time to wake up!\nClick OK to snooze or Cancel to stop the alarm.")

def stop_alarm():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("Alarm Clock By DIV..")

frame = tk.Frame(root)

label = tk.Label(frame, text="---------Enter the time for the alarm (HH:MM AM/PM):---------")
label.pack()

time_var = tk.StringVar()
entry = tk.Entry(frame, textvariable=time_var)
entry.pack()

set_button = tk.Button(frame, text="Set Alarm", command=set_alarm)
set_button.pack()
start_button = tk.Button(frame, text="Start Alarm", command=start_alarm)
start_button.pack()
stop_button = tk.Button(frame, text="Stop Alarm", command=stop_alarm)
stop_button.pack()

frame.pack()

root.mainloop()


