from word import Word
from hangmanList import hangmanList
from observer.observable import Observable


class Model(Observable):
    def __init__(self):
        super().__init__()
        self.word = Word('words.txt')
        self.secretWord = self.word.randFromDB()
        self.__numTries = 0  # 7이되면 gameOver
        self.hangmanList = hangmanList
        self.__currentStatus = "_"*len(self.secretWord)
        self.__guessedChars = ""

    @property
    def numTries(self):
        return self.__numTries

    @property
    def guessedChars(self):
        return self.guessedChars

    @property
    def hamgmanList(self):
        return self.hamgmanList

    @property
    def currentStatus(self):
        return self.__currentStatus

    @numTries.setter
    def numTries(self, num):
        self.__numTries = num
        self.notify()

    def incNumTries(self):
        self.numTries += 1
        self.notify()

    @guessedChars.setter
    def guessedChar(self, char):
        self.__guessedChars += char
        self.notify()

    def fillBlank(self, char):
        for i in range(len(self.secretWord)):
            if self.secretWord[i] == char:
                self.currentStatus = self.currentStatus[:i] + char + self.currentStatus[i+1:]
        self.notify()

    def isSuccess(self):
        if self.secretWord == self.currentStatus:
            return True
        return False

    def isFail(self):
        if self.numTries >= 6:
            return True
        return False

    def isFinished(self):
        return self.isSuccess() or self.isFail()