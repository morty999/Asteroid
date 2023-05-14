import random
import time

from pygame import Vector2

import core


class Enemy:
    def __init__(self):
        self.spawnTime = time.time()
        self.maxSpeed = 6
        self.maxAcc = 2
        self.rotation = 0
        self.decel = 0.995
        self.vies = 1
        zone = random.randint(1, 4)
        if zone == 1:       # haut
            self.pos = Vector2(1, random.randint(1, core.WINDOW_SIZE[1]))
            self.acc = Vector2(random.randint(3, 6),0).rotate(270)
        elif zone == 2:     # gauche
            self.pos = Vector2(random.randint(1, core.WINDOW_SIZE[0]), 1)
            self.acc = Vector2(random.randint(3, 6), 0)
        elif zone == 3:     # droite
            self.pos = Vector2(core.WINDOW_SIZE[0]-1, random.randint(1, core.WINDOW_SIZE[1]))
            self.acc = Vector2(random.randint(3, 6), 0).rotate(180)
        else:               # bas
            self.pos = Vector2(random.randint(1, core.WINDOW_SIZE[0]), core.WINDOW_SIZE[1]-1)
            self.acc = Vector2(random.randint(3, 6), 0).rotate(90)
        self.vel = Vector2(0, 0)
        self.color = (255, 255, 255)
        self.sprite = core.Texture("textures/enemy1.png", Vector2(), 0, (60, 40))
        self.sprite.load()


    def update(self):
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
        self.sprite.pos = self.pos

    def show(self):
        self.sprite.show()
        '''
        # a = 0 - self.vel.angle_to(Vector2(0, 1))
        p1 = self.pos + Vector2(-7, -5).rotate(self.rotation)
        p2 = self.pos + Vector2(0, 15).rotate(self.rotation)
        p3 = self.pos + Vector2(7, -5).rotate(self.rotation)
        p4 = self.pos + Vector2(0, 0).rotate(self.rotation)

        core.Draw.polygon(self.color, ((p1), (p2), (p3), (p4)))
        '''