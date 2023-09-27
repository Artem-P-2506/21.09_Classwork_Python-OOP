from Banknote_Coin_Bill.Banknote import *

class Coin(Banknote):
    def __init__(self, material, color, denomination, year, form, diameter, ribbing):
        super().__init__(self, material, color, denomination, year, form)
        self._diameter = diameter
        self._ribbing = ribbing

    def getDiameter(self):
        return self._diameter

    def getRibbing(self):
        return self._ribbing

    def show(self):
        print("\nМатериал:\t" + str(self.getMaterial()) +
              "\nЦвет:\t" + str(self.getColor()) + "\nНоминал:\t" + str(self.getDenomination()) +
              "\nГод выпуска:\t" + str(self.getYear()) + "\nФорма:\t" + str(self.getForm()) +
              "\nДиаметр:\t" + str(self.getDiameter()) + "\nРебристость:\t" + str(self.getRibbing()))