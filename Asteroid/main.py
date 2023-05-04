import pygame
import core
from Asteroid.partie import Partie


def setup():
    print("start setup")
    core.WINDOW_SIZE=[800,600]
    core.fps =60

    core.memory("partie",Partie())
    core.memory("partie").addPlayer()
    print("end setup")

def run():
    print("start run")
    core.cleanScreen()
    core.printMemory()
    core.memory("partie").show()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:

    if keys[pygame.K_DOWN]:

    if keys[pygame.K_LEFT]:

    if keys[pygame.K_RIGHT]:

    print("end run")

core.main(setup,run)