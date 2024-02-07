from tkinter import Tk, Label, Button, Entry
from MVC.Controller.PointController import PointController
from MVC.Model.Point2D import Point2D

class TkView:
    def __init__(self):
        self.__controller = PointController()

        # test data
        # self.__controller.addPoint(Point2D(4, 4))
        # self.__controller.addPoint(Point2D(5, 4))
        # self.__controller.addPoint(Point2D(4, 5))
        # test data END

        self.__root = Tk()
        self.__root.geometry("200x400")
        self.__root.configure(background="gray")

        Label(text="Enter coordinate X:").pack()
        self.__entryField1 = Entry()
        self.__entryField1.pack()

        Label(text="Enter coordinate Y:").pack()
        self.__entryField2 = Entry()
        self.__entryField2.pack()

        self.__addBtn = Button(text="Add", command=self.btnAddClick)
        self.__addBtn.pack()

        # self.__deleteBtn = Button(text="X", command=self.btnDeleteClick)
        # self.__deleteBtn.pack()

        self.__array = []

        self.__root.mainloop()

    def btnAddClick(self):
        XCoordinate = self.__entryField1.get()
        YCoordinate = self.__entryField2.get()
        if XCoordinate and YCoordinate:
            self.__controller.addPoint(Point2D(XCoordinate, YCoordinate))
            label = Label(text=self.__controller.getPoint(self.__controller.getSize() - 1)).pack()
            self.__array.append(label)
            Button(text="X", command=self.btnDeleteClick).pack()

    def btnDeleteClick(self):
        self.__controller.deletePoint(self.__controller.getSize() - 1)
        self.__array.pop(len(self.__array) - 1)
        self.__root.update()

    def show(self):
        # l1 = Label(text=self.controller.getPoint(2))
        # l1.pack()

        for i in range(self.__controller.getSize()):
            # lTmp = Label(text=self.controller.getPoint(i))
            # lTmp.pack()
            Label(text=self.controller.getPoint(i)).pack()

        self.__root.update()