class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0


    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
         print('-' + q)

        answer = input("Cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
   
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Skor: {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f"{questionNumber} / {totalQuestion}".center(50, '*'))

q1 = Question("en iyi programlama dili?", ['C#', 'python', 'javascript', 'java'], 'python')
q2 = Question("en popüler programlama dili?", ['javascript','C#', 'python', 'java'], 'python')
q3 = Question("en çok tercih edilen programlama dili?", ['python', 'C#', 'javascript', 'java'], 'python')
questions = [q1, q2, q3]

quiz = Quiz(questions)
question = quiz.loadQuestion()