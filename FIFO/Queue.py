class Queue:
    def __init__(self):
        self.__firstElement = None

    def push(self, elementOBJ):
        if not self.__firstElement:
            self.__firstElement = elementOBJ
        else:
            curentElement = self.__firstElement
            # while(True):
            #     if curentElement.getNextElement():
            #         curentElement = curentElement.getNextElement()
            #     else:
            #         curentElement.setNextElement(elementOBJ)
            #         break
            while(curentElement.getNextElement()):
                curentElement = curentElement.getNextElement()
            curentElement.setNextElement(elementOBJ)

    def pop(self):
        element = self.__firstElement
        if element:
            self.__firstElement = element.getNextElement()
        return element