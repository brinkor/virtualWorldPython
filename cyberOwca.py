from Zwierze import Zwierze
from Pole import Pole

class cyberOwca(Zwierze):
    def __init__(self, x, y, turaPowst, world, sila = 11):
        super().__init__(x, y, sila, 4, turaPowst, Pole.CYBEROWCAOWCA, True, world)

    def makeNew(self, x, y, turaPowst, world, sila = 4):
        return cyberOwcaOwca(x, y, turaPowst, self.world, sila)

    def getImage(self):
        return "images\\cyberOwca.png"


