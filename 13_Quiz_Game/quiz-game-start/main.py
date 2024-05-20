from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# q1 = Question(q1, a1)
for data in question_data:
    question = data["text"]
    answer = data["answer"]
    new_ques_and_ans = Question(q_text=question, q_answer=answer)
    question_bank.append(new_ques_and_ans)
    
quiz = QuizBrain(question_bank)
quiz.next_question()


#     print(question_data[i])
# print(question_data[1])
    # q_&_a = Question()
    