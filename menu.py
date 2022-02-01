import sys

import pygame

import alien_invasion as ai
from button_menu import ButtonMenu
from game_state import GameState


class Menu:
    def __init__(self, ai_game: ai.AlienInvasion):
        self.ai_game = ai_game
        self.stats = ai_game.stats
        self.sound = ai_game.sound
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.style = ai_game.style

        self.image = self.style.get_image("menu_bg")
        self.rect = self.screen.get_rect()

        screenCenterX, screenCenterY = self.screen.get_rect().center
        play_button_pos = (screenCenterX, screenCenterY - 50)
        exit_button_pos = (screenCenterX, screenCenterY + 50)
        self.play_button = ButtonMenu(self, "menu_play_button", play_button_pos)
        self.exit_button = ButtonMenu(self, "menu_exit_button", exit_button_pos)

    def check_mouse_motion_event(self, event):
        if self.stats.game_state == GameState.PLAY:
            return

        mouse_pos = event.pos
        self._check_button_focus(self.play_button, mouse_pos)
        self._check_button_focus(self.exit_button, mouse_pos)

    def _check_button_focus(self, button, mouse_pos):
        focused = button.rect.collidepoint(mouse_pos)
        if button.focused != focused:
            button.focused = focused
            if button.focused:
                self.sound.play('shot')

    def check_mouse_events(self):
        if self.stats.game_state == GameState.PLAY:
            return

        mouse_pos = pygame.mouse.get_pos()
        self._check_play_button(mouse_pos)
        self._check_close_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            self.ai_game.call_play_button()

    def _check_close_button(self, mouse_pos):
        button_clicked = self.exit_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            sys.exit()

    def update(self):
        self.play_button.update()
        self.exit_button.update()

    def draw(self):  #
        self.screen.blit(self.image, self.rect)
        self.play_button.draw()
        self.exit_button.draw()
