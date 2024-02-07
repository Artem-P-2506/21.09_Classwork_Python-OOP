class Point2D:
    def __init__(self, x, y):
        self.xCoordinate = x
        self.yCoordinate = y

    def __str__(self):
        return f"xCoordinate: {self.xCoordinate}, yCoordinate: {self.yCoordinate}"