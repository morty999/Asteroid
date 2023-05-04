from agario.map import Map
from agario.player import Player

class Partie:
    def __init__(self):
        self.map=Map()

    def show(self):
        self.map.show()

    def addBots(self):
        for i in range(0,self.map.maxPlayer):
            self.map.addJoueur(Player())

    def addPlayer(self):
        p = Player()
        p.IsBot = False
        self.map.addJoueur(p)
