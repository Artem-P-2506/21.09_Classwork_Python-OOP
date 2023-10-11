from Sneakers.Sneakers import*

class RunningSneakers(Sneakers):
    def __init__(self, brandName, model, color, size, laces, sole):
        super().__init__(brandName, model, color, size, laces, sole)
        self._type = "RUNNING"

    def getType(self):
        return self._type

    def showCharacteristics(self):
        return super().showCharacteristics() + f"\nType:\t{str(self._type)}"