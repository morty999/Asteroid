import random
from pygame import Vector2
import core


class Asteroid:
    def __init__(self, level=None, pos=None, vel=None, rotation=0):
        if level:
            self.level = level
        else:
            self.level = random.randint(1,3)
        self.size = 20 * self.level
        self.acc = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        if rotation != 0:
            self.acc = self.acc.rotate(rotation)
        if vel:
            self.vel = Vector2(vel)
        else:
            self.vel = Vector2()
        if pos:
            self.pos = Vector2(pos)
        else:
            self.pos = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.nbPoints = random.randint(8, 15)
        self.listePoints = []
        for i in range(self.nbPoints):
            point = Vector2(random.randint(self.size/4,self.size),random.randint(self.size/4,self.size)).rotate((360/self.nbPoints)*i)
            self.listePoints.append(point)

    def show(self):
        drawListePoints=[]
        for i in range(self.nbPoints):
            drawListePoints.append(self.listePoints[i]+self.pos)
        core.Draw.polygon((255,255,255), drawListePoints)

    def show_old(self):
        core.Draw.circle((255,255,255), self.pos, self.size)
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
