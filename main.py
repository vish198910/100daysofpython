from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(text=question["text"],answer=question["answer"]))

quiz = QuizBrain(queston_list=question_bank)
quiz.next_question()