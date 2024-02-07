class Atom:
    def __init__(self, numberOfProtons, numberOfNeutrons, numberOfElectrons, weight, valency):
        self._numberOfProtons = numberOfProtons
        self._numberOfNeutrons = numberOfNeutrons
        self._numberOfElectrons = numberOfElectrons
        self._weight = weight
        self._valency = valency

    def setNumberOfProtons(self, newNumberOfProtons):
        self._numberOfProtons = newNumberOfProtons

    def getNumberOfProtons(self):
        return self._numberOfProtons

    def setNumberOfNeutrons(self, newNumberOfNeutrons):
        self._numberOfNeutrons = newNumberOfNeutrons

    def getNumberOfNeutrons(self):
        return self._numberOfNeutrons

    def setNumberOfElectrons(self, newNumberOfElectrons):
        self._numberOfElectrons = newNumberOfElectrons

    def getNumberOfElectrons(self):
        return self._numberOfElectrons

    def setWeight(self, newWeight):
        self._weight = newWeight

    def getWeight(self):
        return self._weight

    def setValency(self, newValency):
        self._valency = newValency

    def getValency(self):
        return self._valency

    def print(self):
        print("Число протонов: " + str(self._numberOfProtons) + "\nЧисло нейтронов: " + str(self._numberOfNeutrons) +
              "\nЧисло електронов: " + str(self._numberOfElectrons) + "\nВес: " + str(self._weight) + "g" +
              "\nВалентность: " + str(self._valency))