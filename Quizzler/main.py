from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    """Takes questions from the API call in data.py and formats it using the Question class in the question_model.py"""
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)  # Passes the question data to the quiz brain to enable quiz functionality
quiz_ui = QuizInterface(quiz)  # Passes the quiz brian and the question_bank to the quiz GUI for better user experience


