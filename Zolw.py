from Zwierze import Zwierze
from Pole import Pole
from Wynik import Wynik
from random import randint

class Zolw(Zwierze):
    SZANSA_NA_RUCH = 25
    MAX_ODBIJANA_SILA = 4
    def __init__(self, x, y, turaPowst, world, sila = 2):
        super().__init__(x, y, sila, 1, turaPowst, Pole.ZOLW, True, world)

    def akcja(self):
        if randint(1, 100) > 100 - self.SZANSA_NA_RUCH:
            super().akcja()

    def kolizja(self, org):
        if org.sila <= self.MAX_ODBIJANA_SILA:
            self.world.komentator.komentujOdbicieAtaku(org, self)
            return Wynik.NEW
        else:
            return super().kolizja(org)

    def makeNew(self, x, y, turaPowst, world, sila = 2):
        return Zolw(x, y, turaPowst, self.world, sila)

    def getImage(self):
        return "images\\zolw.png"


