class Element:
    def __init__(self, value):
        self.__value = value
        self.__nextElement = None

    def getValue(self):
        return self.__value

    def getNextElement(self):
        return self.__nextElement

    def setValue(self, newValue):
        self.__value = newValue

    def setNextElement(self, newNextElement):
        self.__nextElement = newNextElement