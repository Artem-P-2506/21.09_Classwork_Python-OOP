class CalculatorController:
    def __init__(self):
        self.__calculators = []

    def addCalculator(self, calculatorOBJ):
        self.__calculators.append(calculatorOBJ)

    def deleteCalculator(self, index):
        if self.getSize() != 0 and index < self.getSize() and index >= 0:
            self.__calculators.pop(index)

    def getCalculator(self, index):
        if self.getSize() == 0 or index >= self.getSize() or index < 0:
            return None
        else:
            return self.__calculators[index]

    def getSize(self):
        return len(self.__calculators)

    def changeValues(self, calculatorIndex, newFirstNumber, newSecondNumber, newAction):
        self.__calculators[calculatorIndex].firstNumber = newFirstNumber
        self.__calculators[calculatorIndex].secondNumber = newSecondNumber
        self.__calculators[calculatorIndex].action = newAction

    def startCountUp(self, calculatorIndex):
        return self.__calculators[calculatorIndex].countUp()