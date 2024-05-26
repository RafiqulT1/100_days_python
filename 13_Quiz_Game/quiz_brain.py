class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def ask_question(self):
        """Get questions objects from question_bank list and
        ask user if the question is True or False """

        current_question = self.question_list[self.question_number]
        q_num = self.question_number + 1
        user_answer = input(f"Q.{q_num}: {current_question.question} (True / False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        - Check if user answer is right or wrong
        - Count user score
        """

        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number+1}")
        print("\n")


    def questions_left(self):
        """Check if all question has been asked"""
        return len(self.question_list) == self.question_number

