import time

import pygame

import core
from Asteroid.map import Map
from Asteroid.player import Player
from Asteroid.menu import MainMenu, GameOver


class Game:
    def __init__(self):
        pygame.init()
        self.map = Map()
        self.mainMenu = MainMenu(self)
        self.GOMenu = GameOver(self)
        self.GameOver = False
        #Etats
        self.running, self.playing, self.pauseMenu = True, False, False
        #Input utilisateur
        self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False
        self.SPACE_KEY, self.SPECIAL_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        #self.font_name = 'Nom'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0,0,0), (255, 255, 255)


    def update(self):
        self.check_events()
        print(self.playing)
        print(self.GameOver)
        if self.playing:
            self.game_loop()

        else:
            self.menu_loop()

    def menu_loop(self):
        if GameOver is True:
            self.GOMenu.display_menu()
        else:
            self.mainMenu.display_menu()

        self.reset_keys()
        '''
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
            self.map.player.createProj()
        if self.SPECIAL_KEY:
            self.map.player.createBomb()
        if self.map.player.vies <= 0:
            self.playing = False
            self.GameOver = True
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
                if event.key == pygame.K_f:
                    self.SPECIAL_KEY = True
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
                if event.key == pygame.K_f:
                    self.SPECIAL_KEY = False
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = False

    def reset_keys(self):
        self.START_KEY, self.BACK_KEY, self.DOWN_KEY, self.UP_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.SPACE_KEY = False, False, False, False, False, False, False,
