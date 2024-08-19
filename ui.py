from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInter:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.user_answer = ""
        self.number = 0
        self.label = Label(text=f"Score:{self.number}", background=THEME_COLOR, foreground="white", font=("Arial", 20, "bold"))
        self.label.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250)
        self.text_question = self.canvas.create_text(150, 125, text="Just text", width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        self.image1 = PhotoImage(file="images/false.png")
        self.image2 = PhotoImage(file="images/true.png")
        self.button1 = Button(image=self.image1, highlightthickness=0, background=THEME_COLOR, padx=25, pady=25, command=self.its_false)
        self.button2 = Button(image=self.image2, highlightthickness=0, background=THEME_COLOR, padx=25, pady=25, command=self.its_true)
        self.button1.grid(row=2, column=1)
        self.button2.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def its_true(self, ):
        self.quiz.check_answer()
        self.quiz.check_answer(user_answer=self.user_answer)
        if self.quiz.check_answer == True:
            self.number += 1
            self.quiz.next_question()

    def its_false(self):
        self.quiz.check_answer()
        self.quiz.check_answer(user_answer=self.user_answer)
        if self.quiz.check_answer == False:
            self.quiz.next_question()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text_question, text=q_text)