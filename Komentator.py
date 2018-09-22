from Roslina import Roslina
class Komentator:
    """description of class"""
    def __init__(self, world):
        self.world = world
        self.komentarze = list()
        self.dodajKomentarz("Powstal nowy swiat!")

    def dodajKomentarz(self, kom):
        self.komentarze.append(kom)

    def komentujWalke(self, orgWin, orgLost):
        win = type(orgWin).__name__
        lost = type(orgLost).__name__
        if type(orgWin).__base__.__name__ == Roslina.__name__:
            kom = lost + " zjada " + win + " i umiera"
        elif type(orgLost).__base__.__name__ == Roslina.__name__:
            kom = win + " zjada " + lost
        else:
            kom = lost + " polegl w walce z " + win
        self.dodajKomentarz(kom)

    def komentujRozmnazanie(self, org):
        roz = type(org).__name__
        kom = roz + " rozmnozyl sie"
        self.dodajKomentarz(kom)

    def komentujZasianie(self, org):
        roz = type(org).__name__
        kom = roz + " zasial nowa rosline"
        self.dodajKomentarz(kom)

    def komentujSmierc(self):
        self.dodajKomentarz("Gracz umarl, koniec gry")

    def komentujUcieczkeAntylopy(self):
        self.dodajKomentarz("Antylopa ucieka przed walka")

    def komentujZabojstwoBarszczu(self, org):
        dead = type(org).__name__
        kom = "Barszcz Sosnowskiego zabija " + dead
        self.dodajKomentarz(kom)

    def komentujOdbicieAtaku(self, orgA, orgB):
        a = type(orgA).__name__
        b = type(orgB).__name__
        kom = b + " odbija atak " + a
        self.dodajKomentarz(kom)

    def komentujAktywacjeUm(self):
        self.dodajKomentarz("Gracz aktywowal umiejetnosc specjalna, posiada teraz 10 sily")

    def komentujZapis(self):
        self.dodajKomentarz("Zapisano gre")

    def komentujWczytanie(self):
        self.dodajKomentarz("Wczytano gre")

    def usunKomentarze(self):
        self.komentarze.clear()

