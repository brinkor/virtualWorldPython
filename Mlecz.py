from Roslina import Roslina
from Pole import Pole
class Mlecz(Roslina):
    def __init__(self, x, y, turaPowst, world, sila = 0):
        super().__init__(x, y, sila, 0, turaPowst, Pole.MLECZ, True, world)

    def akcja(self):
        for i in range(3):
            super().akcja()

    def getImage(self):
        return "images\\mlecz.png"

    def makeNew(self, x, y, turaPowst, world, sila = 0):
        return Mlecz(x, y, turaPowst, world, sila)


