from tkinter import *
from Kierunek import Kierunek
from Komentator import Komentator
from obslugaPliku import obslugaPliku

class Window:

    def keydown(self, e):
        print(e.keysym)
        if self.world.koniecGry == False:
            cz = self.world.getCzlowiek()
            if e.keysym == "Up":
                cz.kierunek = (Kierunek.GORA)
                self.world.wykonajTure()
                print("up")
                self.setFieldImages()
                #komentarze
            if e.keysym == "Down":
                cz.kierunek = (Kierunek.DOL)
                self.world.wykonajTure()
                print("down")
                self.setFieldImages()
            if e.keysym == "Left":
                cz.kierunek = (Kierunek.LEWO)
                self.world.wykonajTure()
                self.setFieldImages()
                print("left")
            if e.keysym == "Right":
                cz.kierunek = (Kierunek.PRAWO)
                self.world.wykonajTure()
                self.setFieldImages()
                print("right")
            self.printKom()


    def nextT(self):
        if self.world.koniecGry == False:
            cz = self.world.getCzlowiek()
            cz.kierunek = (Kierunek.NIC)
            self.world.wykonajTure()
            self.setFieldImages()
            self.printKom()

    def aktUm(self):
        if self.world.koniecGry == False:
            cz = self.world.getCzlowiek()
            cz.aktywujUmiejetnosc()
            self.printKom()
            
    def save(self):
        if self.world.koniecGry == False:
            self.obs.saveGame(self.world)
            self.world.komentator.komentujZapis()
            self.printKom()
            return #edit

    def load(self):
        self.obs.loadGame(self.world)
        self.world.koniecGry = False
        self.setFieldImages()
        self.world.komentator.komentujWczytanie()
        self.printKom()
        return
        #edit

    def __init__(self, world):
        self.world = world
        self.obs = obslugaPliku()
        self.root = Tk()
        self.win = Frame(self.root)
        self.root.title("vWorld")
        #self.iPole = [[Label(self.win, image=self.iEmpty).grid(row=i, column=j, sticky=W) for j in range(self.world.x)] for i in range(self.world.y)]
        self.alocPole()
        self.setFieldImages()
        self.win.bind("<KeyPress>", self.keydown)
        self.tCommentary = Text(self.win, width=50, height=30, wrap=WORD, background="white")
        self.tCommentary.grid(row=0, column=self.world.y+1, rowspan=self.world.y, sticky=E)
        self.tCommentary.delete(0.0, END)
        self.addButtons()
        self.win.focus_set()
        self.win.pack()
        self.win.mainloop()

    def addButtons(self):
        self.bNext = Button(self.win, text="Nastepna tura", width=10, command=self.nextT)
        self.bNext.grid(row=self.world.y, column=1, columnspan=5)
        self.bUm = Button(self.win, text="Aktywuj Umiejetnosc", width=16, command=self.aktUm)
        self.bUm.grid(row=self.world.y, column=5, columnspan=10)
        self.bSave = Button(self.win, text="Zapisz", width=10, command=self.save)
        self.bSave.grid(row=self.world.y, column=14, columnspan=5)
        self.bLoad = Button(self.win, text="Wczytaj", width=10, command=self.load)
        self.bLoad.grid(row=self.world.y, column=21, columnspan=5)

    def keyDown(e):
        print(e.char)

    def alocPole(self):
        self.iEmpty = PhotoImage(file="images\\empty.png")
        self.iPole = [0] * self.world.y
        for i in range(self.world.y):
            self.iPole[i] = [0] * self.world.x
        for i in range(self.world.y):
            for j in range(self.world.x):
                self.iPole[i][j] = Label(self.win, image=self.iEmpty)
                self.iPole[i][j].grid(row=i, column=j, sticky=W)


    def setFieldImages(self):
        for i in range(self.world.y):
            for j in range(self.world.x):
                org = self.world.getOrganizm(j, i)
                if org == None:
                    self.iPole[i][j].configure(image=self.iEmpty)
                    self.iPole[i][j].image = self.iEmpty
                else:
                    im = PhotoImage(file=org.getImage())
                    self.iPole[i][j].configure(image=im)
                    self.iPole[i][j].image = im

    def printKom(self):
        self.tCommentary.delete(0.0, END)
        for kom in self.world.komentator.komentarze:
            self.tCommentary.insert(END, kom+"\n")
        self.world.komentator.usunKomentarze()
                


        
