from Roslina import Roslina
from Pole import Pole

class BarszczSosnowskiego(Roslina):
    def __init__(self, x, y, turaPowst, world, sila = 10):
        super().__init__(x, y, sila, 0, turaPowst, Pole.BARSZCZ, True, world)

    def akcja(self):
        if self.world.isXYinWorld(self.x - 1, self.y) and (self.world.isXYfree(self.x - 1, self.y)) == False and (self.world.czyRoslina(self.world.getOrganizm(self.x - 1, self.y)) == False):
            org = self.world.getOrganizm(self.x - 1, self.y)
            if (org != None):
                self.world.komentator.komentujZabojstwoBarszczu(org)
                org.die()
        if self.world.isXYinWorld(self.x, self.y - 1) and (self.world.isXYfree(self.x, self.y - 1)) == False and (self.world.czyRoslina(self.world.getOrganizm(self.x, self.y - 1)) == False):
            org = self.world.getOrganizm(self.x, self.y - 1)
            if (org != None):
                self.world.komentator.komentujZabojstwoBarszczu(org)
                org.die()
        if self.world.isXYinWorld(self.x + 1, self.y) and (self.world.isXYfree(self.x + 1, self.y)) == False and (self.world.czyRoslina(self.world.getOrganizm(self.x + 1, self.y)) == False):
            org = self.world.getOrganizm(self.x + 1, self.y)
            if (org != None):
                self.world.komentator.komentujZabojstwoBarszczu(org)
                org.die()
        if self.world.isXYinWorld(self.x, self.y + 1) and (self.world.isXYfree(self.x, self.y + 1)) == False and (self.world.czyRoslina(self.world.getOrganizm(self.x, self.y + 1)) == False):
            org = self.world.getOrganizm(self.x, self.y + 1)
            if (org != None):
                self.world.komentator.komentujZabojstwoBarszczu(org)
                org.die()
        if self.world.isXYinWorld(self.x - 1, self.y - 1) and (self.world.isXYfree(self.x - 1, self.y - 1)) == False and (self.world.czyRoslina(self.world.getOrganizm(self.x - 1, self.y - 1)) == False):
            org = self.world.getOrganizm(self.x - 1, self.y - 1)
            if (org != None):
                self.world.komentator.komentujZabojstwoBarszczu(org)
                org.die()
        if self.world.isXYinWorld(self.x - 1, self.y + 1) and (self.world.isXYfree(self.x - 1, self.y + 1)) == False and (self.world.czyRoslina(self.world.getOrganizm(self.x - 1, self.y + 1)) == False):
            org = self.world.getOrganizm(self.x - 1, self.y + 1)
            if (org != None):
                self.world.komentator.komentujZabojstwoBarszczu(org)
                org.die()
        if self.world.isXYinWorld(self.x + 1, self.y + 1) and (self.world.isXYfree(self.x + 1, self.y + 1)) == False and (self.world.czyRoslina(self.world.getOrganizm(self.x + 1, self.y + 1)) == False):
            org = self.world.getOrganizm(self.x + 1, self.y + 1)
            if (org != None):
                self.world.komentator.komentujZabojstwoBarszczu(org)
                org.die()
        if self.world.isXYinWorld(self.x + 1, self.y - 1) and (self.world.isXYfree(self.x + 1, self.y - 1)) == False and (self.world.czyRoslina(self.world.getOrganizm(self.x + 1, self.y - 1)) == False):
            org = self.world.getOrganizm(self.x + 1, self.y - 1)
            if (org != None):
                self.world.komentator.komentujZabojstwoBarszczu(org)
                org.die()
        super().akcja()


    def kolizja(self, org):
        org.die()
        return super().kolizja(org)

    def getImage(self):
        return "images\\barszcz.png"

    def makeNew(self, x, y, turaPowst, world, sila = 10):
        return BarszczSosnowskiego(x, y, turaPowst, world, sila)


