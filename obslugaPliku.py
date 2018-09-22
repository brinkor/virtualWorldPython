class obslugaPliku:
    def __init__(self):
        self.fileName = "save.txt"

    def saveGame(self, world):
        self.file = open(self.fileName, "w")
        self.saveWorld(world)
        self.saveOrganizmy(world.organizmy)
        self.file.close()

    def loadGame(self, world):
        self.file = open(self.fileName, "r")
        self.loadWorld(world)
        self.loadOrg(world)
        self.file.close()

    def saveWorld(self, world):
        s = str(world.x) + " " + str(world.y) + " " + str(world.tura) + "\n"
        self.file.write(s)

    def saveOrganizmy(self, organizmy):
        for org in organizmy:
            self.file.write(org.saveData() + "\n")

    def loadWorld(self, world):
        s = self.file.readline()
        nums = s.split()
        world.nowaPlansza(int(nums[0]), int(nums[1]), int(nums[2]))

    def loadOrg(self, world):
        world.organizmy.clear()
        for line in self.file:
            nums = line.split()
            for org in world.organizmyPoczatkowe:
                if org.__class__.__name__ == nums[0]:
                    world.dodajOrganizm(org.loadData(nums))
                    break
