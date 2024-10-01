from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('Miles to Kilometer Converter') 
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

def obtener_valor():
    try:
        valor = float(entrada_valor.get())
        actualizar_label(valor)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrea un numero valido")

def actualizar_label(nuevo_valor):
        nuevo_valor = nuevo_valor * 1.609
        label3.config(text=f"{nuevo_valor}")

        
# Entry
entrada_valor = Entry(width=10)
entrada_valor.insert(END, string=0)
# Gets text in entry
print(entrada_valor.get())
entrada_valor.grid(column=1, row=0)

# Label miles
my_label = Label(text="Miles", font=("Arial", 12,"normal"))
my_label.grid(column=2, row=0)

# Label is equal to
label2 = Label(text="is equal to", font=("Arial", 12,"normal"))
label2.grid(column=0,row=1)

label3 = Label(text=0, font=("Arial", 12,"normal"))
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=("Arial", 12,"normal"))
label4.grid(column=2,row=1)

# Button
button = Button(text="Calculate" , command=obtener_valor)
button.grid(column=1,row=2)

# ejemplo: 5 millas x 1,609 = 8,045 kilómetros




window.mainloop()
