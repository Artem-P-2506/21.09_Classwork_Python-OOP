class Line:
    def __init__(self, pointA, pointB):
        self.__pointA = pointA
        self.__pointB = pointB

    def getPointA(self):
        return self.__pointA.getX(), self.__pointA.getY()

    def setPointA(self, newX, newY):
        self.__pointA.setX(newX)
        self.__pointA.setY(newY)

    def getPointB(self):
        return self.__pointB.getX(), self.__pointB.getY()

    def setPointB(self, newX, newY):
        self.__pointB.setX(newX)
        self.__pointB.setY(newY)

    def show(self):
        print(f"Точка 'A': {self.getPointA()}" +
              f"\nТочка 'B': {self.getPointB()}")