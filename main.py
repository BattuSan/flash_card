from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    words_list = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_list = read_csv("data/french_words.csv")
words = words_list.to_dict(orient="records")
current_card = {}


# -------------- csv ---------------------
def refresh():
    global current_card
    global clock
    window.after_cancel(clock)
    current_card = random.choice(words)
    french_word = current_card["French"]
    canvas.itemconfig(background, image=white_background)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(language, text=f"{french_word}", fill="black")
    clock = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    english_word = current_card["English"]
    canvas.itemconfig(background, image=green_background)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(language, text=f"{english_word}", fill="white")


def remove_words():
    global current_card
    words.remove(current_card)
    new_data = DataFrame(words)
    new_data.to_csv("data/words_to_learn.csv", index=FALSE)
    refresh()


# ----------------- UI ---------------------

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
clock = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
white_background = PhotoImage(file="./images/card_front.png")
green_background = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=white_background)
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
language = canvas.create_text(400, 263, text="Hello", font=("Arial", 60, "bold"))

tick_image = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, background=BACKGROUND_COLOR, command=remove_words)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=refresh)

canvas.grid(column=0, row=0, columnspan=2)
tick_button.grid(column=1, row=1)
cross_button.grid(column=0, row=1)
refresh()
window.mainloop()
