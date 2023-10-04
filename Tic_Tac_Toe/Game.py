from Tic_Tac_Toe.Cross import *
from Tic_Tac_Toe.Circle import *

class Game():
    def __init__(self):
        self.__arrayTicTacToe = []

    def __makeArray(self, rows, columns):
        for i in range(rows):
            self.__arrayTicTacToe.append([])
            for j in range(columns):
                self.__arrayTicTacToe[i].append(Cell(i, j))
        return self.__arrayTicTacToe

    def __changeCell(self):
        coorinateX = int(input("Введите X-координату ячейки для хода: "))
        coorinateY = int(input("Введите Y-координату ячейки для хода: "))
        print(f"Введите какое значение Вы хотите поставить в ячейку {coorinateX},{coorinateY}: ")
        value = int(input("CROSS = 1  |  CIRCLE = 0  : "))
        if value == 1:
            self.__arrayTicTacToe[coorinateX - 1][coorinateY - 1] = Cross(coorinateX, coorinateY)
        elif value == 0:
            self.__arrayTicTacToe[coorinateX - 1][coorinateY - 1] = Cell(coorinateX, coorinateY)
        else:
            print("Wrong input!")

    def __showField(self):
        for row in self.__arrayTicTacToe:
            for column in row:
                print("\t", str(column.getValue()), "\t", end="")
            print("\n")

    def startGame(self):
        rows = int(input("Введите количество рядов матрицы: "))
        columns = int(input("Введите количество колонок матрицы: "))
        self.__makeArray(rows, columns)
        print("\n\t\t\t========== ПОЛЕ ==========")
        self.__showField()

        i = 0
        while(i <= rows*columns):
            self.__changeCell()
            i += 1
            print("\n\t\t========== НОВОЕ ПОЛЕ ==========")
            self.__showField()