class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def Next_Question(self):
        self.user_response = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} True/False?: ")
        print(self.user_response)
        self.check_answer(self.user_response, self.question_list[self.question_number].answer)
        self.question_number += 1

    def Still_Has_Questions(self):
        flag = True
        if self.question_number==len(self.question_list):
            flag = False
        return flag

    def check_answer(self, response_1, response_2):
        if response_1 == response_2:
            print("Correct answer!")
            self.score += 1
        else:
            print("Wrong answer!")
        print("Correct answer is "+ response_2)
        print("Score is "+ str(self.score)+"/"+str(self.question_number+1))

