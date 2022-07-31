from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for quest in question_data:
    new_quest = Question(quest['text'],quest['answer'])
    question_bank.append(new_quest)

# print(question_bank)

new_quest = QuizBrain(question_bank)

while new_quest.Still_Has_Questions():
    new_quest.Next_Question()

print("Game Ended, your final score "+ str(new_quest.score))