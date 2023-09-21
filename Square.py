class Square:
    def __init__(self, line1, line2, line3, line4):
        self.__line1 = line1
        self.__line2 = line2
        self.__line3 = line3
        self.__line4 = line4

    def getLine1(self):
        return self.__line1.getPointA(), self.__line1.getPointB()

    def setLine1(self, newAX, newAY, newBX, newBY):
        self.__line1.setA(newAX, newAY)
        self.__line1.setB(newBX, newBY)

    def getLine2(self):
        return self.__line2.getPointA(), self.__line2.getPointB()

    def setLine2(self, newAX, newAY, newBX, newBY):
        self.__line2.setA(newAX, newAY)
        self.__line2.setB(newBX, newBY)

    def getLine3(self):
        return self.__line3.getPointA(), self.__line3.getPointB()

    def setLine3(self, newAX, newAY, newBX, newBY):
        self.__line3.setA(newAX, newAY)
        self.__line3.setB(newBX, newBY)

    def getLine4(self):
        return self.__line4.getPointA(), self.__line4.getPointB()

    def setLine4(self, newAX, newAY, newBX, newBY):
        self.__line4.setA(newAX, newAY)
        self.__line4.setB(newBX, newBY)

    def show(self):
        print(f"\n\tЛиния №1:")
        self.__line1.show()
        print(f"\n\tЛиния №2:")
        self.__line2.show()
        print(f"\n\tЛиния №3:")
        self.__line3.show()
        print(f"\n\tЛиния №4:")
        self.__line4.show()