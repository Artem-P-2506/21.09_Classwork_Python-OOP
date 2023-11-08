class Atom:
    def __init__(self, sign, numberOfProtons, numberOfNeutrons, numberOfElectrons, weight, valency):
        self._sign = sign
        self._numberOfProtons = numberOfProtons
        self._numberOfNeutrons = numberOfNeutrons
        self._numberOfElectrons = numberOfElectrons
        self._weight = weight
        self._valency = valency

    def setSign(self, newSign):
        self._sign = newSign

    def getSign(self):
        return self._sign

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

    def __str__ (self):
        return f"Символ:\t'{self._sign}'" \
               f"\nЧисло протонов:\t{str(self._numberOfProtons)}" \
               f"\nЧисло нейтронов:\t{str(self._numberOfNeutrons)}" \
               f"\nЧисло електронов:\t{str(self._numberOfElectrons)}" \
               f"\nВес:\t{str(self._weight)}g" \
               f"\nВалентность:\t{str(self._valency)}"