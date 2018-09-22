from Roslina import Roslina
from Pole import Pole
class Trawa(Roslina):
    def __init__(self, x, y, turaPowst, world, sila = 0):
        super().__init__(x, y, sila, 0, turaPowst, Pole.TRAWA, True, world)

    def getImage(self):
        return "images\\trawa.png"

    def makeNew(self, x, y, turaPowst, world, sila = 0):
        return Trawa(x, y, turaPowst, world, sila)


