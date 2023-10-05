import os
from Tic_Tac_Toe.Cross import *
from Tic_Tac_Toe.Circle import *

class Game():
    def __init__(self):
        self.__arrayTicTacToe = []
        self.__firstPlayerName = "NONE"
        self.__secondPlayerName = "NONE"

    def getFirstPlayerName(self):
        return self.__firstPlayerName

    def getSecondPlayerName(self):
        return self.__secondPlayerName

    def setFirstPlayerName(self, newName):
        self.__firstPlayerName = newName

    def setSecondPlayerName(self, newName):
        self.__secondPlayerName = newName

    def __makeArray(self, rows, colums):
        for i in range(rows):
            self.__arrayTicTacToe.append([])
            for j in range(colums):
                self.__arrayTicTacToe[i].append(Cell(i, j))

    def __changeCell(self, playerName):
        if playerName == self.__firstPlayerName:
            value = 1
            symbol = "CROSS"
        elif playerName == self.__secondPlayerName:
            value = 2
            symbol = "CIRCLE"
        else: #Передано несуществующее имя игрока
            value = 0
            symbol = "NONE"

        print(f"\tСейчас ходит игрок '{playerName}' ({symbol})!")
        coorinateY = int(input("Введите Y-координату ячейки для хода: "))
        coorinateX = int(input("Введите X-координату ячейки для хода: "))
        # print(f"Введите какое значение Вы хотите поставить в ячейку {coorinateX},{coorinateY}: ")
        # value = int(input("CROSS = 1  |  CIRCLE = 0  : "))
        if value == 1 and self.__arrayTicTacToe[len(self.__arrayTicTacToe) - coorinateY][coorinateX - 1].getValue() == "(noValue)":
            self.__arrayTicTacToe[len(self.__arrayTicTacToe) - coorinateY][coorinateX - 1] = Cross(coorinateX, coorinateY)
        elif value == 2 and self.__arrayTicTacToe[len(self.__arrayTicTacToe) - coorinateY][coorinateX - 1].getValue() == "(noValue)":
            self.__arrayTicTacToe[len(self.__arrayTicTacToe) - coorinateY][coorinateX - 1] = Сircle(coorinateX, coorinateY)
        else:
            print("Wrong input or cell is not empty!")

        with open("gameLOGS.txt", 'a') as file:
            file.write(f"\nPlayer\t'{playerName}' set into cell\t{coorinateX},{coorinateY} symbol\t{symbol}")


    def __showField(self):
        print("\n=> ПОЛЕ:")
        for row in self.__arrayTicTacToe:
            for column in row:
                print("\t", str(column.getValue()), "\t", end="")
            print("\n")

    def startGame(self):
        self.__firstPlayerName = input("Введите имя первого игрока (CROSS): ")
        self.__secondPlayerName = input("Введите имя второго игрока (CIRCLE): ")
        with open("gameLOGS.txt", 'w') as file:
            file.write(f"First player name:\t{str(self.__firstPlayerName)}\nSecond player name:\t{str(self.__secondPlayerName)}")

        rows = int(input("Введите количесво рядков у поля: "))
        colums = int(input("Введите количесво колонок у поля: "))
        with open("gameLOGS.txt", 'a') as file:
            file.write(f"\nField size (rows*columns):\t{rows}*{colums}\n")
        self.__makeArray(rows, colums)
        self.__showField()

        while(True):
            self.__changeCell(self.__firstPlayerName) # Ходит первый игрок
            self.__showField()
            self.__changeCell(self.__secondPlayerName) # Ходит второй игрок
            self.__showField()


        # i = 0
        # while(i < rows*colums):
        #     self.__changeCell()
        #     i += 1
        #     print("\n=> НОВОЕ ПОЛЕ:")
        #     self.__showField()

