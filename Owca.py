from Zwierze import Zwierze
from Pole import Pole
class Owca(Zwierze):
    def __init__(self, x, y, turaPowst, world, sila = 4):
        super().__init__(x, y, sila, 4, turaPowst, Pole.OWCA, True, world)

    def makeNew(self, x, y, turaPowst, world, sila = 4):
        return Owca(x, y, turaPowst, self.world, sila)

    def getImage(self):
        return "images\\owca.png"


