from tkinter import *
import requests

# Mi resultaod
def get_quote():
    # Make a get() request to the kanye rest API.
    response = requests.get(url="https://api.kanye.rest/")
    # Raise an exepection if the request returned and unsuccessful status code.
    response.raise_for_status()
    data = response.json()
    # Parse the JSON to obtain the quote text.
    quote = data["quote"]
    # Display the quote in the canva's quote_text widget.
    canvas.itemconfig(quote_text, text=quote, fill='black')
        
# Resultado Angela
# def get_quote_angela():
#     response = requests.get("https://api.kanye.rest/")
#     response.raise_for_status()
#     data = response.json()
#     quote = data["quote"]
#     canvas.itemconfig(quote_text , text=quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="C:\\Users\\Gustavo\\Documents\\codigo\\100DaysOfCode\\seccion33\\appKanye\\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="C:\\Users\\Gustavo\\Documents\\codigo\\100DaysOfCode\\seccion33\\appKanye\\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
get_quote()

window.mainloop()



