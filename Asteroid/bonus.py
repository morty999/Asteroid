import random
import time

from pygame import Vector2

import core


class Bonus:
    def __init__(self, pos):
        self.pos = Vector2(pos)
        self.size = 30
        self.startTime = time.time()
        '''
        Type
        1 = lifeUp
        2 = speedUp
        3 = projectileUp (number)
        4 = projectileUp (size)
        4 = projectileUp (life)
        5 = shieldProj (duration)
        6 = 
        '''
        self.type = random.randint(1, 5)
        self.lifeTime = 10
        self.colorRed = (255,0,5)
        self.colorBlue = (0,0,255)
        self.colorGreen = (0,255,0)
        self.colorYellow = (255,255,0)
        self.colorCyan = (0,255,255)
        self.colorPurple = (255,0,255)

    def show(self):
        if self.type == 1:
            core.Draw.circle(self.colorRed, self.pos, self.size, 5)
        elif self.type == 2:
            core.Draw.circle(self.colorBlue, self.pos, self.size, 5)
        elif self.type == 3:
            core.Draw.circle(self.colorGreen, self.pos, self.size, 5)
        elif self.type == 4:
            core.Draw.circle(self.colorYellow, self.pos, self.size, 5)
        elif self.type == 5:
            core.Draw.circle(self.colorCyan, self.pos, self.size, 5)
        elif self.type == 6:
            core.Draw.circle(self.colorPurple, self.pos, self.size, 5)


