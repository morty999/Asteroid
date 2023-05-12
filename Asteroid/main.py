import time

import pygame
import core
from Asteroid.game import Game


def setup():
    print("start setup")
    core.WINDOW_SIZE = [1440, 900]
    core.fps = 60
    core.memory("load", False)
    print("end setup")


def run():
    t=time.time()
    if core.memory("load")==False:
        core.memory("game", Game())
        core.memory("load", True)
    core.cleanScreen()
    core.memory("game").update()
    print(time.time()-t)
core.main(setup, run)
