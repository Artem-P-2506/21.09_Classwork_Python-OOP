from Materials_Guns.Materials.Material import *

class Metal(Material):
    def __init__(self):
        super()._materialType = "METAL"
        super()._color = "SILVER"
        super()._weight = 500