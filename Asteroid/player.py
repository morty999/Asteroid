import random
from pygame import Vector2

import core


class Player:
        def __init__(self):
            self.maxSpeed = 6
            self.maxAcc = 2
            self.decel = 0.95
            self.vies = 5
            self.pos = Vector2(core.WINDOW_SIZE[0]/2, core.WINDOW_SIZE[1]/2)
            self.acc = Vector2(0, 0)
            self.vel = Vector2(0, 0)
            self.color = (255, 255, 255)

        def avancer(self):
            self.acc += Vector2(0, -1)

        def reculer(self):
            self.acc += Vector2(0, 1)

        def tournerGauche(self):
            self.acc += Vector2(-1, 0)

        def tournerDroite(self):
            self.acc += Vector2(1, 0)

        def update(self):
            # gestion si accel > accelMax
            if self.acc.length() > self.maxAcc:
                self.acc.scale_to_length(self.maxAcc)

            # gestion changement vitesse si acc non nulle sinon deceleration
            if self.acc.length() != 0:
                self.vel += self.acc
            else:
                self.vel *= self.decel

            # gestion si speed > speedMax
            if self.vel.length() > self.maxSpeed:
                self.vel.scale_to_length(self.maxSpeed)

            # reset vecteur accel
            self.acc = Vector2(0, 0)

            # gestion des dépassements de bordures d'écran
            if self.pos.x <= 0:
                self.pos.x = core.WINDOW_SIZE[0]
            elif self.pos.x >= core.WINDOW_SIZE[0]:
                self.pos.x = 10
            elif self.pos.y <= 0:
                self.pos.y = core.WINDOW_SIZE[1]
            elif self.pos.y >= core.WINDOW_SIZE[1]:
                self.pos.y = 10
            # déplacement par rapport à la vitesse
            self.pos += self.vel

        def show(self):
            a = 0 - self.vel.angle_to(Vector2(0, 1))
            p1 = self.pos + Vector2(-5, 0).rotate(a)
            p2 = self.pos + Vector2(0, 15).rotate(a)
            p3 = self.pos + Vector2(5, 0).rotate(a)

            core.Draw.polygon(self.color, ((p1), (p2), (p3)))