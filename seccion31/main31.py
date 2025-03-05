from tkinter import *
from random import choice
import pandas
import time

BACKGROUND_COLOR = '#B1DDC6'
current_card = {}
to_learn = {}
ruta = 'C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/data/5000PalabrasIngles.csv'
cart_front = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/images/card_front.png"
cart_back = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/images/card_back.png"
wrong = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/images/wrong.png"
right = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/images/right.png"
safe = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/data/word_to_learn.csv"
# --------------------------------Read CSV -----------------------------#
try:
    data = pandas.read_csv(safe)
except FileNotFoundError:
    original_data = pandas.read_csv(ruta)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_cart():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill='black')
    canvas.itemconfig(card_word, text=current_card['English'], fill='black')
    canvas.itemconfig(card_background, image=card_font_img)
    flip_timer = window.after(3000, func=flip_card)
    

def flip_card():
    canvas.itemconfig(card_title, text="Spanish", fill="white")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(safe, index=False)
    next_cart()
    
# -------------------------------UI SETUP -----------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas principal con grid
canvas = Canvas(window, width=800, height=526) 
card_font_img = PhotoImage(file=cart_front)
card_back_image = PhotoImage(file=cart_back)
card_background = canvas.create_image(400, 263, image=card_font_img)
card_title = canvas.create_text(400, 150, text="Idioma", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="Word", fill='black', font=("Ariel", 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# boton x
photo_wrong = PhotoImage(file=wrong)
unknown_bottom = Button(image=photo_wrong, highlightthickness=0, command=next_cart)
unknown_bottom.grid(row=1, column=0)
# boton ✔
photo_right = PhotoImage(file=right)
known_bottom = Button(image=photo_right, highlightthickness=0, command=is_known)
known_bottom.grid(row=1, column=1)

next_cart()

window.mainloop()
