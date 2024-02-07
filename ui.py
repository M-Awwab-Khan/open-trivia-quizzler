THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text='Score: 0', font=('SF Display', 15, 'normal'), bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        self.question_canvas = Canvas(bg='white', height=250, width=300)
        self.question_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_canvas.create_text(150, 125, text='Amazon acquired Twitch in August 2014 for $970 million dollars.', font=('SF Pro Display', 20, 'italic'), width=270)
        correct_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        self.correct_button = Button(image=correct_img)
        self.correct_button.grid(row=2, column=0, padx=20, pady=20)
        self.wrong_button = Button(image=false_img)
        self.wrong_button.grid(row=2, column=1, padx=20, pady=20)


        self.window.mainloop()