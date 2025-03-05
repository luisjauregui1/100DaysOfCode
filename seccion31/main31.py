from tkinter import *
from random import choice
import pandas
import time

BACKGROUND_COLOR = '#B1DDC6'
ruta = 'C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/data/5000PalabrasIngles.csv'
cart_front = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/images/card_front.png"
cart_back = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/images/card_back.png"
#--------------------------------Read CSV -----------------------------#
data = pandas.read_csv(ruta)
to_learn = data.to_dict(orient="records")

def next_cart():
    
    curretn_cart = choice(to_learn)
    
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=curretn_cart['English'])

    
    
    
# -------------------------------UI SETUP -----------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas principal con grid
canvas = Canvas(window, width=800, height=526)
background = PhotoImage(file=cart_front)
canvas.create_image(400, 263, image=background)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# Texto de Canvas principal
card_title = canvas.create_text(400, 150, text="Idioma", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="Word", fill='black', font=("Ariel", 60, 'bold'))

photo_wrong = PhotoImage(file="C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/images/wrong.png")
unknown_bottom = Button(image=photo_wrong, command=next_cart)
unknown_bottom.config(bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_bottom.grid(row=1, column=0)

photo_right = PhotoImage(file="C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion31/images/right.png")
known_bottom = Button(image=photo_right, command=next_cart)
known_bottom.config(bg=BACKGROUND_COLOR, highlightthickness=0)
known_bottom.grid(row=1,column=1)

# 3s
new_image = PhotoImage(file=cart_back)
old_image = PhotoImage(file=cart_front)
canvas_image = canvas.create_image(300,300 ,image=old_image)

# para cambiar la imagen:
canvas.itemconfig(canvas_image, image=new_image)

next_cart()

window.mainloop()