from Snake_Game.Snake import *
from Snake_Game.Field import *
import random

class Game:
    def __init__(self):
        self._field = Field()
        self._snake = Snake()

    def startGame(self):
        field = self._field.getField()
        self._field.setSnake(random.randint(0, len(field) - 1), random.randint(0, len(field[0]) - 1), self._snake.getHeadSimbol())
        self._field._showField()