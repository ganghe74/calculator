from model import Model
from view import hangmanObserver, currentWordObserver, guessedCharsObserver, messageObserver



class Controller:
    def __init__(self):
        self.model = Model()
        self.observer_hangman = hangmanObserver()
        self.observer_current_word = currentWordObserver()
        self.observer_guessed_chars = guessedCharsObserver()
        self.observer_message = messageObserver()
        self.model.register(self.observer_hangman, self.observer_current_word, self.observer_guessed_chars
                            , self.observer_message)
        print("initialized")

    # 추측을 1회 시행
    # 에러나면 return False
    def guess(self, char):
        # 1글자가 아니면 에러출력, return False
        if len(char) != 1:
            self.view.printError("One character at a time!")
            return False

        # 이미 추측한 문자인 경우 에러출력, return False
        if char in self.model.guessedChars:
            self.view.printError("You already guessed \"" + char + "\"")
            return False

        self.model.addGuessedChar(char)

        # 문자를 맞추면 model.currentStatus 의 공백을 채움
        # 못맞추면 numTries증가
        if char in self.model.secretWord:
            self.model.fillBlank(char)
        else:
            self.model.incNumTries()
        return True

if __name__ == '__main__':
    controller = Controller()