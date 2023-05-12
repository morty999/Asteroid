import random
import time
import core
from pygame import Vector2

from Asteroid.asteroid import Asteroid
from Asteroid.player import Player
from Asteroid.projectile import Projectile


class Map:
    def __init__(self):
        self.level=1                                         #Niveau de la partie
        self.initAsteroidDone = False
        self.maxAsteroid = 3 + 2 * self.level
        self.size = Vector2(core.WINDOW_SIZE)
        self.asteroid = []
        self.enemy = []
        self.projectiles = []
        self.player = Player()
        #Game values
        self.shot_CD = 0.2
        self.score = 0
        self.color_white = (255,255,255)

    def show(self):
        for elem in self.asteroid:
            elem.show()
        #for elem in self.enemy:
            #elem.show()
        for elem in self.projectiles:
            elem.show()
        self.player.show()
        core.Draw.text(self.color_white, "Score: " + str(self.score),(10,0))
        for i in range(0, self.player.vies):
            p1 = (10 + (30*i), 60)
            p2 = (20 + (30*i), 35)
            p3 = (30 + (30*i), 60)
            p4 = (20 + (30 * i), 50)
            core.Draw.polygon(self.color_white, ((p1), (p2), (p3), (p4)))

    def update(self):
        #check projectiles lifespan
        for p in self.projectiles:
            if time.time() - p.startTime > p.lifeTime:
                self.projectiles.remove(p)

        #Update all elements from the map
        for elem in self.asteroid:
            elem.update()
        #for elem in self.enemy:
            #elem.update()
        for elem in self.projectiles:
            elem.update()
        self.player.update()
        self.initAsteroid()
        self.checkCollision()

    def createProj(self, vel, pos, rotation):
        # si le temps depuis le dernier tir est supérieur au cooldown entre deux tir, on crée un nouveau projectile
        if (len(self.projectiles) == 0) or ((time.time() - self.projectiles[-1].startTime) > self.shot_CD):
            proj = Projectile()
            proj.pos = Vector2(pos)
            #a = 0 - vel.angle_to(Vector2(0, 1)) #permet de déterminer l'angle de tir du projectile
            proj.acc = proj.acc.rotate(rotation)       #applique la rotation au vecteur d'acceleration du projectile
            proj.acc += vel                     #ajoute le vecteur de vitesse actuel du vaisseau à l'acceleration du projectile
            self.projectiles.append(proj)

    def initAsteroid(self):
        if not self.initAsteroidDone:
            for i in range(self.maxAsteroid):
                self.spawnAsteroidV2()
            self.initAsteroidDone = True

    def spawnAsteroid(self, level=None, pos=None):
        aste = Asteroid()
        if level:
            aste.level = level
        else:
            aste.level = random.randint(1, 3)
        aste.size *= aste.level
        if pos:
            aste.pos = pos
        self.asteroid.append(aste)

    def spawnAsteroidV2(self):
        aste = Asteroid()
        self.asteroid.append(aste)

    def splitAsteroid(self,aste):
        aste1 = Asteroid(aste.level-1, aste.pos, aste.vel, 90)
        self.asteroid.append(aste1)
        aste2 = Asteroid(aste.level-1, aste.pos, aste.vel, 270)
        self.asteroid.append(aste2)

    def checkCollision(self):
        for aste in self.asteroid:
            for proj in self.projectiles:
                if (abs(aste.pos.x - proj.pos.x) < aste.size) and (abs(aste.pos.y - proj.pos.y) < aste.size) :
                    self.projectiles.remove(proj)
                    if aste.level != 1:
                        self.splitAsteroid(aste)
                    self.asteroid.remove(aste)


