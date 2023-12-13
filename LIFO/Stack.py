class Stack:
    def __init__(self):
        self.__firstElement = None

    def push(self, elementOBJ):
        if not self.__firstElement:
            self.__firstElement = elementOBJ
        else:
            curentElement = self.__firstElement
            while(curentElement.getNextElement()):
                curentElement = curentElement.getNextElement()
            curentElement.setNextElement(elementOBJ)

    def pop(self):
        if self.__firstElement and not self.__firstElement.getNextElement() == None:
            curentElement = self.__firstElement
            while (curentElement.getNextElement()):
                nextElement = curentElement.getNextElement()
                if not nextElement.getNextElement():
                    break
                curentElement = nextElement
            lastElement = curentElement.getNextElement()
            curentElement.setNextElement(None)
            return lastElement
        else:
            lastElement = self.__firstElement
            if lastElement:
                self.__firstElement = None
            return lastElement