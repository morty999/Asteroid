import pygame
import core
from Asteroid.game import Game


def setup():
    print("start setup")
    core.WINDOW_SIZE = [1440, 900]
    core.fps = 60
    core.memory("game", Game())
    print("end setup")


def run():
    core.cleanScreen()
    core.memory("game").update()


core.main(setup, run)
