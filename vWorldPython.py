from World import World
from Organizm import Organizm
from Roslina import Roslina
from Trawa import Trawa
from Wilk import Wilk
from Zwierze import Zwierze
print("Hello")
for i in range(10):
	print(i)
print("Hello")
w = World(20, 15)
w.printPola()
#o = Organizm(0,0,10,2,1,3,True,w);
#r = Roslina(0,0,4,5,0,3,True,w);
t = Trawa(0,0,1,w)
wi = Wilk(1, 1, 1, w)
w.dodajOrganizm(t.makeNew(1,1,1,w))
newWorld = World(20, 20)
if type(wi).__base__.__name__ == Zwierze.__name__:
    print(1)
newWorld.zyj()
print(1)