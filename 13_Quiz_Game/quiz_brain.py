class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def ask_question(self):
        q_num = self.question_number
        q_list = self.question_list
        input(f"Q.{q_num + 1}: {q_list[q_num].question} (True / False)").lower()

    def questions_left(self):
        return len(self.question_list) == self.question_number
        #     return True
        # return False
