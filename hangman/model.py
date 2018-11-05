from hangman import Hangman
from word import Word


class Model:

    ImageList = []
    UsedChar = []
    BlankToAnswer = []
    Answer = ''


    def __init__(self):
        word = Word('words.txt')
        self.ImageList = Hangman.text
        self.UsedChar = []
        self.Answer = word.randFromDB()
        for letter in range(len(self.Answer)):
            self.BlankToAnswer.append('_')
        print("Model initiate end")
        print("Answer Length: " + str(len(self.BlankToAnswer)))


    def downLife(self):
        del self.ImageList[-1]

    def FillBlank(self, char):
        CorrectIndex = []
        for i in range(len(self.Answer)):
            if char == self.Answer[i]:
                CorrectIndex.append(i)
                continue
        for j in CorrectIndex:
            self.BlankToAnswer[j] = char

    def addUsedChar(self, char):
        self.UsedChar.append(char)
