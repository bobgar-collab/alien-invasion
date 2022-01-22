import sys

import pygame

import alien_invasion as ai
from button import Button


class Menu:
    def __init__(self, ai_game: ai.AlienInvasion):
        self.ai_game = ai_game
        self.stats = ai_game.stats
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # self.bg_image = pygame.image.load(self.settings.bg_image_path)
        self.bg_image = pygame.image.load("images/menu.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen.get_rect().w, self.screen.get_rect().h))
        self.rect_a = self.screen.get_rect()

        screenCenterX, screenCenterY = self.screen.get_rect().center
        w = 250
        h = 50
        play_button_pos = (screenCenterX, screenCenterY - 50)
        exit_button_pos = (screenCenterX, screenCenterY + 50)
        self.play_button = Button(self, "Play Now", w, h, play_button_pos)
        self.exit_button = Button(self, "Exit Game", w, h, exit_button_pos)

    def check_mouse_events(self):
        mouse_pos = pygame.mouse.get_pos()
        self._check_play_button(mouse_pos)
        self._check_close_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.ai_game.call_play_button()

    def _check_close_button(self, mouse_pos):
        button_clicked = self.exit_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            sys.exit()

    def update(self):
        pass

    def draw_background(self):  #
        self.screen.blit(self.bg_image, self.rect_a)
        self.play_button.draw_button()
        self.exit_button.draw_button()
