from Materials_Guns.Materials.Material import *

class Wood(Material):
    def __init__(self):
        super()._materialType = "WOOD"
        super()._color = "BROWN"
        super()._weight = 250