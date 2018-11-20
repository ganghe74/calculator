#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from observer.observer import Observer


class hangmanView(QTextEdit):
    def __init__(self):
        QTextEdit.__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignLeft)
        font = self.font()
        font.setFamily('Courier New')
        self.setFont(font)
        self.setText("hangmanView")


class hangmanObserver(Observer):
    def __init__(self):
        pass

    def update(self, model):
        self.hangmanView.setText(model.hangmanList[6 - model.numTries])


class currentWordView(QLineEdit):
    def __init__(self):
        QLineEdit.__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setPointSize(font.pointSize() + 8)
        self.setFont(font)
        self.setText("currentWordView")

class currentWordObserver(Observer):
    def __init__(self):
        pass

    def update(self, model):
        self.currentWordView.setText(model.currentStatus)


class guessedCharsView(QLineEdit):
    def __init__(self):
        QLineEdit.__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignLeft)
        self.setMaxLength(52)
        self.setText("guessedCharsView")


class guessedCharsObserver(Observer):
    def __init__(self):
        pass

    def update(self, model):
        self.guessedCharsView.setText(model.guessedChars)


class messageView(QLineEdit):
    def __init__(self):
        QLineEdit.__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignLeft)
        self.setMaxLength(52)
        self.setText("messageView")


class messageObserver(Observer):
    def __init__(self):
        pass

    def update(self, model):
        self.messageView.setText("미구현")

class Layout(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        # Hangman display window
        self.hangmanWindow = hangmanView()

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = currentWordView()
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = guessedCharsView()
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = messageView()
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        #self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        #self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = Layout()
    game.show()
    sys.exit(app.exec_())