from tkinter import *
import time
import pygame
from tkinter import ttk, messagebox

INTRODUCTORY_TEXT = "Don't miss that appointment, \nIt might be the next big thing"

BOLD_FONT = "kpmg bold"
FONT = "Kpmg"

RINGTONE = ["Bell", "Bella Ciao", "Despacito", "Flute", "Footwalk", "Go", "Recorder"]

HOURS = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21",
         "22", "23"
         ]

MINUTES = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21",
           "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32",
           "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43",
           "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54",
           "55", "56", "57", "58", "59"
           ]

preferred_alarm_time = []

root = Tk()
root.title("My Alarm Clock")
root.geometry("500x800")

BACKGROUND_IMAGE = PhotoImage(file="C:/Users/ezest/PycharmProjects/Alarm Clock/"
                                   "Background_images/beautiful_morning sun.png")
BACKGROUND_IMAGE_NEW_WINDOW = PhotoImage(file="C:/Users/ezest/PycharmProjects/Alarm Clock/"
                                              "Background_images/sun_rise.png")


background_label = Label(root, image=BACKGROUND_IMAGE)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

intro_text = Label(root, text=INTRODUCTORY_TEXT, font=(FONT, 20))
intro_text.pack(padx=-0, pady=10)


def clock():
    """This function checks the current time every second (1000 millisecond) and displays it on the screen"""
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    sec = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime("%A")
    time_zone = time.strftime("%Z")

    display.config(text=f"{hour}:{minute}:{sec} {am_pm}")
    display.after(1000, clock)
    day_display.config(text=f"{day} {time_zone[0:3]}")


def turn_on_alarm():
    """This code checks the users alarm time and ringtone choice with the current time and turns on the alarm if
     condition is met. Remember the else statement recalls the function every second until the condition is met"""
    d_time_now = [time.strftime('%H'), time.strftime('%M')]
    pygame.mixer.init()
    if d_time_now == preferred_alarm_time[0:2] and len(preferred_alarm_time) > 0:
        display_alarm_title.pack(pady=(50, 10))
        display_alarm_title.config(text=preferred_alarm_time[3])
        tone_choice = preferred_alarm_time[2]
        pygame.mixer.music.load(f"C:/Users/ezest/PycharmProjects/Alarm Clock/Tones/{tone_choice}.mp3")
        pygame.mixer.music.play(loops=2)
    else:
        display.after(1000, turn_on_alarm)


display = Label(root, text="", font=(BOLD_FONT, 50), fg="black", bg="white")
display.pack(pady=(50, 10))

day_display = Label(root, text="", font=(FONT, 20))
day_display.pack(pady=1)

display_alarm_title = Label(root, text="", font=(BOLD_FONT, 50), fg="black", bg="white",
                            wraplength=600)


def second_window():
    """This is the pop-up window that allows a user pick his preferred time and ringtone for a reminder alarm"""

    def alarm_details():
        """This collects the details of the users preferred alarm time and appends it to a list"""
        tone = dropdown_menu_ringtone.get()
        min_ute = dropdown_menu_minute.get()
        ho_ur = dropdown_menu_hour.get()
        reminder_title = text_input.get("1.0", END)
        preferred_alarm_time.extend([ho_ur, min_ute, tone, reminder_title])
        dropdown_menu_ringtone.delete(0, END)
        dropdown_menu_minute.delete(0, END)
        dropdown_menu_hour.delete(0, END)
        text_input.delete("1.0", END)
        messagebox.showinfo(title="Alarm Set", message="You are all set, \nPlease close this message")

    def stop():
        """Gives the user an opportunity to stop the previewed alarm tune"""
        dropdown_menu_ringtone.get()
        pygame.mixer.music.stop()

    def play():
        """This code allows a user to preview the chosen alarm tune from the list of tunes"""
        pygame.mixer.init()
        tone_choice = dropdown_menu_ringtone.get()
        pygame.mixer.music.load(f"C:/Users/ezest/PycharmProjects/Alarm Clock/{tone_choice}.mp3")
        pygame.mixer.music.play(loops=1)

    new_window = Toplevel(root)
    new_window.title("Set Alarm")
    new_window.geometry("200x400")

    background_label_nw = Label(new_window, image=BACKGROUND_IMAGE_NEW_WINDOW)
    background_label_nw.place(x=0, y=0, relwidth=1, relheight=1)

    """Contains the different fields in the set alarm window"""
    alarm_title_nw = Label(new_window, text="Title", font=(FONT, 12), padx=10)
    alarm_title_nw.pack(padx=-0, pady=(8, 2))
    text_input = Text(new_window, height=3, width=20)
    text_input.pack(padx=-0, pady=(8, 2))

    default_hour = StringVar(new_window)
    default_hour.set(HOURS[0])  # default value
    dropdown_menu_label_hour = Label(new_window, text="Hour", font=(FONT, 12), padx=10)
    dropdown_menu_label_hour.pack(pady=(8, 2))
    dropdown_menu_hour = ttk.Combobox(new_window, textvariable=default_hour, values=HOURS)
    dropdown_menu_hour.pack(pady=(8, 2))

    default_minute = StringVar(new_window)
    default_minute.set(MINUTES[0])  # default value
    dropdown_menu_label_minute = Label(new_window, text="Minute", font=(FONT, 12), padx=10)
    dropdown_menu_label_minute.pack(pady=(8, 2))
    dropdown_menu_minute = ttk.Combobox(new_window, textvariable=default_minute, values=MINUTES)
    dropdown_menu_minute.pack(pady=(8, 2))

    default_ringtone = StringVar(new_window)
    default_ringtone.set(RINGTONE[0])  # default value
    dropdown_menu_label_ringtone = Label(new_window, text="Ringtones", font=(FONT, 10), padx=10)
    dropdown_menu_label_ringtone.pack(pady=(8, 2))
    dropdown_menu_ringtone = ttk.Combobox(new_window, textvariable=default_ringtone, values=RINGTONE)
    dropdown_menu_ringtone.pack(pady=(8, 2))

    """Contains buttons to listen and stop ringing tones as well ass to set your alarm"""
    stop_ringtone = Button(new_window, text="Stop", font=("BOLD_FONT", 12), fg="white", bg="red",
                           command=stop)
    stop_ringtone.pack(pady=(8, 2))
    play_ringtone = Button(new_window, text="Listen", font=("BOLD_FONT", 12), fg="white", bg="black",
                           command=play)
    play_ringtone.pack(pady=(8, 2))
    confirm_alarm = Button(new_window, text="OK", font=("BOLD_FONT", 12), fg="white", bg="green",
                           command=alarm_details)
    confirm_alarm.pack(pady=(8, 2))


button_nw = Button(root, text="Set Alarm", font=(BOLD_FONT, 20), fg="black", bg="white", command=second_window)
button_nw.pack(pady=(80, 10))

turn_on_alarm()
clock()


root.mainloop()
