
class View:



    def __init__(self):
        pass


    def UpdateView(self, image, blankToAnswer, usedChar):
        print(image)
        print("Current : ", end='')
        print(blankToAnswer)
        print("Already Used : ", end='')
        print(usedChar)

    def printFail(self):
        print("Fail!")

    def printSuccess(self):
        print("Success!")

    def printAnswer(self, answer):
        print("Answer : " + answer)

