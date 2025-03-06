class Bot:
    def __init__(self):
        self.question = ""
        self.answer = ""

    def set_question(self, question, answer):
        self.question = question
        self.answer = answer

    def get_question(self):
        return self.question

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()
