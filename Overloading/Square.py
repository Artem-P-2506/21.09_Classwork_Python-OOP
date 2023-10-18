from Overloading.Figure import *

class Square(Figure):
    def __init__(self, color, material, coordinatesOBJ, sideSize):
        super().__init__(color, material, coordinatesOBJ)
        self._sideSize = sideSize

    def getSideSize(self):
        return self._sideSize

    def setSideSize(self, newSideSize):
        self._sideSize = newSideSize

    def __str__(self):
        return super().__str__() + "\nSize of side:\t" + str(self._sideSize)