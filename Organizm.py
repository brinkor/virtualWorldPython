#from World import World
from Pole import Pole
from abc import ABC, abstractmethod
from Wynik import Wynik
class Organizm(ABC):
    def __init__(self, x, y, sila, inicjatywa, turaPowst, typPola, alive, world):
        from World import World
        self.x = x
        self.y = y
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.turaPowst = turaPowst
        self.typPola = typPola
        self.alive = alive
        self.world = world

    @abstractmethod
    def getImage(self):
        pass
    @abstractmethod
    def akcja(self):
        pass
    @abstractmethod
    def makeNew(self,x,y,turaPowst,world):
        pass

    def kolizja(self, org):
        if self.sila == org.sila:
            if self.turaPowst < org.turaPowst:
                win = True
            else:
                win = False
        elif self.sila > org.sila:
            win = True
        else:
            win = False
        if win == True:
            self.world.komentator.komentujWalke(self, org)
            org.die()
        else:
            self.world.komentator.komentujWalke(org, self)
            self.die()
        if win == True:
            return Wynik.WIN
        else:
            return Wynik.LOST

    def die(self):
        self.world.setPole(self.x, self.y, Pole.EMPTY)
        self.alive = False

    def saveData(self):
        return self.__class__.__name__ + " " + str(self.x) + " " + str(self.y) + " " + str(self.turaPowst) + " " + str(self.sila)

    def loadData(self, line):
        return self.makeNew(int(line[1]), int(line[2]), int(line[3]), self.world, int(line[4]))

