from Organizm import Organizm
from Pole import Pole
from Wynik import Wynik
class Zwierze(Organizm):
    def __init__(self, x, y, sila, inicjatywa, turaPowst, typPola, alive, world):
        super().__init__(x, y, sila, inicjatywa, turaPowst, typPola, alive, world)
        from World import World

    def akcja(self):
        xy = self.world.findAnyField(self.x, self.y)
        if self.world.isXYfree(xy.x, xy.y):
            self.world.setPole(self.x, self.y, Pole.EMPTY)
            self.world.setPole(xy.x, xy.y, self.typPola)
            self.x = xy.x
            self.y = xy.y
        else:
            org = self.world.getOrganizm(xy.x, xy.y)
            if org != None:
                wynik = org.kolizja(self)
                if wynik == Wynik.LOST:
                    self.world.setPole(self.x, self.y, Pole.EMPTY)
                    self.world.setPole(xy.x, xy.y, self.typPola)
                    self.x = xy.x
                    self.y = xy.y
                elif wynik == Wynik.WIN:
                    self.world.setPole(self.x, self.y, Pole.EMPTY)
            else:
                print("brak organizmu na zajetym polu??")

    def rozmnazaj(self):
        puste = self.world.findEmpty(self.x, self.y)
        if puste.x == -1 or puste.y == -1:
            return
        self.world.dodajOrganizm(self.makeNew(puste.x, puste.y, self.world.tura, self.world))
        self.world.komentator.komentujRozmnazanie(self)

    def kolizja(self, org):
        if org.__class__ == self.__class__:
            self.rozmnazaj()
            return Wynik.NEW
        return super().kolizja(org)

