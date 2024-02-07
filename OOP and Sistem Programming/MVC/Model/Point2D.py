class Point2D:
    def __init__(self, x, y):
        self._coordX = x
        self._coordY = y

    def getX(self):
        return self._coordX
    def getY(self):
        return self._coordY

    def __str__(self):
        return f"{self._coordX} : {self._coordY}"