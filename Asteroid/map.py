from pygame import Vector2
from Asteroid.player import Player

import core


class Map:
    def __init__(self):
        self.maxPlayer=20
        self.maxFood=100
        self.taille=Vector2(core.WINDOW_SIZE)
        self.joueurs=[]
        self.food = []
        self.pieges = []

    def spawnFood(self):
        pass
    def spawnPlayer(self):
        pass

    def show(self):
        for elem in self.joueurs:
            elem.show()

    def addJoueur(self,p):
        if len(self.joueurs)<self.maxPlayer:
            self.joueurs.append(p)