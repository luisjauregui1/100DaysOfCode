from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
IMAGE_TRUE = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion34/quizzler-app-star/images/true.png"
IMAGE_FALSE = "C:/Users/Gustavo/Documents/codigo/100DaysOfCode/seccion34/quizzler-app-star/images/false.png"


class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
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
            width=350,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    
        # Boton con true_img (palomita)
        self.true_img = PhotoImage(file=IMAGE_TRUE)
        self.true_botton = Button(image=self.true_img, highlightthickness=0, bg=THEME_COLOR, command=self.true_botton)
        self.true_botton.grid(row=2, column=0)
        
        # imagen con false_img (tache)
        self.false_img = PhotoImage(file=IMAGE_FALSE)
        self.false_botton = Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR, command=self.false_botton)
        self.false_botton.grid(row=2, column=1)
        
        self.get_next_question()
                
        self.window.mainloop()
        
    def get_next_question(self):   
        self.canvas.config(bg='White')
        
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_botton.config(state="disabled")
            self.false_botton.config(state="disabled")
        
    def true_botton(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_botton(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)    
                