import time

import pygame
import core
from Asteroid.game import Game


def setup():
    print("start setup")
    core.WINDOW_SIZE = [1600, 900]
    core.fps = 60
    core.memory("load", False)
    core.memory("meanTime", 0)
    core.memory("sumTime", 0)
    core.memory("FrameCPT", 1)
    print("end setup")


def run():
    t = time.time()
    if core.memory("load")==False:
        core.memory("game", Game())
        core.memory("load", True)
    core.cleanScreen()
    core.memory("game").update()
    core.memory("meanTime", (core.memory("sumTime")+time.time()-t)/core.memory("FrameCPT"))
    print(core.memory("meanTime"))


core.main(setup, run)
