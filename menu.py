import sys

import pygame

import alien_invasion as ai
from button_menu import ButtonMenu
from game_state import GameState
from utils import load_image


class Menu:
    def __init__(self, ai_game: ai.AlienInvasion):
        self.ai_game = ai_game
        self.stats = ai_game.stats
        self.sound = ai_game.sound
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.style = ai_game.style

        style = self.style.get_style("menu_bg")
        self.image = load_image(style.path, (style.width, style.height))
        self.rect = self.screen.get_rect()

        play_button_style = self.style.get_style("menu_play_button")
        play_button_focus_style = self.style.get_style("menu_play_button_focus")
        exit_button_style = self.style.get_style("menu_exit_button")
        exit_button_focus_style = self.style.get_style("menu_exit_button_focus")

        screenCenterX, screenCenterY = self.screen.get_rect().center
        play_button_pos = (screenCenterX, screenCenterY - 50)
        exit_button_pos = (screenCenterX, screenCenterY + 50)

        self.play_button = ButtonMenu(self, play_button_style, play_button_focus_style, play_button_pos)
        self.exit_button = ButtonMenu(self, exit_button_style, exit_button_focus_style, exit_button_pos)

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
        pass

    def draw(self):  #
        self.screen.blit(self.image, self.rect)
        self.play_button.draw()
        self.exit_button.draw()
