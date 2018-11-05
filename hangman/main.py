from controller import Controller
from view import View
from model import Model

def Main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    while True:
        if controller.getLife() > 0:
            while True:
                controller.UpdateView(controller.getImage(), controller.getBlankToAnswer(), controller.getUsedChar())
                inputChar = controller.inputChar()
                if controller.isUsed(inputChar) == False and inputChar != -1:
                    controller.addUsedChar(inputChar)
                    if controller.isCorrect(inputChar) == True:
                        controller.FillBlank(inputChar)
                        if controller.isComplete():
                            controller.UpdateView(controller.getImage(), controller.getBlankToAnswer(),
                                                  controller.getUsedChar())
                            controller.printSuccess()
                            return 0
                        else:
                            break
                    else: # 입력한 문자가 정답에 없는 경우
                        controller.downLife()
                        break

                else: # 이미 사용한 문자인 경우 또는 입력된 문자가 잘못된 경우
                    continue
            continue
        else:
            controller.UpdateView(controller.getImage(), controller.getBlankToAnswer(), controller.getUsedChar())
            controller.printFail()
            controller.printAnswer(controller.getAnswer())
            break

if __name__ == '__main__':
    Main()