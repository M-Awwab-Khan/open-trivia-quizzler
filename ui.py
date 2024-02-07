THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text='Score: 0', font=('SF Pro Display', 15, 'normal'), bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        self.question_canvas = Canvas(bg='white', height=250, width=300)
        self.question_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.question_canvas.create_text(150, 125, text='Amazon acquired Twitch in August 2014 for $970 million dollars.', font=('SF Pro Display', 20, 'italic'), width=270)
        self.show_next_question()
        correct_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        self.correct_button = Button(image=correct_img, command= lambda x='True': self.fetch_answer(x))
        self.correct_button.grid(row=2, column=0, padx=20, pady=20)
        self.wrong_button = Button(image=false_img, command=lambda x='False': self.fetch_answer(x))
        self.wrong_button.grid(row=2, column=1, padx=20, pady=20)


        self.window.mainloop()
    def show_next_question(self):
        if self.quiz.still_has_questions():
            self.question_canvas.config(bg='white')
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.\n Thanks for playing.')
            self.correct_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def fetch_answer(self, user_answer):
        is_true = self.quiz.check_answer(user_answer)
        self.give_feedback(is_true)
        self.window.after(1000, self.show_next_question)

    def give_feedback(self, is_true):
        if is_true:
            self.question_canvas.config(bg='green')
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.question_canvas.config(bg='red')