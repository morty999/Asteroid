import random
from pygame import Vector2
import core


class Asteroid:
    def __init__(self, level=None, pos=None, inverter=1):
        if level:
            self.level = level
        else:
            self.level = random.randint(1,3)
        self.size = 20 * self.level
        self.acc = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))*inverter
        self.vel = Vector2()
        if pos:
            self.pos = pos
        else:
            self.pos = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))

    def show(self):
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
