
class Controller:

    ErrorMessage = ''
    char = ''
    Alphabet = "q w e r t y u i o p a s d f g h j k l z x c v b n m".split()

    def __init__(self, model, view):
        self.model = model
        self.view = view


    def getLife(self):
        return len(self.model.ImageList) - 1

    def getImage(self):
        return self.model.ImageList[-1]

    def getUsedChar(self):
        return self.model.UsedChar

    def getBlankToAnswer(self):
        return self.model.BlankToAnswer

    def getErrorMessage(self):
        return self.ErrorMessage

    def getInputedChar(self):
        return self.char

    def getAnswer(self):
        return self.model.Answer

    def inputChar(self):
        self.char = input("Select a Letter : ")
        if self.char not in self.Alphabet: # 정해진 포맷 입력이 아닌 경우
            return -1 # -1을 반환
        return self.char


    def isUsed(self, char):
        for k in self.model.UsedChar:
            if k == char:
                return True
        return False

    def isCorrect(self, char):
        for l in range(len(self.model.Answer)):
            if char == self.model.Answer[l]:
                return True
        return False

    def isComplete(self):
        for m in self.model.BlankToAnswer:
            if m == '_':
                return False
        return True

    def FillBlank(self, char):
        self.model.FillBlank(char)

    def UpdateView(self, image, blankToAnswer, usedChar):
        self.view.UpdateView(image, blankToAnswer, usedChar)

    def downLife(self):
        self.model.downLife()

    def addUsedChar(self, char):
        self.model.addUsedChar(char)

    def printFail(self):
        self.view.printFail()

    def printSuccess(self):
        self.view.printSuccess()

    def printAnswer(self, answer):
        self.view.printAnswer(answer)





