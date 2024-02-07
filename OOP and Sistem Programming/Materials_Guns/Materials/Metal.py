from Materials_Guns.Materials.Material import *

class Metal(Material):
    def __init__(self):
        super().__init__("METAL", "SILVER", 500)