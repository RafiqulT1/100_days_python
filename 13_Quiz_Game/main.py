from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list to insert question objects
question_bank = []

for q_and_a in question_data:
    """
    - Iterate over the question_data list.
    - create a Question object from each entry in question_data.
    - Append each Question object to the question_bank.
    """
    new_question = Question(q_and_a["text"], q_and_a["answer"])
    question_bank.append(new_question)

# print(question_bank[0].question)


quiz = QuizBrain(question_bank)

while not quiz.questions_left():
    quiz.ask_question()
    quiz.question_number += 1

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
