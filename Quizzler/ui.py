from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=270, text="", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_is_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Gets the next question when the true/false button is clicked on the GUI"""
        self.canvas.config(bg="white")  # Changes the canvas background color to white as it brings forth a new question

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_is_true(self):
        """Connected to the true button hence give user answer as true when the button is pushed"""
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def answer_is_false(self):
        """Connected to the false button hence give user answer as false when the button is pushed"""
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, answer_is_right):
        """Changes the background color of the canvas to either red or green based on the answer given by the user"""
        if answer_is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Automatically goes to the next question after 1second of taking user answer and providing feedback
        self.window.after(1000, self.get_next_question)

