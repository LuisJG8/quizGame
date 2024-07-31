from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for thing in question_data:
    question_text = thing["question"]
    question_answer = thing["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final score is: {quiz.count}/{quiz.question_number}")
