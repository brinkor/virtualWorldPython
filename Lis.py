from Zwierze import Zwierze
from Pole import Pole
from Wynik import Wynik
from random import randint
from XY import XY

class Lis(Zwierze):
    def __init__(self, x, y, turaPowst, world, sila = 3):
        super().__init__(x, y, sila, 7, turaPowst, Pole.LIS, True, world)

    def makeNew(self, x, y, turaPowst, world, sila = 3):
        return Lis(x, y, turaPowst, self.world, sila)

    def getImage(self):
        return "images\\lis.png"

    def akcja(self):
        xy = self.znajdzBezpiecznePole()
        if xy.x != -1 and xy.y != -1:
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

    def znajdzBezpiecznePole(self):
        losowy = randint(0, 7)
        zwiekszany = losowy
        xy = XY()
        while True:
            if zwiekszany == 0:
                if self.world.isXYinWorld(self.x - 1, self.y) and (self.world.isXYfree(self.x - 1, self.y) or self.isWeaker(self.x - 1, self.y)):
                    xy.x = self.x - 1;
                    xy.y = self.y;
                    return xy;
            elif zwiekszany == 1:
                if self.world.isXYinWorld(self.x + 1, self.y) and (self.world.isXYfree(self.x + 1, self.y) or self.isWeaker(self.x + 1, self.y)):
                    xy.x = self.x + 1;
                    xy.y = self.y;
                    return xy;
            elif zwiekszany == 2:
                if self.world.isXYinWorld(self.x + 1, self.y + 1) and (self.world.isXYfree(self.x + 1, self.y + 1) or self.isWeaker(self.x + 1, self.y + 1)):
                    xy.x = self.x + 1;
                    xy.y = self.y + 1;
                    return xy;
            elif zwiekszany == 3:
                if self.world.isXYinWorld(self.x + 1, self.y - 1) and (self.world.isXYfree(self.x + 1, self.y - 1) or self.isWeaker(self.x + 1, self.y - 1)):
                    xy.x = self.x + 1;
                    xy.y = self.y - 1;
                    return xy;
            elif zwiekszany == 4:
                if self.world.isXYinWorld(self.x - 1, self.y - 1) and (self.world.isXYfree(self.x - 1, self.y - 1) or self.isWeaker(self.x - 1, self.y - 1)):
                    xy.x = self.x - 1;
                    xy.y = self.y - 1;
                    return xy;
            elif zwiekszany == 5:
                if self.world.isXYinWorld(self.x - 1, self.y + 1) and (self.world.isXYfree(self.x - 1, self.y + 1) or self.isWeaker(self.x - 1, self.y + 1)):
                    xy.x = self.x - 1;
                    xy.y = self.y + 1;
                    return xy;
            elif zwiekszany == 6:
                if self.world.isXYinWorld(self.x, self.y + 1) and (self.world.isXYfree(self.x, self.y + 1) or self.isWeaker(self.x, self.y + 1)):
                    xy.x = self.x;
                    xy.y = self.y + 1;
                    return xy;
            elif zwiekszany == 7:
                if self.world.isXYinWorld(self.x, self.y - 1) and (self.world.isXYfree(self.x, self.y - 1) or self.isWeaker(self.x, self.y - 1)):
                    xy.x = self.x;
                    xy.y = self.y - 1;
                    return xy;
            zwiekszany = (zwiekszany + 1) % 8
            if losowy == zwiekszany:
                break;
        xy.x = -1
        xy.y = -1
        return xy

    def isWeaker(self, x, y):
        org = self.world.getOrganizm(self.x, self.y)
        if org != None:
            if org.sila < self.sila or (org.sila == self.sila and org.turaPowst < self.turaPowst):
                return True
            else:
                return False
        return True
