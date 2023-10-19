from Materials_Guns.Materials.Material import *

class Plastic(Material):
    def __init__(self):
        super()._materialType = "PLASTIC"
        super()._color = "BLACK"
        super()._weight = 150