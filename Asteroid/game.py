import time

import pygame
from Asteroid.map import Map
from Asteroid.player import Player

class Game:
    def __init__(self):
        self.map = Map()
        #Etats
        self.running, self.playing = True, False
        #Imput utilisateur
        self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False
        self.SPACE_KEY, self.START_KEY, self.BACK_KEY = False, False, False


    def show(self):
        pass

    def update(self):
        self.check_events()
        self.game_loop()


    def game_loop(self):        # Permet de gérer la boucle de jeu
        if self.UP_KEY:
            self.map.player.avancer()
        if self.DOWN_KEY:
            self.map.player.reculer()
        if self.LEFT_KEY:
            self.map.player.tournerGauche()
        if self.RIGHT_KEY:
            self.map.player.tournerDroite()
        if self.SPACE_KEY:
            self.map.createProj(self.map.player.vel, self.map.player.pos)
        self.map.update()
        self.map.show()
                
    def check_events(self):     # Permet de gérer les evennements pygame (set et reset les touches utilisateur)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                # self.curr_menu.run_display = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = False
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = False
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = False
                if event.key == pygame.K_UP:
                    self.UP_KEY = False
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = False
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = False
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = False


