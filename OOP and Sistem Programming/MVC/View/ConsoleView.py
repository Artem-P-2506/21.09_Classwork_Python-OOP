from MVC.Controller.PointController import PointController
from MVC.Model.Point2D import Point2D

class ConsoleView:
    def __init__(self):
        self.__controller = PointController()

        self.__controller.addPoint(Point2D(4, 4))
        self.__controller.addPoint(Point2D(5, 4))
        self.__controller.addPoint(Point2D(4, 5))

    def show(self):
        print(self.__controller.getPoint(2))