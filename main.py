import tkinter as tk
import time

def set_alarm():
    global alarm_time
    alarm_time = alarm_entry.get()
    alarm_label.config(text="Alarm set for " + alarm_time,font=("Helvetica", 40))

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    if alarm_time and current_time[:5] == alarm_time[:5]:
        alarm_label.config(text="ALARM!", font=("Helvetica", 40))

    time_label.after(1000, update_time)

# Create GUI window
window = tk.Tk()
window.title("Alarm Clock")
window.config(bg='lightgreen')

# Create GUI components
time_label = tk.Label(window, text="", font=("Helvetica", 48))
alarm_label = tk.Label(window, text="", font=("Helvetica", 48))
my_label=tk.Label(window,text="Enter as Hr:min:Sec",font=("Helvetica", 24))
alarm_entry = tk.Entry(window, font=("Helvetica", 14))
set_alarm_button = tk.Button(window, text="Set Alarm",font=("Helvetica", 24), command=set_alarm)

# Place components in the window
time_label.pack(pady=20)
alarm_label.pack()
my_label.pack(pady=20)
alarm_entry.pack(pady=10)
set_alarm_button.pack()

# Initialize alarm_time
alarm_time = ""

# Start the clock update loop
update_time()

# Start GUI event loop
window.mainloop()
