import random
import time
import core
from pygame import Vector2
from Asteroid.player import Player
from Asteroid.projectile import Projectile


class Map:
    def __init__(self):
        self.level=0                                         #Niveau de la partie
        self.maxAsteroid = 5 + 2 * self.level
        self.size = Vector2(core.WINDOW_SIZE)
        self.asteroid = []
        self.enemy = []
        self.projectiles = []
        self.player = Player()

    def show(self):
        #for elem in self.asteroid:
            #elem.show()
        #for elem in self.enemy:
            #elem.show()
        for elem in self.projectiles:
            elem.show()
        self.player.show()

    def update(self):
        #check projectiles lifespan
        for p in self.projectiles:
            if time.time() - p.startTime > p.lifeTime:
                self.projectiles.remove(p)

        #Update all elements from the map
        #for elem in self.asteroid:
            #elem.update()
        #for elem in self.enemy:
            #elem.update()
        for elem in self.projectiles:
            elem.update()
        self.player.update()

    def createProj(self,acc, pos):
        proj = Projectile()
        proj.pos = Vector2(pos)
        proj.acc = acc     #à modifier
        self.projectiles.append(proj)

    def spawnAsteroid(self):
        pass