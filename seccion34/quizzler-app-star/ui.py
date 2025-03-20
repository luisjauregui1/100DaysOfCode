from tkinter import *

THEME_COLOR = "#375362"
IMAGE_TRUE = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion34/quizzler-app-star/images/true.png"
IMAGE_FALSE = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion34/quizzler-app-star/images/false.png"


class QuizInterface:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler") 
        
        # Configuracion de la venta
        self.window.config(padx=30,pady=30, bg=THEME_COLOR)

        # Texto Score
        self.score = Label(text="Score: 0", fg="white", font=("Arial", 18, "italic"), bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        # Cuadro de preguntas (Canvas)
        self.canvas = Canvas(self.window, width=400, height=300)
        self.question_text = self.canvas.create_text(
            200,
            150,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    
        # Boton con true_img (palomita)
        self.true_img = PhotoImage(file=IMAGE_TRUE)
        self.true_botton = Button(image=self.true_img, highlightthickness=0, bg=THEME_COLOR)
        self.true_botton.grid(row=2, column=0)
        
        # imagen con false_img (tache)
        self.false_img = PhotoImage(file=IMAGE_FALSE)
        self.false_botton = Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR)
        self.false_botton.grid(row=2, column=1)
        
                
        self.window.mainloop()