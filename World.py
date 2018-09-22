from Pole import Pole
from Komentator import Komentator
from Organizm import Organizm
from Roslina import Roslina
from XY import XY
from random import randint
from Czlowiek import Czlowiek
from Trawa import Trawa
from Owca import Owca
from Wilk import Wilk
from Lis import Lis
from Zolw import Zolw
from Antylopa import Antylopa
from Mlecz import Mlecz
from Guarana import Guarana
from WilczeJagody import WilczeJagody
from BarszczSosnowskiego import BarszczSosnowskiego
from Window import Window

class World:
    """description of class"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.koniecGry = False
        self.tura = 0
        self.komentator = Komentator(self)
        self.organizmy = list() #lsita org zainicjowac funkcja
        self.organizmyPoczatkowe = list()
        self.ustawOrgPocz()
        self.pole = [[Pole.EMPTY for j in range(x)] for i in range(y)]

    def ustawOrgPocz(self): #dopisz nowo dodane organizmy tutaj
        for typ in range(Pole.SIZE - 1):
            if typ == Pole.CZLOWIEK:
                self.organizmyPoczatkowe.append(Czlowiek(0, 0, self.tura, self))
            elif typ == Pole.TRAWA:
                self.organizmyPoczatkowe.append(Trawa(0, 0, self.tura, self))
            elif typ == Pole.OWCA:
                self.organizmyPoczatkowe.append(Owca(0, 0, self.tura, self))
            elif typ == Pole.WILK:
                self.organizmyPoczatkowe.append(Wilk(0, 0, self.tura, self))
            elif typ == Pole.LIS:
                self.organizmyPoczatkowe.append(Lis(0, 0, self.tura, self))
            elif typ == Pole.ZOLW:
                self.organizmyPoczatkowe.append(Zolw(0, 0, self.tura, self))
            elif typ == Pole.ANTYLOPA:
                self.organizmyPoczatkowe.append(Antylopa(0, 0, self.tura, self))
            elif typ == Pole.MLECZ:
                self.organizmyPoczatkowe.append(Mlecz(0, 0, self.tura, self))
            elif typ == Pole.GUARANA:
                self.organizmyPoczatkowe.append(Guarana(0, 0, self.tura, self))
            elif typ == Pole.WILCZE_JAG:
                self.organizmyPoczatkowe.append(WilczeJagody(0, 0, self.tura, self))
            elif typ == Pole.BARSZCZ:
                self.organizmyPoczatkowe.append(BarszczSosnowskiego(0, 0, self.tura, self))

    def getOrganizm(self, x, y):
        for i in range(len(self.organizmy)): # zminic na for org in organizmy?
            org = self.organizmy[i]
            if org.x == x and org.y == y:
                return org
        return None

    def getCzlowiek(self):
        for i in range(len(self.organizmy)):
            org = self.organizmy[i]
            if isinstance(org, Czlowiek):
                return org
        return None

    def nowaPlansza(self, x, y, tura):
        self.x = x
        self.y = y
        self.tura = tura
        self.pole = [[Pole.EMPTY for j in range(x)] for i in range(y)]


    def czyRoslina(self, org):
        if org != None:
            if type(org).__base__.__name__ == Roslina.__name__:
                return True
            else:
                return False
        else:
            return False

    def generujSwiat(self):
        if self.tura == 0:
            wpisano = False
            for o in self.organizmyPoczatkowe:
                if o.typPola == Pole.CZLOWIEK:
                    lOrg = 1
                else:
                    lOrg = randint(2, 4)
                for j in range(lOrg):
                    while wpisano == False:
                        losX = randint(0, self.x - 1)
                        losY = randint(0, self.y - 1)
                        if self.pole[losY][losX] == Pole.EMPTY:
                            org = o.makeNew(losX, losY, self.tura, self)
                            self.dodajOrganizm(org);
                            wpisano = True
                    wpisano = False

    def usunCiala(self):
        rem = list()
        for org in self.organizmy:
            if org.alive == False:
                rem.append(org)
        for o in rem:
            self.organizmy.remove(o)

    def wykonajTure(self):
        if self.tura == 0:
            self.generujSwiat()
        else:
            self.getCzlowiek().sprawdzUmiejetnosc()
            akcje = list()
            for org in self.organizmy:
                akcje.append(org)
            for org in akcje:
                if org.alive == True:
                    org.akcja()
            self.usunCiala()
        self.tura = self.tura + 1

    def zyj(self):
        self.wykonajTure()
        w = Window(self)

    def printPola(self):
        for i in range(self.y):
            for j in range(self.x):
                print(self.pole[i][j])

    def setPole(self, x, y, typPola):
        self.pole[y][x] = typPola

    def dodajOrganizm(self, org):
        self.setPole(org.x, org.y, org.typPola)
        self.organizmy.append(org)
        self.organizmy.sort(key=self.compOrg, reverse=True)

    def compOrg(self, org):
        return org.inicjatywa

    def isXYfree(self, x, y):
        if self.pole[y][x] == Pole.EMPTY:
            return True
        else:
            return False

    def isXYinWorld(self, x, y):
        if x >= 0 and x < self.x and y >= 0 and y < self.y:
            return True
        else:
            return False

    def findAnyField(self, x, y):
        xy = XY()
        found = False
        los = randint(0, 8)
        while found == False:
            if los == 0:
                if self.isXYinWorld(x + 1, y + 1):
                    found = True
                    xy.x = x + 1
                    xy.y = y + 1
            elif los == 1:
                if self.isXYinWorld(x + 1, y):
                    found = True
                    xy.x = x + 1
                    xy.y = y
            elif los == 2:
                if self.isXYinWorld(x - 1, y + 1):
                    found = True
                    xy.x = x - 1
                    xy.y = y
            elif los == 3:
                if self.isXYinWorld(x, y + 1):
                    found = True
                    xy.x = x
                    xy.y = y + 1
            elif los == 4:
                if self.isXYinWorld(x, y - 1):
                    found = True
                    xy.x = x
                    xy.y = y - 1
            elif los == 5:
                if self.isXYinWorld(x + 1, y - 1):
                    found = True
                    xy.x = x + 1
                    xy.y = y - 1
            elif los == 6:
                if self.isXYinWorld(x - 1, y - 1):
                    found = True
                    xy.x = x - 1
                    xy.y = y - 1
            elif los == 7:
                if self.isXYinWorld(x - 1, y + 1):
                    found = True
                    xy.x = x - 1
                    xy.y = y + 1
            los = (los + 1) % 8
        return xy

    def findEmpty(self, x, y):
        xy = XY()
        if (self.isXYinWorld(x - 1, y) and self.isXYfree(x - 1, y)):
            xy.x = x - 1
            xy.y = y
            return xy
        if (self.isXYinWorld(x - 1, y - 1) and self.isXYfree(x - 1, y - 1)):
            xy.x = x - 1
            xy.y = y - 1
            return xy
        if (self.isXYinWorld(x - 1, y + 1) and self.isXYfree(x - 1, y + 1)):
            xy.x = x - 1
            xy.y = y + 1
            return xy
        if (self.isXYinWorld(x, y - 1) and self.isXYfree(x, y - 1)):
            xy.x = x 
            xy.y = y - 1
            return xy
        if (self.isXYinWorld(x, y + 1) and self.isXYfree(x, y + 1)):
            xy.x = x
            xy.y = y + 1
            return xy
        if (self.isXYinWorld(x + 1, y - 1) and self.isXYfree(x + 1, y - 1)):
            xy.x = x + 1
            xy.y = y - 1
            return xy
        if (self.isXYinWorld(x + 1, y) and self.isXYfree(x + 1, y)):
            xy.x = x + 1
            xy.y = y
            return xy
        if (self.isXYinWorld(x + 1, y + 1) and self.isXYfree(x + 1, y + 1)):
            xy.x = x + 1
            xy.y = y + 1
            return xy
        xy.x = -1
        xy.y = -1
        return xy