from Zwierze import Zwierze
from Pole import Pole
from Kierunek import Kierunek
from Wynik import Wynik

class Czlowiek(Zwierze):
    SUPER_SILA = 10
    def __init__(self, x, y, turaPowst, world, sila = 5, licznik = 0):
        super().__init__(x, y, sila, 4, turaPowst, Pole.CZLOWIEK, True, world)
        self.kierunek = Kierunek.NIC
        self.licznik = licznik

    def die(self):
        super().die()
        self.world.koniecGry = True
        self.world.komentator.komentujSmierc()

    def akcja(self):
        if self.kierunek == Kierunek.GORA:
            if self.world.isXYinWorld(self.x, self.y - 1) == False:
                return
            if self.world.isXYfree(self.x, self.y - 1) == True:
                self.przesun(0, -1)
            else:
                org = self.world.getOrganizm(self.x, self.y - 1)
                if org.kolizja(self) == Wynik.LOST:
                    self.przesun(0, -1)
        elif self.kierunek == Kierunek.DOL:
            if self.world.isXYinWorld(self.x, self.y + 1) == False:
                return
            if self.world.isXYfree(self.x, self.y + 1) == True:
                self.przesun(0, 1)
            else:
                org = self.world.getOrganizm(self.x, self.y + 1)
                if org.kolizja(self) == Wynik.LOST:
                    self.przesun(0, 1)
        elif self.kierunek == Kierunek.LEWO:
            if self.world.isXYinWorld(self.x - 1, self.y) == False:
                return
            if self.world.isXYfree(self.x - 1, self.y) == True:
                self.przesun(-1, 0)
            else:
                org = self.world.getOrganizm(self.x - 1, self.y)
                if org.kolizja(self) == Wynik.LOST:
                    self.przesun(-1, 0)
        elif self.kierunek == Kierunek.PRAWO:
            if self.world.isXYinWorld(self.x + 1, self.y) == False:
                return
            if self.world.isXYfree(self.x + 1, self.y) == True:
                self.przesun(1, 0)
            else:
                org = self.world.getOrganizm(self.x + 1, self.y)
                if org.kolizja(self) == Wynik.LOST:
                    self.przesun(1, 0)

    def przesun(self, oX, oY):
        if oX == 0 and oY != 0:
            self.world.setPole(self.x, self.y, Pole.EMPTY)
            self.y = self.y + oY
            self.world.setPole(self.x, self.y, Pole.CZLOWIEK)
        if oX != 0 and oY == 0:
            self.world.setPole(self.x, self.y, Pole.EMPTY)
            self.x = self.x + oX
            self.world.setPole(self.x, self.y, Pole.CZLOWIEK)
            

    def aktywujUmiejetnosc(self):
        if self.licznik == 0:
            self.world.komentator.komentujAktywacjeUm()
            self.licznik = Czlowiek.SUPER_SILA
            self.sila = Czlowiek.SUPER_SILA + 1
            return True
        return False

    def sprawdzUmiejetnosc(self):
        if self.licznik != 0:
            if self.licznik >= Czlowiek.SUPER_SILA//2:
                self.sila = self.sila - 1
            self.licznik = self.licznik - 1

    def saveData(self):
        return super().saveData() + " " + str(self.licznik)

    def loadData(self, line):
        return self.makeNew(int(line[1]), int(line[2]), int(line[3]), self.world, int(line[4]), int(line[5]))

    def makeNew(self, x, y, turaPowst, world, sila = 5, licznik = 0):
        return Czlowiek(x, y, turaPowst, self.world, sila, licznik)

    def getImage(self):
        return "images\\czlowiek.png"


