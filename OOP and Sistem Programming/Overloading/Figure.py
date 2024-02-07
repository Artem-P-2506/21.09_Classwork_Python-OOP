class Figure:
    def __init__(self, color, material, coordinatesOBJ):
        self._color = color
        self._material = material
        self._coordinates = coordinatesOBJ

    def getColor(self):
        return self._color

    def getMaterial(self):
        return self._material

    def getCoordinates(self):
        return self._coordinates.getCoordinateX(), self._coordinates.getCoordinateY()

    def setCoordinates(self, newCoordinateX, newCoordinateY):
        self._coordinates.setCoordinateX(newCoordinateX)
        self._coordinates.setCoordinateY(newCoordinateY)

    def setColor(self, newColor):
        self._color = newColor

    def setMaterial(self, newMaterial):
        self._material = newMaterial

    def __str__(self):
        return "Color:\t" + str(self._color) + "\nMaterial:\t" + str(self._material) + "\nCoordinates:\t" + str(self.getCoordinates())