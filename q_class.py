from random import shuffle


class Question:
    def __init__(self, q_text, n_ansewrs, answers_list, pic=False, image=None):
        self.text = q_text
        self.num_of_ansewrs = n_ansewrs
        self.ansewrs = answers_list
        self.image = pic
        if pic:
            self.picture = image

    def mix_question(self):
        temp = [i for i in self.ansewrs]
        shuffle(temp)
        return Question(self.text, self.num_of_ansewrs, temp)


class Test:
    def __init__(self, questions=[]):
        self.question_list = questions

    def add_question(self, new_question):
        self.question_list.append(new_question)

    def mix_test(self):
        temp = [i.mix_question() for i in self.question_list]
        shuffle(temp)
        return Test(temp)
