class PointController:
    def __init__(self):
        self.__points = []

    def addPoint(self, point):
        print(point)
        self.__points.append(point)

    def deletePoint(self, index):
        if self.getSize() != 0 and index < self.getSize() and index >= 0:
            self.__points.pop(index)
    def getPoint(self, index):
        if self.getSize() == 0:
            return None
        return self.__points[index]
    def getSize(self):
        return len(self.__points)