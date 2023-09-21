class Atom:
    def __init__(self, numberOfProtons, numberOfNeutrons, numberOfElectrons, weight, valency):
        self.__numberOfProtons = numberOfProtons
        self.__numberOfNeutrons = numberOfNeutrons
        self.__numberOfElectrons = numberOfElectrons
        self.__weight = weight
        self.__valency = valency

    def setNumberOfProtons(self, newNumberOfProtons):
        self.__numberOfProtons = newNumberOfProtons

    def getNumberOfProtons(self):
        return self.__numberOfProtons

    def setNumberOfNeutrons(self, newNumberOfNeutrons):
        self.__numberOfNeutrons = newNumberOfNeutrons

    def getNumberOfNeutrons(self):
        return self.__numberOfNeutrons

    def setNumberOfElectrons(self, newNumberOfElectrons):
        self.__numberOfElectrons = newNumberOfElectrons

    def getNumberOfElectrons(self):
        return self.__numberOfElectrons

    def setWeight(self, newWeight):
        self.__weight = newWeight

    def getWeight(self):
        return self.__weight

    def setValency(self, newValency):
        self.__valency = newValency

    def getValency(self):
        return self.__valency

    def print(self):
        print("Число протонов: " + str(self.getNumberOfProtons()) + "\nЧисло нейтронов: " + str(self.getNumberOfNeutrons()) +
              "\nЧисло електронов: " + str(self.getNumberOfElectrons()) + "\nВес: " + str(self.getWeight()) + "g" +
              "\nВалентность: " + str(self.getValency()))