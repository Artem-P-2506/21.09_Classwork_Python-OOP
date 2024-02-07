class Banknote:
    def __init__(self, material, color, denomination, year, form):
        self._material = material
        self._color = color
        self._denomination = denomination
        self._year = year
        self._form = form

    def getMaterial(self):
        return self._material

    def getColor(self):
        return self._color

    def getDenomination(self):
        return self._denomination

    def getYear(self):
        return self._year

    def getForm(self):
        return self._form