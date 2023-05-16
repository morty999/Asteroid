import random
import time

from pygame import Vector2

import core
from Asteroid.projectile import Projectile


class Enemy:
    def __init__(self):
        self.destroyed = False
        self.shotCD = 3
        self.projectiles = []
        self.lasMoveTime = time.time()
        self.moveCD = random.uniform(1, 3)
        self.maxSpeed = 6
        self.rotation = 0
        self.decel = 0.99
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
        if time.time() - self.lasMoveTime > self.moveCD:
            self.acc = Vector2(random.randint(3, 6), 0).rotate(random.randint(1,360))
            self.lasMoveTime = time.time()
            self.moveCD = random.uniform(1, 3)
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

        # check projectiles lifespan
        for p in self.projectiles:
            if time.time() - p.startTime > p.lifeTime:
                self.projectiles.remove(p)

        # update all projectiles
        for elem in self.projectiles:
            elem.update()

    def show(self):
        for elem in self.projectiles:
            elem.show()
        self.sprite.show()

    def createProj(self,player):
        # si le temps depuis le dernier tir est supérieur au cooldown entre deux tir, on crée un nouveau projectile
        if (len(self.projectiles) == 0) or ((time.time() - self.projectiles[-1].startTime) > self.shotCD):
            proj = Projectile()
            proj.size = 5
            proj.pos = Vector2(self.pos)
            proj.acc = Vector2(player - self.pos).normalize()*10
            proj.lifeTime = 3
            self.projectiles.append(proj)