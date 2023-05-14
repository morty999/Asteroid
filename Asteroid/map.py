import random
import time
import core
from pygame import Vector2

from Asteroid.asteroid import Asteroid
from Asteroid.enemy import Enemy
from Asteroid.player import Player
from Asteroid.projectile import Projectile


class Map:
    def __init__(self):
        self.background = core.Texture("textures/bg_2.jpg", Vector2(0,0), 0, (core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))
        self.background.load()
        self.level = 1                                         # Niveau de la partie
        self.initAsteroidDone = False
        self.maxAsteroid = 7 + 3 * self.level
        self.maxEnemy = 2
        self.size = Vector2(core.WINDOW_SIZE)
        self.asteroid = []
        self.enemy = []
        self.player = Player()
        self.color_white = (255, 255, 255)
        # Game values
        self.spawnAsteCD = 3
        self.spawnEnemyCD = 10
        self.score = 0
        self.startTime = time.time()
        self.elapsedTime = time.time()



    def show(self):
        if self.background.ready:
            self.background.show()
        for elem in self.asteroid:
            elem.show()
        for elem in self.enemy:
            elem.show()
        self.player.show()
        core.Draw.text(self.color_white, "Score: " + str(self.score), (10, 0))
        core.Draw.text(self.color_white, "Time: " + str(int(self.elapsedTime)), (10, 100))
        for i in range(0, self.player.vies):
            p1 = (10 + (30*i), 60)
            p2 = (20 + (30*i), 35)
            p3 = (30 + (30*i), 60)
            p4 = (20 + (30*i), 50)
            core.Draw.polygon(self.color_white, ((p1), (p2), (p3), (p4)))

    def update(self):
        self.elapsedTime = time.time() - self.startTime
        # check time since last asteroid
        if len(self.asteroid) > 0 and (time.time() - self.asteroid[-1].spawnTime > self.spawnAsteCD):
            self.spawnAsteroidV2()
        if len(self.enemy) == 0 or (len(self.enemy) < self.maxEnemy and (time.time() - self.enemy[-1].spawnTime > self.spawnEnemyCD)):
            self.spawnEnemy()
        # Update all elements from the map
        for elem in self.asteroid:
            elem.update()
        for elem in self.enemy:
            elem.update()
            elem.createProj(self.player.pos)
        self.player.update()
        self.initAsteroid()
        self.checkCollision()
        # self.PurgeAsteroid()

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

    def spawnEnemy(self):
        ene = Enemy()
        self.enemy.append(ene)

    def splitAsteroid(self,aste):
        aste1 = Asteroid(aste.level-1, aste.pos, aste.vel, 90)
        self.asteroid.append(aste1)
        aste2 = Asteroid(aste.level-1, aste.pos, aste.vel, 270)
        self.asteroid.append(aste2)

    def checkCollision(self):
        for aste in self.asteroid:
            if not aste.protected:
                for proj in self.player.projectiles:
                    if (abs(aste.pos.x - proj.pos.x) < (aste.size + (proj.size/2)))\
                            and (abs(aste.pos.y - proj.pos.y) < (aste.size + (proj.size/2))):
                        self.player.projectiles.remove(proj)
                        if aste.level != 1:
                            self.splitAsteroid(aste)
                        self.score += (4 - aste.level) * 100
                        self.asteroid.remove(aste)

            if (abs(aste.pos.x - self.player.pos.x)) < aste.size and (abs(aste.pos.y - self.player.pos.y) < aste.size):
                self.player.pos = Vector2(core.WINDOW_SIZE[0]/2, core.WINDOW_SIZE[1]/2)
                self.player.vies -= 1
                if aste.level != 1:
                    self.splitAsteroid(aste)
                self.asteroid.remove(aste)

        for enemy in self.enemy:
            for proj in enemy.projectiles:
                if (abs(self.player.pos.x - proj.pos.x) < (8 + (proj.size / 2))) \
                        and (abs(self.player.pos.y - proj.pos.y) < (8 + (proj.size / 2))):
                    enemy.projectiles.remove(proj)
                    self.player.pos = Vector2(core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2)
                    self.player.vies -= 1
            for proj in self.player.projectiles:
                if (abs(enemy.pos.x - proj.pos.x) < (8 + (proj.size / 2))) \
                        and (abs(enemy.pos.y - proj.pos.y) < (8 + (proj.size / 2))):
                    enemy.projectiles.remove(proj)



'''
            for aster in self.asteroid:
                if aste != aster:
                    if (abs(aste.pos.x - aster.pos.x) < ((aste.size/2) + (aster.size/2))) and (abs(aste.pos.y - aster.pos.y) < ((aste.size/2) + (aster.size/2))):
                        if not aste.protected:
                            if aste.level != 1:
                                self.splitAsteroid(aste)
                            aste.destroyed = True
                        if not aster.protected:
                            if aster.level != 1:
                                self.splitAsteroid(aster)
                            aster.destroyed = True
                break

    def PurgeAsteroid(self):
        for aste in self.asteroid:
            if aste.destroyed:
                self.asteroid.remove(aste)
'''