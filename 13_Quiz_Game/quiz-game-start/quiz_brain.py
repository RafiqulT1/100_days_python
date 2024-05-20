class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q1{self.question_number}: {current_question.text} (True / False)?\n")



    
    