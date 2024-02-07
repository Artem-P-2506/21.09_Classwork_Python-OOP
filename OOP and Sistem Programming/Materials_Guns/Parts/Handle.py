from Materials_Guns.Materials import *

class Handle:
    def __init__(self, material, weight):
        self._material = material
        self._weight = weight

    def getMaterial(self):
        return self._material

    def getWeight(self):
        return self._weight