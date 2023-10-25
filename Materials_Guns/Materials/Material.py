class Material:
    def __init__(self, materialType, color, weight):
        self._materialType = materialType
        self._color = color
        self._weight = weight

    def getMaterialType(self):
        return self._materialType

    def getWeight(self):
        return self._weight

    def getColor(self):
        return self._color

    def __str__(self):
        return f"Marerial:\t{str(self._materialType)}\nColor:\t{str(self._color)}\nWeight:\t{str(self._weight)}"