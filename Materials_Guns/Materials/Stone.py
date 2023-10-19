from Materials_Guns.Materials.Material import *

class Stone(Material):
    def __init__(self):
        super()._materialType = "STONE"
        super()._color = "GRAY"
        super()._weight = 350