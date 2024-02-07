from Snake_Game.Point2D import *

dirictions = ["NONE", "UP", "DOWN", "LEFT", "RIGHT"]

class Snake:
    def __init__(self):
        self._snakeArray = []
        self._headSymbol = "$"
        self._symbol = "+"
        self._size = 1
        self._directionOfMovement = dirictions[0]

    def getSnakeArray(self):
        return self._snakeArray

    def getHeadSymbol(self):
        return self._headSymbol

    def getBodySymbol(self):
        return self._symbol

    def getSize(self):
        return self._size

    def getDirectionOfMovement(self):
        return self._directionOfMovement

    def addNewHead(self, coordinateX, coordinateY):
        self._snakeArray.insert(0, Point2D(coordinateX, coordinateY))
        self._snakeArray.pop()

    def setDirectionOfMovement(self, newDirection):
        self._directionOfMovement = newDirection

    # def setSnakeOnField(self, fieldOBJ):
    #     fieldOBJ[self._CoordinateX][self._CoordinateY] = self._headSymbol

    def move(self, fieldOBJ):
        # if self._directionOfMovement == dirictions[1]: # UP
        #     if 0 <= self._CoordinateY - 1:
        #         self._CoordinateY -= 1
        #     else:
        #         self._CoordinateY = fieldOBJ.getFieldSize() - 1
        # elif self._directionOfMovement == dirictions[2]: # DOWN
        #     if self._CoordinateY + 1 < fieldOBJ.getFieldSize():
        #         self._CoordinateY += 1
        #     else:
        #         self._CoordinateY = 0
        # elif self._directionOfMovement == dirictions[3]: # LEFT
        #     if 0 <= self._CoordinateX - 1:
        #         self._CoordinateX -= 1
        #     else:
        #         self._CoordinateX = fieldOBJ.getFieldSize() - 1
        # elif self._directionOfMovement == dirictions[4]: # RIGHT
        #     if self._CoordinateX + 1 < fieldOBJ.getFieldSize():
        #         self._CoordinateX += 1
        #     else:
        #         self._CoordinateX = 0

        if self._directionOfMovement == dirictions[1]: # UP
            if 0 <= self._snakeArray[0].getCoordinateY - 1:
                self._snakeArray[0].setCoordinateY(self._snakeArray[0].getCoordinateY - 1)
            else:
                self._snakeArray[0].setCoordinateY(fieldOBJ.getFieldSize() - 1)
        elif self._directionOfMovement == dirictions[2]: # DOWN
            if self._snakeArray[0].getCoordinateY + 1 < fieldOBJ.getFieldSize():
                self._snakeArray[0].setCoordinateY(self._snakeArray[0].getCoordinateY + 1)
            else:
                self._snakeArray[0].setCoordinateY(0)
        elif self._directionOfMovement == dirictions[3]: # LEFT
            if 0 <= self._snakeArray[0].getCoordinateX - 1:
                self._snakeArray[0].setCoordinateX(self._snakeArray[0].getCoordinateX - 1)
            else:
                self._snakeArray[0].setCoordinateX(fieldOBJ.getFieldSize() - 1)

        elif self._directionOfMovement == dirictions[4]: # RIGHT
            if self._snakeArray[0].X + 1 < fieldOBJ.getFieldSize():
                self._snakeArray[0].setCoordinateX(self._snakeArray[0].getCoordinateX + 1)
            else:
                self._snakeArray[0].setCoordinateX(0)
        else:
            print("Invalid direction given!")