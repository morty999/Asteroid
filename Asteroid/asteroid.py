import random
import time

from pygame import Vector2
import core


class Asteroid:
    def __init__(self, level=None, pos=None, vel=None, rotation=0):
        self.spawnTime = time.time()
        self.protected = True
        self.protectedTime = 1
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 3)
        self.size = 20 * self.level
        self.acc = Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        if rotation != 0:
            self.acc = self.acc.rotate(rotation)
        if vel:
            self.vel = Vector2(vel)
        else:
            self.vel = Vector2()
        if pos:
            self.pos = Vector2(pos)
        else:
            zone = random.randint(1, 4)
            if zone == 1:
                self.pos = Vector2(1, random.randint(1, core.WINDOW_SIZE[1]))
            elif zone == 2:
                self.pos = Vector2(random.randint(1, core.WINDOW_SIZE[0]), 1)
            elif zone == 3:
                self.pos = Vector2(core.WINDOW_SIZE[0]-1, random.randint(0, core.WINDOW_SIZE[1]))
            else:
                self.pos = Vector2(random.randint(0, core.WINDOW_SIZE[0]), core.WINDOW_SIZE[1]-1)
        self.nbPoints = random.randint(8, 13)
        self.listePoints = []
        for i in range(self.nbPoints):
            x = random.randint(int(self.size/5*2), self.size)
            y = random.randint(int(self.size/5*2), self.size)
            r = (360/self.nbPoints)*i
            point = Vector2(x, y).rotate(r)
            self.listePoints.append(point)


    def show(self):
        drawListePoints=[]
        for i in range(self.nbPoints):
            drawListePoints.append(self.listePoints[i]+self.pos)
        for pts in drawListePoints:
            pts.rotate(50)
        core.Draw.polygon((170, 170, 170), drawListePoints)

    def show_old(self):
        core.Draw.circle((255, 255, 255), self.pos, self.size)

    def update(self):
        self.vel += self.acc
        # gestion des bordures
        if self.pos.x <= 0:
            self.pos.x = core.WINDOW_SIZE[0]
        elif self.pos.x >= core.WINDOW_SIZE[0]:
            self.pos.x = 10
        elif self.pos.y <= 0:
            self.pos.y = core.WINDOW_SIZE[1]
        elif self.pos.y >= core.WINDOW_SIZE[1]:
            self.pos.y = 10
        self.pos += self.vel
        self.acc = (0, 0)

        if self.protected:
            if time.time() - self.spawnTime > self.protectedTime:
                self.protected = False

