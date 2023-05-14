import pygame

import core


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = core.WINDOW_SIZE[0]/2, core.WINDOW_SIZE[1]/2
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        self.font_color = (255,255,255)
        self.font_size = 50
        self.font_style = 'Arial'


    def draw_cursor(self):
        core.Draw.text(self.font_color, '*', (self.cursor_rect.x, self.cursor_rect.y),45, self.font_style)

    def blit_screen(self):
        self.game.window.blit_screen(self.game.display,(0,0))
        pygame.display.update()
        self.game.reset_keys()

    '''
       def draw_text(self, text, size, x, y):
            font = pygame.font.Font(self.font_name, size)
            text_surface = font.render(text, True, self.WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            self.display.blit(text_surface, text_rect)
    '''

class MainMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 70
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 140
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 210
        self.exitx, self.exity = self.mid_w, self.mid_h + 280
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.game.check_events()
        self.check_input()
        core.Draw.text(self.font_color, 'MAIN MENU', (core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2 - 20), self.font_size, self.font_style)
        core.Draw.text(self.font_color, 'START', (self.startx, self.starty), self.font_size, self.font_style)
        core.Draw.text(self.font_color, 'OPTIONS', (self.optionsx, self.optionsy), self.font_size, self.font_style)
        core.Draw.text(self.font_color, 'CREDITS', (self.creditsx, self.creditsy), self.font_size, self.font_style)
        core.Draw.text(self.font_color, 'EXIT', (self.exitx, self.exity), self.font_size, self.font_style)
        self.draw_cursor()

    def move_cursor (self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state='Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                pass
            elif self.state == 'Credits':
                pass
            elif self.state == 'Exit':
                pass
            self.run_display = False
