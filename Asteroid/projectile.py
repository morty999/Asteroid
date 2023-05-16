import time
from pygame import Vector2
import core


class Projectile:
    def __init__(self):
        self.size = 3
        self.acc = Vector2(0,10)
        self.vel = Vector2()
        self.pos = Vector2()
        self.lifeTime = 1
        self.life = 1
        self.startTime = time.time()
        self.color = (255,0,0)

    def show(self):
        core.Draw.circle(self.color, self.pos, self.size)

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


    def destruction(self):
        pass

    def collision(self):
        pass