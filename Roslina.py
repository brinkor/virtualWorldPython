#from abc import ABC, abstractmethod
from Organizm import Organizm
from random import randint
class Roslina(Organizm):
    TEMPO_ROZROSTU = 3
    def __init__(self, x, y, sila, inicjatywa, turaPowst, typPola, alive, world):
        super().__init__(x,y,sila,inicjatywa,turaPowst,typPola,alive,world)

    def akcja(self):
        ran = randint(1, 100)
        if ran < self.TEMPO_ROZROSTU:
            xy = self.world.findEmpty(self.x, self.y)
            if xy.x == -1 or xy.y == -1:
                return
            self.world.dodajOrganizm(self.makeNew(xy.x, xy.y, self.world.tura, self.world))
            self.world.komentator.komentujZasianie(self)



