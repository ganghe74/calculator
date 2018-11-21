import model
import view
import controller

model = model.Model()
view = view.Layout(view.game)
controller = controller.Controller(model, view)

while not model.isFinished():
    view.printHangman()
    char = view.inputChar()
    controller.guess(char)

if model.isSuccess():
    view.printSuccess()
elif model.isFail():
    view.printFail()
else:
    view.printError("Game Finished with unknown error")