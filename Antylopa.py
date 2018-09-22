from Zwierze import Zwierze
from Pole import Pole
from random import randint
from XY import XY
from Wynik import Wynik

class Antylopa(Zwierze):
    def __init__(self, x, y, turaPowst, world, sila = 4):
        super().__init__(x, y, sila, 4, turaPowst, Pole.ANTYLOPA, True, world)

    def akcja(self):
        for i in range(2):
            if self.alive == True:
                super().akcja()

    def kolizja(self, org):
        ucieczka = randint(0, 1)
        if self.__class__ == org.__class__:
            return super().kolizja(org)
        elif ucieczka == 1:
            self.world.komentator.komentujUcieczkeAntylopy()
            while True:
                xy = self.world.findAnyField(self.x, self.y)
                if xy.x != org.x or xy.y != org.y:
                    break
            if self.world.isXYfree(xy.x, xy.y):
                self.world.setPole(self.x, self.y, Pole.EMPTY)
                self.world.setPole(xy.x, xy.y, self.typPola)
                self.x = xy.x
                self.y = xy.y
            else:
                przeciwnik = self.world.getOrganizm(xy.x, xy.y)
                if przeciwnik != None:
                    wynik = przeciwnik.kolizja(self)
                    if wynik == Wynik.LOST:
                        self.world.setPole(self.x, self.y, Pole.EMPTY)
                        self.world.setPole(xy.x, xy.y, self.typPola)
                        self.x = xy.x
                        self.y = xy.y
                    elif wynik == Wynik.WIN:
                        self.world.setPole(self.x, self.y, Pole.EMPTY)
            return Wynik.LOST
        else:
            return super().kolizja(org)


    def makeNew(self, x, y, turaPowst, world, sila = 4):
        return Antylopa(x, y, turaPowst, self.world, sila)

    def getImage(self):
        return "images\\antylopa.png"


