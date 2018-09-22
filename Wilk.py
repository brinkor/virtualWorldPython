from Zwierze import Zwierze
from Pole import Pole
class Wilk(Zwierze):
    def __init__(self, x, y, turaPowst, world, sila = 9):
        super().__init__(x, y, sila, 5, turaPowst, Pole.WILK, True, world)

    def makeNew(self, x, y, turaPowst, world, sila = 9):
        return Wilk(x, y, turaPowst, self.world, sila)

    def getImage(self):
        return "images\\wilk.png"


