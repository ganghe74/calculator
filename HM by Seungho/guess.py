class Guess:


    def __init__(self, word):
        self.guessedChars=[]
        self.currentStatus=''
        self.useAlphabet=[]
        self.secretWord=word
        self.currentStatusList = []
        self.count=0
        for i in range(len(word)):
            self.currentStatusList.append('_')
        self.numTries=0
        self.secretWordList=[]
        for i in range(len(self.secretWord)):
            self.secretWordList.append(self.secretWord[i])

    def display(self):
        for i in range(len(self.secretWord)):
            print(self.currentStatusList[i],end=" ")
            if i==len(self.secretWord)-1:
                print("")
        print(self.numTries)
        print("Used alphabet: ",end="")
        print(self.guessedChars)



    def guess(self, character):
        self.count=0
        check=True
        if character in self.guessedChars:
            check=True
        else:

            self.guessedChars.append(character)
            if character==str(0):
                self.guessedChars.pop()

        for i in range(len(self.secretWordList)):
            if self.secretWordList[i]==character:
                self.currentStatusList[i]=character
                check=False
                continue
            elif character==str(0):
                check=False
            else:
                continue

        if check == True:

            self.numTries+=1








        if '_' in self.currentStatusList:
            False
        else:
            for i in range(len(self.currentStatusList)):
                self.currentStatus+=self.currentStatusList[i]

            return True



