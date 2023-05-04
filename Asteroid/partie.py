from Asteroid.map import Map
from Asteroid.player import Player

class Partie:
    def __init__(self):
        self.map=Map()

    def show(self):
        self.map.show()

    def addPlayer(self):
        p = Player()
        p.IsBot = False
        self.map.addJoueur(p)
