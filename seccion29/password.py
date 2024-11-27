from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    ruta_file = "C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion29/data.txt"
    
    website_texto = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    
    if len(email_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the detalis entered: \nEmail: {email_text}    \nPassword: {password_text} \nIs it ok to save?" )
        
        if is_ok:
            f = open(ruta_file, "a")
            f.write(f"{website_texto} | {email_text} | {password_text} \n")
            f.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    
        
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file="C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=35)
website_entry.grid(row=1 , column=1 , columnspan=2 )
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "correo@gmail.com" )
password_entry = Entry(width=21)  
password_entry.grid(row=3, column=1)

# Buttons

generate_password_botton = Button(text="Generate Password", command=generate_password)
generate_password_botton.grid(row=3, column=2,)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4 , column=1, columnspan=2 )



window.mainloop()