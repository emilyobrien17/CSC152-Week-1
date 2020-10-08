from random import randint


class MultiplicationGame:
    # Initialize 4 class properties
    randomNumbers = [0, 0]
    answer = 0
    userAnswer = 0
    attempts = 0

    # Get Random Numbers
    def getRandomNumbers(self):
        self.randomNumbers[0] = randint(1, 12)
        self.randomNumbers[1] = randint(1, 12)

    # Set Answer to Question
    def setAnswer(self):
        self.answer = self.randomNumbers[0] * self.randomNumbers[1]

    # Begin the game
    def mult(self):
        # Setup random numbers and answer
        self.getRandomNumbers()
        self.setAnswer()
        while True:
            print(self.randomNumbers[0], " times ",  self.randomNumbers[1])
            self.userAnswer = eval(input("What is the answer? "))
            self.attempts = self.attempts + 1
            if self.userAnswer == self.answer:
                print("Correct!")
                print("Number of tries ", self.attempts)
                break


def main():
    multGame = MultiplicationGame()
    multGame.mult()


main()