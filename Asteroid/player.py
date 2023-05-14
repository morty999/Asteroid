import random
import time

from pygame import Vector2

import core
from Asteroid.projectile import Projectile


class Player:
    def __init__(self):
        self.projectiles = []
        self.shotCD = 0.2
        self.maxSpeed = 6
        self.maxAcc = 2
        self.rotation = 0
        self.decel = 0.98
        self.vies = 5
        self.pos = Vector2(core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2)
        self.acc = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.color = (255, 255, 255)

    def avancer(self):
        self.acc += Vector2(0, 1).rotate(self.rotation)

    def reculer(self):
        self.acc += Vector2(0, -1).rotate(self.rotation)

    def tournerGauche(self):
        # self.acc += Vector2(-1, 0)
        self.rotation -= 270 / core.fps

    def tournerDroite(self):
        # self.acc += Vector2(1, 0)
        self.rotation += 270 / core.fps

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

        # check projectiles lifespan
        for p in self.projectiles:
            if time.time() - p.startTime > p.lifeTime:
                self.projectiles.remove(p)

        for elem in self.projectiles:
            elem.update()

    def show(self):
        for elem in self.projectiles:
            elem.show()
        # a = 0 - self.vel.angle_to(Vector2(0, 1))
        p1 = self.pos + Vector2(-7, -5).rotate(self.rotation)
        p2 = self.pos + Vector2(0, 15).rotate(self.rotation)
        p3 = self.pos + Vector2(7, -5).rotate(self.rotation)
        p4 = self.pos + Vector2(0, 0).rotate(self.rotation)

        core.Draw.polygon(self.color, ((p1), (p2), (p3), (p4)))

    def createProj(self, vel, pos, rotation):
        # si le temps depuis le dernier tir est supérieur au cooldown entre deux tir, on crée un nouveau projectile
        if (len(self.projectiles) == 0) or ((time.time() - self.projectiles[-1].startTime) > self.shotCD):
            proj = Projectile()
            proj.pos = Vector2(pos)
            proj.acc = proj.acc.rotate(rotation)        #applique la rotation au vecteur d'acceleration du projectile
            proj.acc += vel                             #ajoute le vecteur de vitesse actuel du vaisseau à l'acceleration du projectile
            self.projectiles.append(proj)
