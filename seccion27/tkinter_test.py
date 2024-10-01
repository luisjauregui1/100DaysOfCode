from tkinter import *

window = Tk()

window.title('My first GUI Program')
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label['text'] = 'New Text'
my_label.config(text="New Text")

# Button
def button_click():
    valor = input.get()
    my_label.config(text=valor)    

# Button
button = Button(text="Click Me", command=button_click)
button.grid(column=2,row=1)

# Entry
input = Entry(width=30)
input.insert(END, string="Some text to being with.")
# Gets text in entry
print(input.get())
input.grid(column=3, row=1)

text = Text(height=5,width=30)
text.focus()

text.insert(END, "Explane of multi-line text entry.")
print(text.get("1.0",END))
text.grid()

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid()

# Scale
# Called with current scale value. 
def scale_used(value):
    print(value)
    
scale = Scale(from_=0, to=100, command=scale_used)
scale.grid()

# CheckButton
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?",variable=checked_state,command=checkbutton_used)

checked_state.get()
checkbutton.grid()

# RadioButton
def radio_used():
    print(radio_state.get())
    
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="Option2", value=2, variable= radio_used)
radiobutton1.grid()
radiobutton2.grid()

# listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apple', "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
    
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.grid()



window.mainloop()
