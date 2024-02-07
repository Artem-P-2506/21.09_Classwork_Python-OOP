import os

class Sneakers:
    def __init__(self, brandName, model, color, size, laces, sole):
        self._brandName = brandName
        self._model = model
        self._color = color
        self._size = size
        self._laces = laces
        self._sole = sole

    def getBrandName(self):
        return self._brandName

    def getModel(self):
        return self._model

    def getColor(self):
        return self._color

    def getSize(self):
        return self._size

    def getLaces(self):
        return self._laces

    def getSole(self):
        return self._sole

    def showCharacteristics(self):
        return f"Brand:\t{str(self._brandName)}\nModel:\t{str(self._model)}" + \
            f"\nColor:\t{str(self._color)}\nSize:\t{str(self._size)}" + \
            f"\nLaces:\t{str(self._laces)}\nSole:\t{str(self._sole)}"