import datetime
import tkinter as tk
from tkinter import ttk
from playsound import playsound  # Install playsound using pip install playsound

def set_alarm():
    # Get user-selected values for hours, minutes, and AM/PM
    selected_hour = hour_var.get()
    selected_minute = minute_var.get()
    am_pm = am_pm_var.get()

    # Format the alarm time string
    alarm_time_str = f"{selected_hour:02d}:{selected_minute:02d} {am_pm}"

    try:
        # Parse the alarm time string to datetime object
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%I:%M %p")
    except ValueError:
        result_label.config(text="Invalid time format. Use HH:MM AM/PM")
        return

    # Get current time and create datetime objects for comparison
    current_time = datetime.datetime.now().time()
    current_datetime = datetime.datetime.combine(datetime.date.today(), current_time)
    alarm_datetime = datetime.datetime.combine(datetime.date.today(), alarm_time.time())

    # Adjust alarm time for the next day if it's in the past
    if current_datetime > alarm_datetime:
        alarm_datetime += datetime.timedelta(days=1)

    # Calculate time difference until the alarm
    time_difference = alarm_datetime - current_datetime

    # Update result label with alarm set message
    result_label.config(text=f"Alarm set for {alarm_time.strftime('%I:%M %p')}")

    # Set a timer to play the alarm sound when the time comes
    root.after(time_difference.seconds * 1000, play_alarm)

def play_alarm():
    # Replace with the path to your alarm sound file
    playsound("onlymp3.to - iphone_alarm_sound_effect-PWn-Wh9O3N8-192k-1701399952.mp3")

# Create the main Tkinter window
root = tk.Tk()
root.title("Python Alarm Clock")

# Create a frame within the window for organizing widgets
frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Load alarm logo
alarm_logo = tk.PhotoImage(file="ios-alarm.png")
logo_label = ttk.Label(frame, image=alarm_logo)
logo_label.grid(column=0, row=0, columnspan=3)

# Widgets for setting the alarm time
entry_label = ttk.Label(frame, text="Set alarm time:")
entry_label.grid(column=0, row=1, columnspan=3, pady=10)

hour_var = tk.IntVar()
hour_combobox = ttk.Combobox(frame, textvariable=hour_var, values=list(range(1, 13)))
hour_combobox.set(datetime.datetime.now().hour)
hour_combobox.grid(column=0, row=2, padx=5)

minute_var = tk.IntVar()
minute_combobox = ttk.Combobox(frame, textvariable=minute_var, values=list(range(0, 60)))
minute_combobox.set(datetime.datetime.now().minute)
minute_combobox.grid(column=1, row=2, padx=5)

am_pm_var = tk.StringVar()
am_pm_combobox = ttk.Combobox(frame, textvariable=am_pm_var, values=["AM", "PM"])
am_pm_combobox.set(datetime.datetime.now().strftime("%p"))
am_pm_combobox.grid(column=2, row=2, padx=5)

# Button to set the alarm
set_button = ttk.Button(frame, text="Set Alarm", command=set_alarm)
set_button.grid(column=0, row=3, columnspan=3, pady=10)

# Label to display result or error messages
result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=4, columnspan=3)

# Start the Tkinter event loop
root.mainloop()
