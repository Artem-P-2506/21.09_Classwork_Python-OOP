from Tic_Tac_Toe.Cross import *
from Tic_Tac_Toe.Circle import *

class Game():
    def __init__(self):
        self.__arrayTicTacToe = []

    def makeArray(self, rows, columns):
        for i in range(rows):
            self.__arrayTicTacToe.append([])
            for j in range(columns):
                self.__arrayTicTacToe[i].append(Cell(i, j))
        return self.__arrayTicTacToe

    def showField(array):
        for row in array:
            for column in row:
                print("\t", str(column.getValue()), "\t", end="")
            print("\n")