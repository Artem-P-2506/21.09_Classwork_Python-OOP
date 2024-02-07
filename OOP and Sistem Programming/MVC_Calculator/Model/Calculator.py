# ACTIONS = ("ADD", "SUBTRACT", "MULTIPLY", "DIVIDE")
ACTIONS = ("+", "-", "*", "/")

class Calculator:
    def __init__(self, firstNumber, secondNumber, action):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
        self.action = action

    def countUp(self):
        if self.action == ACTIONS[0]:
            return float(self.firstNumber) + float(self.secondNumber)
        if self.action == ACTIONS[1]:
            return float(self.firstNumber) - float(self.secondNumber)
        if self.action == ACTIONS[2]:
            return float(self.firstNumber) * float(self.secondNumber)
        if self.action == ACTIONS[3]:
            if not self.secondNumber == 0:
                return float(self.firstNumber) / float(self.secondNumber)
            else:
                return ValueError("Деление на ноль не допусимо!")
        else:
            return ValueError("Неверная операция действия!")