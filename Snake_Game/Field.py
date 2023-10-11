class Field:
    def __init__(self):
        self._sizeX = 0
        self._sizeY = 0
        self._field = self.__makeField()

    def getSizeX(self):
        return self._sizeX

    def getSizeY(self):
        return self._sizeY

    def setSnake(self, xCoordinate, yCoordinate, symbol):
        self._field[xCoordinate][yCoordinate] = symbol


    def __makeField(self):
        self._sizeY = int(input("Введите количесво рядков у поля: "))
        self._sizeX = int(input("Введите количесво колонок у поля: "))
        tempArray = []
        for i in range(self._sizeY):
            tempArray.append([])
            for j in range(self._sizeX):
                tempArray[i].append(".")
        return tempArray

    def _showField(self):
        print("\n=> ПОЛЕ:")
        for row in self._field:
            for column in row:
                print("\t\t", str(column), end="")
            print("\n")
    def getField(self):
        return self._field