from Roslina import Roslina
from Pole import Pole
class WilczeJagody(Roslina):
    def __init__(self, x, y, turaPowst, world, sila = 99):
        super().__init__(x, y, sila, 0, turaPowst, Pole.WILCZE_JAG, True, world)

    def kolizja(self, org):
        org.die()
        return super().kolizja(org)

    def getImage(self):
        return "images\\wilczeJag.png"

    def makeNew(self, x, y, turaPowst, world, sila = 99):
        return WilczeJagody(x, y, turaPowst, world, sila)


