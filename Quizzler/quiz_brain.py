import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Returns a boolean after checking if there is/are question(s) left to be answered """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Gets the next question in the question database (question data list)"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        #  Used html.unescape to decode all html encodings in the questions
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """Checks the answer provided and returns a boolean to denote right or wrong as True or False"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

