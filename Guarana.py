from Roslina import Roslina
from Pole import Pole
class Guarana(Roslina):
    def __init__(self, x, y, turaPowst, world, sila = 0):
        super().__init__(x, y, sila, 0, turaPowst, Pole.GUARANA, True, world)

    def kolizja(self, org):
        org.sila = org.sila + 3
        return super().kolizja(org)

    def getImage(self):
        return "images\\guarana.png"

    def makeNew(self, x, y, turaPowst, world, sila = 0):
        return Guarana(x, y, turaPowst, world, sila)


