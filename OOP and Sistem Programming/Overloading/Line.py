from Overloading.Figure import *


class Line(Figure):
    def __init__(self, color, material, coordinatesOBJ, length):
        super().__init__(color, material, coordinatesOBJ)
        self._length = length

    def getLength(self):
        return self._length

    def setLength(self, newLength):
        self._length = newLength

    def __str__(self):
        return super().__str__() + "\nLength:\t" + str(self._length)