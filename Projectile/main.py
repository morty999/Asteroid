import random
import time

from pygame import Vector2

import core
from Projectile.projectile import Projectile


def setup():
    print("Setup START---------")
    core.fps = 30

    core.WINDOW_SIZE = [800, 800]

    core.memory("mesProjectiles", [])

    print("Setup END-----------")


def createProj(pos):
    proj = Projectile()
    proj.position = Vector2(pos)
    proj.accel = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    core.memory('mesProjectiles').append(proj)


def run():
    core.cleanScreen()
    if core.getMouseLeftClick():
        if (len(core.memory('mesProjectiles')) == 0) or time.time() - core.memory("mesProjectiles")[-1].startTime > 0.2:
            createProj(core.getMouseLeftClick())

    for p in core.memory('mesProjectiles'):
        if time.time() - p.startTime > p.lifeTime:
            core.memory("mesProjectiles").remove(p)

    for p in core.memory('mesProjectiles'):
        p.deplacement()
        p.draw()


core.main(setup, run)
