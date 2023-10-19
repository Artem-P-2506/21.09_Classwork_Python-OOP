class Weapon:
    def __init__(self):
        self._type = "NONE"
        self._weight = "NONE"
        self._damage = "NONE"
        self._parts = []

    def getType(self):
        return self._type

    def getWeight(self):
        return self._weight

    def getDamage(self):
        return self._damage

    def getParts(self):
        return self._parts

    def __str__(self):
        return f"Type:\t{str(self._type)}\nWeight:\t{str(self._weight)}\nDamage:\t{str(self._damage)}\nParts:\t{str(self._parts)}"