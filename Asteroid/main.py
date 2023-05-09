import pygame
import core
from Asteroid.partie import Partie


def setup():
    print("start setup")
    core.WINDOW_SIZE=[800, 600]
    core.fps = 30

    core
    core.memory("partie",Partie())
    print("end setup")
    p= Partie()

def run():
    core.cleanScreen()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                core.memory('partie').map.player.avancer()
            if event.key == pygame.K_DOWN:
                core.memory('partie').map.player.reculer()
            if event.key == pygame.K_LEFT:
                core.memory('partie').map.player.tournerGauche()
            if event.key == pygame.K_RIGHT:
                core.memory('partie').map.player.tournerDroite()
            if event.key == pygame.K_SPACE:
                core.memory('partie').map.createProj(core.memory('partie').map.player.acc, core.memory('partie').map.player.pos)
    core.memory("partie").update()
    core.memory("partie").show()

core.main(setup,run)