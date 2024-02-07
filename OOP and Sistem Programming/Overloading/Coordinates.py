class Coordinates:
    def __init__(self, coordinateX, coordinateY):
        self._coordinateX = coordinateX
        self._coordinateY = coordinateY

    def getCoordinateX(self):
        return self._coordinateX

    def getCoordinateY(self):
        return self._coordinateY

    def setCoordinateX(self, newCoordinateX):
        self._coordinateX = newCoordinateX

    def setCoordinateY(self, newCoordinateY):
        self._coordinateY = newCoordinateY