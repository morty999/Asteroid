import random
import time

from pygame import Vector2

import core
from Asteroid.projectile import Projectile


class Player:
    def __init__(self):
        self.immunity = True
        self.immunityStart = time.time()
        self.immunityDuration = 2
        self.projectiles = []
        self.shotCD = 0.3
        self.maxSpeed = 6
        self.maxAcc = 2
        self.rotation = 0
        self.decel = 0.98
        self.vies = 5
        self.pos = Vector2(core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2)
        self.acc = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.color_white = (255, 255, 255)
        self.color_NeonBlue = (0, 219, 255)
        #gestion bonus
        self.bonusSpeed, self.bonusProjNumber, self.bonusProjSize, self.bonusProjLevel, self.bomb = 1, 1, 1, 1, 2
        self.lastBombTime = time.time()

    def avancer(self):
        self.acc += Vector2(0, 1).rotate(self.rotation)

    def reculer(self):
        self.acc += Vector2(0, -1).rotate(self.rotation)

    def tournerGauche(self):
        # self.acc += Vector2(-1, 0)
        self.rotation -= 225 / core.fps

    def tournerDroite(self):
        # self.acc += Vector2(1, 0)
        self.rotation += 225 / core.fps

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

        if self.immunity and (time.time() - self.immunityStart > self.immunityDuration):
            self.immunity = False

    def show(self):
        for elem in self.projectiles:
            elem.show()
        # a = 0 - self.vel.angle_to(Vector2(0, 1))
        p1 = self.pos + Vector2(-7, -5).rotate(self.rotation)
        p2 = self.pos + Vector2(0, 15).rotate(self.rotation)
        p3 = self.pos + Vector2(7, -5).rotate(self.rotation)
        p4 = self.pos + Vector2(0, 0).rotate(self.rotation)
        core.Draw.polygon(self.color_white, (p1, p2, p3, p4))
        p1 = self.pos + Vector2(-9, -7).rotate(self.rotation)
        p2 = self.pos + Vector2(0, 17).rotate(self.rotation)
        p3 = self.pos + Vector2(9, -7).rotate(self.rotation)
        p4 = self.pos + Vector2(0, -2).rotate(self.rotation)
        core.Draw.polyline(self.color_NeonBlue, (p1, p2, p3, p4), 3)

    def createProj(self):
        rota = self.rotation
        # si le temps depuis le dernier tir est supérieur au cooldown entre deux tir, on crée un nouveau projectile
        if (len(self.projectiles) == 0) or ((time.time() - self.projectiles[-1].startTime) > self.shotCD):
            for i in range(0, self.bonusProjNumber):
                if i % 2 == 0:
                    rota += 15*i
                else:
                    rota -= 15*i
                proj = Projectile()
                proj.size = 1 + 2 * self.bonusProjSize
                proj.life = self.bonusProjLevel
                proj.color = (0, 219, 255)
                proj.pos = Vector2(self.pos)
                proj.acc = proj.acc.rotate(rota)                #applique la rotation au vecteur d'acceleration du projectile
                proj.acc += self.vel                            #ajoute le vecteur de vitesse actuel du vaisseau à l'acceleration du projectile
                self.projectiles.append(proj)

    def createBomb(self):
        rota = self.rotation
        if self.bomb > 1 and (time.time() - self.lastBombTime > 5):
            for i in range(0, 24):
                rota += 15*i
                proj = Projectile()
                proj.size = 1 + 2 * self.bonusProjSize
                proj.life = self.bonusProjLevel
                proj.color = (0, 219, 255)
                proj.pos = Vector2(self.pos)
                proj.acc = proj.acc.rotate(rota)
                self.projectiles.append(proj)
            self.bomb -= 1
            self.lastBombTime = time.time()

    def kill(self):
        self.pos = Vector2(core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2)
        self.vies -= 1
        self.immunity = True
        self.immunityStart = time.time()