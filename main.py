# class Key:
#     def __init__(self, teeth, size, material, color):
#         self.__teeth = teeth
#         self.__size = size
#         self.__material = material
#         self.color = color
#
#     def getTeeth(self):
#         return self.__teeth
#
#     def getSize(self):
#         return self.__size
#
#     def setSize(self, size):
#         self.__size = size
#
#     def getMaterial(self):
#         return self.__material
#
#     def showCharacteristics(self):
#         print("Number of teeth:" + str(self.getTeeth()) + "\nSize:" + str(self.getSize())
#               + "\nMaterial:" + str(self.getMaterial()) + "\nColor:" + str(self.color))
#
#     def openLock(self):
#         print("Lock was opened with key! \n(Number of teeth and size:\t" +
#               str(self.getTeeth()) + ",\t" + str(self.__size) + ")")
#
# if __name__ == "__main__":
#     key = Key(12, 50, "iron", "red")
#     key.showCharacteristics()
#     key.openLock()
#     print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#     key.setSize(80)
#     key.color = "black"
#     key.showCharacteristics()
#     key.openLock()
#
#
#==========================================================================================================================================================================================
# import os
#
# def writeNumbers(usersArray):
#     with open("file.txt", "w") as file:
#         for number in usersArray:
#             file.write(str(usersArray[number-1]))
#             file.write(",")
#
# def readNumbers():
#     with open("file.txt", "r") as file:
#         data = file.readline()
#         data = data.split(",")
#         array = []
#         sum = 0
#         for item in data:
#             array.append(item)
#         for item in array:
#             sum += int(item)
#         return sum
#
#
#
# if __name__ == "__main__":
#     array = []
#     for i in range(7):
#         number = int(input("Write number #%i: " % (i + 1)))
#         array.append(number)
#     writeNumbers(array)
#     print(str(readNumbers()))
#
#
#==========================================================================================================================================================================================
# import os
#
# if __name__ == "__main__":
#     filesInDir = os.listdir(os.getcwd())
#     i = 1
#     for item in filesInDir:
#         if os.path.isfile(item):
#             print("File #" + str(i) + ": " + str(item))
#             i += 1
#
#     if not os.path.exists("TEKCTA"):
#         root = os.getcwd()
#         os.mkdir("TEKCTA")
#         for item in filesInDir:
#             if os.path.isfile(item):
#                 with open(item, "r") as oldFile:
#                     temp = oldFile.read()
#                     os.chdir("TEKCTA")
#                     with open(item, "w") as newFile:
#                         newFile.write(temp)
#                 os.chdir(root)
#                 os.rmdir(item)
#
#
#==========================================================================================================================================================================================
# import os
# import SecondSkript
# from Banknote import *
# from SecondSkript import *
#
# if __name__ == "__main__":
#
#
#
#             SecondSkript.isBanknote()
#
#
#==========================================================================================================================================================================================
#class Banknote:
#     def __init__(self, material, color, xSize, ySize, denomination, year, serialNumber, waterStamp , facialPicture, backPicture):
#         self.__material = material
#         self.__color = color
#         self.__xSize = xSize
#         self.__ySize = ySize
#         self.__denomination = denomination
#         self.__year = year
#         self.__serialNumber = serialNumber
#         self.__waterStamp = waterStamp
#         self.__facialPicture = facialPicture
#         self.__backPicture = backPicture
#
#     def getMaterial(self):
#         return self.__material
#
#     def getColor(self):
#         return self.__color
#
#     def getXSize(self):
#         return self.__xSize
#
#     def getYSize(self):
#         return self.__ySize
#
#     def getDenomination(self):
#         return self.__denomination
#
#     def getYear(self):
#         return self.__year
#
#     def getSeriealNumber(self):
#         return self.__serialNumber
#
#     def getWaterStamp(self):
#         return self.__waterStamp
#
#     def getFacialPicture(self):
#         return self.__facialPicture
#
#     def getBackPicture(self):
#         return self.__backPicture
#
#     def print(self):
#         print("\nМатериал:\t" + str(self.getMaterial()) + "\nЦвет:\t" + str(self.getColor()) +
#               "\nРазмер_X:\t" + str(self.getXSize()) + "мм" + "\nРазмер_Y:\t" + str(self.getYSize()) + "мм" +
#               "\nНоминал:\t" + str(self.getDenomination()) + "\nГод выпуска:\t" + str(self.getYear()) +
#               "\nСерийный номер:\t" + str(self.getSeriealNumber()) + "\nВодная марка:\t" + str(self.getWaterStamp()) +
#               "\nЛицевая картинка:\t" + str(self.getFacialPicture()) + "\nЗадняя картинка:\t" + str(self.getBackPicture()))
#
#
#==========================================================================================================================================================================================
# from Atom import *
# from Point2D import *
# from Line import *
# from Square import *
#
# if __name__ == "__main__":
#     # atom1 = Atom(5, 6, 7, 11.18478, 7)
#     # atom2 = Atom(7, 8, 3, 15.487, 3)
#     # atom3 = Atom(3, 2, 1, 5.7744, 1)
#     # atom1.print()
#     # print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#     # atom2.print()
#     # print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#     # atom3.print()
#
#     pointA = Point2D(0, 0)
#     pointB = Point2D(5, 0)
#     pointC = Point2D(5, -5)
#     pointD = Point2D(0,-5)
#     line1 = Line(pointA, pointB)
#     line2 = Line(pointB, pointC)
#     line3 = Line(pointC, pointD)
#     line4 = Line(pointD, pointA)
#
#     square1 = Square(line1, line2, line3, line4)
#     square1.show()
#
#
#==========================================================================================================================================================================================
from Banknote_Coin_Bill.Coin import *
from Banknote_Coin_Bill.Bill import *

if __name__ == "__main__":
    coin10 = Coin("Bronze", "None", 10, 2009, "round", 15, "True")
    bill100 = Bill("Paper", "Yellow", 100, 2018, "rectangle", 142, 75, "AK12547863", "waterStamp.png", "facialPicture.png", "backPicture.png")

    print("")
    coin10.show()
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    bill100.show()