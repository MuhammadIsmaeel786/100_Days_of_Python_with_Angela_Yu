class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_anwser = input(f"Q.{self.question_number}: {current_question.text} True : False : ")
        self.check_answer(user_anwser, current_question.answer)
    
    def check_answer(self, user_anwser,correct_anwser):
        if user_anwser.lower() == correct_anwser.lower():
            self.score += 1
            print("Correct!")
        else:
            print(f"Sorry, that's wrong. The correct answer was {correct_anwser}")
        print(f"Your Score is {self.score}/{self.question_number}")
        print("\n")