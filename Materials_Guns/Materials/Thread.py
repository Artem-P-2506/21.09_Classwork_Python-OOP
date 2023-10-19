from Materials_Guns.Materials.Material import *

class Thread(Material):
    def __init__(self):
        super()._materialType = "THREAD"
        super()._color = "WHITE"
        super()._weight = 100