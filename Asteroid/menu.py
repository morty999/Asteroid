import time

import pygame
from pygame import Vector2
from Asteroid import game

import core
from Asteroid.map import Map


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h, self.indent_w, self.indent_h = core.WINDOW_SIZE[1] / 2, core.WINDOW_SIZE[0] / 2, 200, 200
        self.line_spacing = 70
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        self.offsetCursor = Vector2()
        self.font_color = (255, 255, 255)
        self.font_size = 50
        self.cursorLength = 390
        self.cursorHeight = self.font_size + 20
        self.text_font = 'font/Text_font.ttf'
        self.tile_font = 'font/Asteroid_font.ttf'
        self.italic_text_font = 'font/Text_font_bold_italic.ttf'
        self.game_over_font = 'font/Game_over_empty_font.ttf'
        self.cursorCD = 0.2
        self.lastCursorMove = time.time()

    def blit_screen(self):
        self.game.window.blit_screen(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def display_text(self, color, texte, position, taille=30, font='Arial'):
        pygame.font.init()
        myfont = pygame.font.Font(font, taille)
        textsurface = myfont.render(texte, False, color)
        if len(color) > 3:
            textsurface.set_alpha(color[3])
        core.screen.blit(textsurface, position)

    '''
       def draw_text(self, text, size, x, y):
            font = pygame.font.Font(self.font_name, size)
            text_surface = font.render(text, True, self.WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            self.display.blit(text_surface, text_rect)
    '''


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.titrex, self.titrey = self.mid_w, self.indent_h - 2 * self.line_spacing
        self.startx, self.starty = self.indent_w, self.indent_h + 2*self.line_spacing
        self.creditsx, self.creditsy = self.indent_w, self.indent_h + 3 * self.line_spacing
        self.exitx, self.exity = self.indent_w, self.indent_h + 4 * self.line_spacing
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.background = core.Texture("textures/mainBG.jpg", Vector2(0, 0), 0, (core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))
        self.background.load()

    def display_menu(self):
        if self.background.ready:
            self.background.show()
        self.game.check_events()
        self.check_input()
        self.display_text((51, 214, 255), 'ASTEROID', (self.titrex, self.titrey), 120, self.tile_font)
        self.display_text(self.font_color, 'START', (self.startx, self.starty), self.font_size, self.text_font)
        self.display_text(self.font_color, 'CREDITS', (self.creditsx, self.creditsy), self.font_size, self.text_font)
        self.display_text(self.font_color, 'EXIT', (self.exitx, self.exity), self.font_size, self.text_font)
        self.draw_cursor()


    def move_cursor(self):
        if time.time() - self.lastCursorMove > self.cursorCD:
            self.lastCursorMove = time.time()
            if self.game.DOWN_KEY:
                if self.state == 'Start':
                    self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                    self.state = 'Credits'
                elif self.state == 'Credits':
                    self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                    self.state = 'Exit'
                elif self.state == 'Exit':
                    self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                    self.state = 'Start'
                    pass

            elif self.game.UP_KEY:
                if self.state == 'Start':
                    self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                    self.state = 'Exit'
                elif self.state == 'Credits':
                    self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                    self.state = 'Start'
                elif self.state == 'Exit':
                    self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                    self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Credits':
                pass
            elif self.state == 'Exit':
                game.running, game.playing, game.mainMenu, game.pauseMenu = False, False, False, False
                game.mainMenu.run_display = False

    def draw_cursor(self):
        self.offsetCursor = Vector2(self.cursor_rect.x+60, self.cursor_rect.y-5)
        # def points rectangle Cursor
        p1 = self.offsetCursor
        p2 = self.offsetCursor + Vector2(self.cursorLength, 0)
        p3 = self.offsetCursor + Vector2(self.cursorLength, self.cursorHeight)
        p4 = self.offsetCursor + Vector2(0, self.cursorHeight)
        core.Draw.polyline((51, 214, 255), (p1, p2, p3, p4), 5)


class GameOver(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.titrex, self.titrey = self.mid_w, self.indent_h - 3 * self.line_spacing
        self.scorex,self.scorey = self.mid_w + 150, self.indent_h - self.line_spacing
        self.restartx, self.restarty = self.indent_w, self.indent_h + 2 * self.line_spacing
        self.exitx, self.exity = self.indent_w, self.indent_h + 3 * self.line_spacing
        self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)
        self.background = core.Texture("textures/GameOver.jpg", Vector2(0, 0), 0,(core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))
        self.background.load()

    def display_menu(self):
        if self.background.ready:
            self.background.show()
        self.game.check_events()
        self.check_input()
        self.display_text((255, 0, 0), 'Game Over', (self.titrex, self.titrey), 120, self.tile_font)
        self.display_text(self.font_color, 'Score: ' + str(self.game.map.score), (self.scorex, self.scorey), 80, self.tile_font)
        self.display_text(self.font_color, 'RESTART', (self.restartx, self.restarty), self.font_size, self.text_font)
        self.display_text(self.font_color, 'EXIT', (self.exitx, self.exity), self.font_size, self.text_font)
        self.draw_cursor()

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
                self.game.GameOver = False
                self.game.map = Map()
            elif self.state == 'Exit':
                game.running, game.playing, game.mainMenu, game.pauseMenu = False, False, False, False
                game.mainMenu.run_display = False

    def move_cursor(self):
        if time.time() - self.lastCursorMove > self.cursorCD:
            self.lastCursorMove = time.time()
            if self.game.DOWN_KEY:
                if self.state == 'Start':
                    self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                    self.state = 'Exit'
                elif self.state == 'Exit':
                    self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)
                    self.state = 'Start'

            elif self.game.UP_KEY:
                if self.state == 'Start':
                    self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                    self.state = 'Exit'
                elif self.state == 'Exit':
                    self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)
                    self.state = 'Start'

    def draw_cursor(self):
        self.offsetCursor = Vector2(self.cursor_rect.x + 60, self.cursor_rect.y - 5)
        # def points rectangle Cursor
        p1 = self.offsetCursor
        p2 = self.offsetCursor + Vector2(self.cursorLength, 0)
        p3 = self.offsetCursor + Vector2(self.cursorLength, self.cursorHeight)
        p4 = self.offsetCursor + Vector2(0, self.cursorHeight)
        core.Draw.polyline((255, 0, 0), (p1, p2, p3, p4), 5)

class Pause(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.titrex, self.titrey = self.mid_w + 150, self.indent_h - 3 * self.line_spacing
        self.scorex,self.scorey = self.mid_w + 150, self.indent_h - self.line_spacing
        self.restartx, self.restarty = self.indent_w, self.indent_h + 2 * self.line_spacing
        self.exitx, self.exity = self.indent_w, self.indent_h + 3 * self.line_spacing
        self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)
        self.background = core.Texture("textures/GameOver.jpg", Vector2(0, 0), 0,(core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))
        self.background.load()

    def display_menu(self):
        if self.background.ready:
            self.background.show()
        self.game.check_events()
        self.check_input()
        self.display_text((51, 214, 255), 'Pause', (self.titrex, self.titrey), 120, self.tile_font)
        self.display_text(self.font_color, 'Score: ' + str(self.game.map.score), (self.scorex, self.scorey), 80, self.tile_font)
        self.display_text(self.font_color, 'RESUME', (self.restartx, self.restarty), self.font_size, self.text_font)
        self.display_text(self.font_color, 'EXIT', (self.exitx, self.exity), self.font_size, self.text_font)
        self.draw_cursor()

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
                self.game.pause = False
            elif self.state == 'Exit':
                game.running, game.playing, game.mainMenu, game.pauseMenu = False, False, False, False
                game.mainMenu.run_display = False

    def move_cursor(self):
        if time.time() - self.lastCursorMove > self.cursorCD:
            self.lastCursorMove = time.time()
            if self.game.DOWN_KEY:
                if self.state == 'Start':
                    self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                    self.state = 'Exit'
                elif self.state == 'Exit':
                    self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)
                    self.state = 'Start'

            elif self.game.UP_KEY:
                if self.state == 'Start':
                    self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                    self.state = 'Exit'
                elif self.state == 'Exit':
                    self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)
                    self.state = 'Start'

    def draw_cursor(self):
        self.offsetCursor = Vector2(self.cursor_rect.x + 60, self.cursor_rect.y - 5)
        # def points rectangle Cursor
        p1 = self.offsetCursor
        p2 = self.offsetCursor + Vector2(self.cursorLength, 0)
        p3 = self.offsetCursor + Vector2(self.cursorLength, self.cursorHeight)
        p4 = self.offsetCursor + Vector2(0, self.cursorHeight)
        core.Draw.polyline((51, 214, 255), (p1, p2, p3, p4), 5)