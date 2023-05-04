import random
from pygame import Vector2

import core


class Player:
        def __init__(self):
            self.IsBot = True
            self.Name = "Bob"
            self.UUID = random.randint(1000000, 9000000)
            self.mass = 10
            self.VMax = 10
            self.AccMax = 5
            self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
            self.acc = Vector2(0,0)
            self.vitesse = Vector2(0, 0)
            self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        def deplacement(self):
            pass


        def grandir(self):
            pass

        def evaporation(self):
            pass
        def show(self):
            core.Draw.circle(self.couleur,self.position,self.mass)