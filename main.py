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
# from Banknote_Coin_Bill.Coin import *
# from Banknote_Coin_Bill.Bill import *
#
# if __name__ == "__main__":
#     coin10 = Coin("Bronze", "None", 10, 2009, "round", 15, "True")
#     bill100 = Bill("Paper", "Yellow", 100, 2018, "rectangle", 142, 75, "AK12547863", "waterStamp.png", "facialPicture.png", "backPicture.png")
#
#     print("")
#     coin10.show()
#     print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
#     bill100.show()
#
#
#==========================================================================================================================================================================================
# import os
# import threading
#
# def writeInFile(array):
#     with open("file.txt", 'w') as file:
#         for item in array:
#             file.write(str(item) + ",")
#
# if __name__ == "__main__":
#     myArray = []
#     for i in range(1000000):
#         myArray.append(i)
#
#     t1 = threading.Thread(target=writeInFile, args=(myArray, ))
#     t1.start()
#
#
#==========================================================================================================================================================================================
# import threading
# import time
#
# def Timer(hours, minutes, secunds):
#     if (0 <= hours*60 + minutes*60 + secunds ):
#         isTime = True
#         while(isTime):
#             for secund in range(secunds):
#                 print(f"Осталось: {hours}:{minutes}:{secunds-secund}")
#                 time.sleep(1)
#             print(f"Осталось: {hours}:{minutes}:0")
#             time.sleep(1)
#             if minutes != 0:
#                 secunds = 59
#                 minutes -= 1
#                 continue
#             elif hours != 0:
#                 minutes = 59
#                 secunds = 59
#                 hours -= 1
#             else:
#                 isTime = False
#                 print("Время вышло!")
#     else:
#         print("Wrong input!")
#
# def Stopwatch(hours, minutes, secunds):
#     allTimeInSecunds = hours * 60 + minutes * 60 + secunds
#     if (0 <= allTimeInSecunds):
#         isTime = True
#         while (isTime):
#             hoursLeft = 0
#             minutesLeft = 0
#             secundLeft = 0
#             for i in range(allTimeInSecunds):
#                 print(f"Прошло: {hoursLeft}:{minutesLeft}:{secundLeft}")
#                 time.sleep(1)
#                 secundLeft += 1
#
#                 if secundLeft >= 60:
#                     if minutesLeft >= 60:
#                         hoursLeft += 1
#                     else:
#                         minutesLeft += 1
#                         secundLeft = 0
#                 if i >= allTimeInSecunds - 1:
#                     isTime = False
#                     print("Время вышло!")
#     else:
#         print("Wrong input!")
#
#
#
# if __name__ == "__main__":
#     hours = int(input("Введите сколько часов ждать: "))
#     minutes = int(input("Введите сколько минут ждать: "))
#     secunds = int(input("Введите сколько секунд ждать: "))
#     t1 = threading.Thread(target=Timer, args=(hours, minutes, secunds))
#     t2 = threading.Thread(target=Stopwatch, args=(hours, minutes, secunds))
#     choise = int(input("1/2"))
#     if choise == 1:
#         t1.start()
#     elif choise == 2:
#         t2.start()
#
#
#==========================================================================================================================================================================================
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def __init__(self, args):
#         super().__init__()
#         self._args = args
#
#     def run(self):
#         print(self._args)
#
#
# #========================= MAIN =========================
# if __name__ == "__main__":
#     array = []
#     for i in range(10):
#         array.append(MyThread(f"#{i + 1}"))
#
#     for item in array:
#         item.run()
#         time.sleep(4)
#
#
#==========================================================================================================================================================================================
# from Tic_Tac_Toe.Game import *
#
# if __name__ == "__main__":
#     newGame = Game()
#     newGame.startGame()
#
#
#==========================================================================================================================================================================================
# from Sneakers.RunningSneakers import*
# from Sneakers.Scripts import*
# import os
#
# if __name__ == "__main__":
#     runningSneakers = RunningSneakers("Puma", "First mile", "Black", 43, True, "Sport")
#     writeCharacteristicsToFile(runningSneakers)
#     runningSneakersCopy = RunningSneakers(readCharacteristicsFromFile(os.path.join(os.getcwd() + "file.txt")))
#
#
#==========================================================================================================================================================================================
# from Snake_Game.Game import *
#
# if __name__ == "__main__":
#      snakeGame = Game()
#      snakeGame.startGame()
#
#
#==========================================================================================================================================================================================
# from Overloading.Line import *
# from Overloading.Square import *
# from Overloading.Coordinates import *
#
# def compare(firstOBJ, secondOBJ):
#      return str(firstOBJ) == str(secondOBJ)
#
# if __name__ == "__main__":
#      squareCoordinates = Coordinates(1, 4)
#      lineCoordinates = Coordinates(-3, 8)
#
#      square = Square("red" ,"plastic" , squareCoordinates, 5)
#      line = Line("black" ,"wood" , lineCoordinates, 10)
#
#      print(f"\n{str(square)}")
#      print(f"\n{str(line)}")
#      print(f"\nCompare:\t{compare(square, line)}")
#
#
#==========================================================================================================================================================================================
# import psutil
# import time
#
# if __name__ == "__main__":
#      for item in psutil.process_iter():
#           print(item)
#      print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
#
#      programNames = {"chrome.exe", "safari.exe", "explorer.exe"}
#      workedMoreThenHour = []
#      for program in programNames:
#           flag = False
#           for item in psutil.process_iter():
#                if item.name() == program:
#                     flag = True
#                     if time.time() - item.create_time() >= 3600 and item.name() not in workedMoreThenHour:
#                          workedMoreThenHour.append(item.name())
#           print(f"Is '{program}' open:\t{flag}")
#
#      print("\nWorked more then hour:")
#      for name in workedMoreThenHour:
#           print(name)
#
#
#==========================================================================================================================================================================================
# import json
# from Materials_Guns.Materials.Wood import *
# from Materials_Guns.Materials.Metal import *
# from Materials_Guns.Materials.Stone import *
# from Materials_Guns.Materials.Leather import *
# # from Point_Line_Square.Point2D import Point2D
#
# if __name__ == "__main__":
#     materials = [Wood(), Metal(), Stone(), Leather()]
#     materialsDICT = []
#     for item in materials:
#         materialsDICT.append(item.__dict__)
#
#     with open("materials.json", "w") as file:
#         pointJSON = json.dumps(str(materialsDICT))
#         file.write(pointJSON)
#
#     with open("materials.json", "r") as file:
#         print(str(json.load(file)))
#
#
#     # points = [Point2D(3, 5), Point2D(7, 0), Point2D(-4, 2), Point2D(9, 1), Point2D(-5, -5)]
#     # pointsDICT = []
#     # for item in points:
#     #     pointsDICT.append(str(item))
#     #
#     # with open("point2D.json", "w") as file:
#     #     pointJSON = json.dumps(str(pointsDICT))
#     #     file.write(pointJSON)
#     #
#     # with open("point2D.json", "r") as file:
#     #     print(str(file.read()))
#
#
#==========================================================================================================================================================================================
# import psutil
# import json
# import shutil
# import os
#
# if __name__ == "__main__":
#     processesDICT = []
#     for item in psutil.process_iter():
#         print(item)
#         streamName = f"Name: {item.name()}"
#         if streamName in processesDICT:
#             continue
#         streamPID = f"PID: {item.pid}"
#         processesDICT.append(streamName)
#         processesDICT.append(streamPID)
#
#     with open("processes.json", 'w') as file:
#         processesJSON = json.dumps(str(processesDICT))
#         file.write(processesJSON)
#
#     pathToFile = os.path.join(os.getcwd(), "processes.json")
#     desctopPath = os.path.join(os.path.expanduser('~'), "Desktop")
#     shutil.copy(pathToFile, os.path.join(desctopPath, "processes.json"))
#
#
#==========================================================================================================================================================================================
# from Molecules.Atom import *
# from Molecules.Molecule import *
#
# if __name__ == "__main__":
#     atom1 = Atom("H", 10, 10, 10, 30, 8)
#     atom2 = Atom("O", 20, 20, 20, 60, 16)
#
#     molecule1 = Molecule("H2O", atom1, atom2, atom1)
#     molecule1.print()
#     print("\n-=-=-=-=-=-=-=-=-")
#     print(molecule1.atoms[1])
#
#
#==========================================================================================================================================================================================
from tkinter import *
from tkinter import ttk

def clickRed():
    global window
    # window["text"] = "+10      RED"
    global colorRed
    if colorRed + 10 <= 255:
        colorRed += 10
    else:
        print("MAX VALUE")
    window["background"] = f"#{colorRed:02x}{colorGreen:02x}{colorBlue:02x}"

def clickGreen():
    global window
    # window["text"] = "+10 GREEN"
    global colorGreen
    if colorGreen + 10 <= 255:
        colorGreen += 10
    else:
        print("MAX VALUE")
    window["background"] = f"#{colorRed:02x}{colorGreen:02x}{colorBlue:02x}"

def clickBlue():
    global window
    # window["text"] = "+10    BLUE"
    global colorBlue
    if colorBlue + 10 <= 255:
        colorBlue += 10
    else:
        print("MAX VALUE")
    window["background"] = f"#{colorRed:02x}{colorGreen:02x}{colorBlue:02x}"



if __name__ == "__main__":
    window = Tk()
    window.geometry("700x500")
    window.resizable(True, True)
    window.title("Hello window!")
    colorRed = 0
    colorGreen = 0
    colorBlue = 0
    window.configure(background=f"#{colorRed:02x}{colorGreen:02x}{colorBlue:02x}")

    button1 = ttk.Button(text="RED", command=clickRed)
    button1.place(x=150, y=200)

    button2 = ttk.Button(text="GREEN", command=clickGreen)
    button2.place(x=300, y=200)

    button3 = ttk.Button(text="BLUE", command=clickBlue)
    button3.place(x=450, y=200)

    # label1 = ttk.Label(text="--COLOR--")
    # label1.place(x=160, y=10)
    # label1.configure(background=f"#{colorRed:02x}{colorGreen:02x}{colorBlue:02x}")
    # label1.configure(background="white")

    window.mainloop()