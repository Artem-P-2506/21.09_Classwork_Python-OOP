class Point2D:
    def __init__(self, x, y):
        self.__xCoordinate = x
        self.__yCoordinate = y

    def getX(self):
        return self.__xCoordinate

    def setX(self, newX):
        self.__xCoordinate = newX

    def getY(self):
        return self.__yCoordinate

    def setY(self, newY):
        self.__yCoordinate = newY