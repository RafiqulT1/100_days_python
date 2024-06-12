class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_num < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1 
        print(f"Q.{self.question_num}. {current_question.text}")
        input("True / False? :")