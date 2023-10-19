from Materials_Guns.Materials.Material import *

class Leather(Material):
    def __init__(self):
        super()._materialType = "LEATHER"
        super()._color = "LIGHT BROWN"
        super()._weight = 350