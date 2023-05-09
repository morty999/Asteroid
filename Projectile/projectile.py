import time

from pygame import Vector2

import core


class Projectile:
    def __init__(self):
        self.taille = 5
        self.accel = Vector2()
        self.vitesse = Vector2()
        self.position = Vector2()
        self.lifeTime = 3
        self.startTime = time.time()

    def draw(self):
        core.Draw.circle((255,255,255), self.position, self.taille)

    def deplacement(self):
        self.vitesse += self.accel
        self.position += self.vitesse

    def destruction(self):
        pass

    def collision(self):
        pass