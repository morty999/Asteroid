import pygame
import core
from Asteroid.game import Game


def setup():
    print("start setup")
    core.WINDOW_SIZE = [800, 600]
    core.fps = 30
    core.memory("game", Game())
    print("end setup")


def run():
    core.cleanScreen()
    core.memory("game").update()


core.main(setup, run)
