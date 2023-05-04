import random
from pygame import Vector2

import core


class Player:
        def __init__(self):
            self.IsBot = True
            self.VMax = 10
            self.AccMax = 5
            self.decel = 1
            self.vies = 5
            self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
            self.acc = Vector2(0,0)
            self.vitesse = Vector2(0, 0)
            self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        def avancer(self):
            pass

        def tournerGauche(self):
            pass

        def tournerDroite(self):
            pass

        def show(self):
            a = 0 - self.acc.angle_to(Vector2(0, 1))
            p1 = self.position + Vector2(-5, 0).rotate(a)
            p2 = self.position + Vector2(0, 15).rotate(a)
            p3 = self.position + Vector2(5, 0).rotate(a)

            core.Draw.polygon(self.couleur, ((p1), (p2), (p3)))