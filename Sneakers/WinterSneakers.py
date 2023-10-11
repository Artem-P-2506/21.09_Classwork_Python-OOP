from Sneakers.Sneakers import*

class WinterSneakers(Sneakers):
    def __init__(self, brandName, model, color, size, laces, sole):
        super().__init__(brandName, model, color, size, laces, sole)
        self._type = "WINTER"

    def getType(self):
        return self._type

    def showCharacteristics(self):
        return super().showCharacteristics() + f"\nType: {str(self._type)}"