from Banknote_Coin_Bill.Banknote import *

class Bill(Banknote):
    def __init__(self, material, color, denomination, year, form, xSize, ySize, serialNumber, waterStamp , facialPicture, backPicture):
        super().__init__(material, color, denomination, year, form)
        self._xSize = xSize
        self._ySize = ySize
        self._serialNumber = serialNumber
        self._waterStamp = waterStamp
        self._facialPicture = facialPicture
        self._backPicture = backPicture

    def getXSize(self):
        return self._xSize

    def getYSize(self):
        return self._ySize

    def getSeriealNumber(self):
        return self._serialNumber

    def getWaterStamp(self):
        return self._waterStamp

    def getFacialPicture(self):
        return self._facialPicture

    def getBackPicture(self):
        return self._backPicture

    def show(self):
        print("Материал:\t" + str(self.getMaterial()) +
              "\nЦвет:\t" + str(self.getColor()) + "\nНоминал:\t" + str(self.getDenomination()) +
              "\nГод выпуска:\t" + str(self.getYear()) + "\nФорма:\t" + str(self.getForm()) +
              "\nРазмер_X:\t" + str(self.getXSize()) + "мм" + "\nРазмер_Y:\t" + str(self.getYSize()) + "мм" +
              "\nСерийный номер:\t" + str(self.getSeriealNumber()) + "\nВодная марка:\t" + str(self.getWaterStamp()) +
              "\nЛицевая картинка:\t" + str(self.getFacialPicture()) + "\nЗадняя картинка:\t" + str(self.getBackPicture()))