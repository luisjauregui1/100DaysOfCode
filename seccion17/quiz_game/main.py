from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for i in range(len(question_data)):
    new_q = Question(question_data[i]['question'], question_data[i]['correct_answer'])
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    valor=quiz.next_question()



print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")