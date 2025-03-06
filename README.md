import pytest

class Bot:
    def __init__(self):
        self.question = ""
        self.answer = ""

    def set_question(self, question):
        self.question = question

    def get_question(self):
        return self.question

    def check_answer(self, user_answer):
        return user_answer == self.answer
        
def bot():
    return Bot()

def test_question(bot):
    bot.set_question("What is 2 + 2?")
    assert bot.get_question() == "What is 2 + 2?"

def test_answer(bot):
    bot.answer = "4"
    assert bot.check_answer("4") is True
    assert bot.check_answer("5") is False
