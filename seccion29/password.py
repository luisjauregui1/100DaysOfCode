from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- Create a file ------------------------------- #
def crear_archivo_json(nombre_archivo):
    try:
        with open(nombre_archivo, "x") as archivo:
            # Escribe un objeto JSON vacío (puede ser {} o [] según tus necesidades)
            json.dump({}, archivo)
        print(f"Archivo JSON '{nombre_archivo}' creado exitosamente.")
    except FileExistsError:
        print(f"El archivo JSON '{nombre_archivo}' ya existe.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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


def search():
    global website_entry
    search_entry = website_entry.get()

    if len(search_entry) == 0:
        messagebox.showinfo(
            title="Oopss", message="Please make sure you haven't left any fields empty.")
    else:

        try:
            with open("data.json", 'r') as data_file:
                valor = json.load(data_file)
                email = valor[search_entry]["email"]
                password = valor[search_entry]["password"]

                if search_entry in valor:
                    messagebox.showinfo(title="found", message=f"email: {email}\npassword: {password}")

        except KeyError:
            messagebox.showinfo(title="Oops", message="Does not exist")

        

       


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global website_texto
    website_texto = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_texto: {
            "email": email_text,
            "password": password_text

        }
    }

    if len(email_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title="website", message=f"These are the detalis entered: \nEmail: {email_text} \nPassword: {password_text} \nIs it ok to save?")
        # Notes:
        #   json.dump() -> Write
        #   json.load() -> Read
        #   json.update() -> Update
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated dats
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

crear_archivo_json("data.json")

canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(
    file="C:\\Users\\Gustavo\\Documents\\codigo\\100DaysOfCode\\seccion29\\logo.png")
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
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "correo@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_botton = Button(text="Search", command=search)
search_botton.grid(row=1, column=3, columnspan=2)
generate_password_botton = Button(
    text="Generate Password", command=generate_password)
generate_password_botton.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
