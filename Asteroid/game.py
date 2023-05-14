import time

import pygame

import core
from Asteroid.map import Map
from Asteroid.player import Player
from Asteroid.menu import MainMenu

class Game:
    def __init__(self):
        pygame.init()
        self.mainMenu = MainMenu(self)
        self.map = Map()
        #Etats
        self.running, self.playing, self.pauseMenu = True, False, False
        #Input utilisateur
        self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False
        self.SPACE_KEY, self.START_KEY, self.BACK_KEY = False, False, False
        #self.font_name = 'Nom'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)


    def update(self):
        self.check_events()

        if self.playing:
            self.game_loop()

        elif self.pauseMenu:
            pass

        else:
            self.menu_loop()

    def menu_loop(self):
        #core.Draw.text((255,255,255), "MAIN MENU", (10,0))
        self.mainMenu.display_menu()
        '''
        self.reset_keys()

        self.mainMenu.move_cursor()
        self.mainMenu.check_input()
        '''

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
            self.map.createProj(self.map.player.vel, self.map.player.pos, self.map.player.rotation)
        self.map.update()
        self.map.show()
                
    def check_events(self):     # Permet de gérer les evennements pygame (set et reset les touches utilisateur)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing, self.mainMenu, self.pauseMenu = False, False, False, False
                self.mainMenu.run_display = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_s:
                    self.DOWN_KEY = True
                if event.key == pygame.K_z:
                    self.UP_KEY = True
                if event.key == pygame.K_q:
                    self.LEFT_KEY = True
                if event.key == pygame.K_d:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = False
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = False
                if event.key == pygame.K_s:
                    self.DOWN_KEY = False
                if event.key == pygame.K_z:
                    self.UP_KEY = False
                if event.key == pygame.K_q:
                    self.LEFT_KEY = False
                if event.key == pygame.K_d:
                    self.RIGHT_KEY = False
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = False

    def reset_keys(self):
        self.START_KEY, self.BACK_KEY, self.DOWN_KEY, self.UP_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.SPACE_KEY = False, False, False, False, False, False, False,
