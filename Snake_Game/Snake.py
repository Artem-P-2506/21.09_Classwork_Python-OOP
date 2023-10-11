class Snake:
    def __init__(self):
        self._headSimbol = "$"
        self._simbol = "+"
        self._size = 1
        self._directionOfMovement = "NONE"

    def getHeadSimbol(self):
        return self._headSimbol

    def getSimbol(self):
        return self._simbol

    def getSize(self):
        return self._size

    def getDirectionOfMovement(self):
        return self._directionOfMovement