import pygame

import alien_invasion as ai


class Menu:
    def __init__(self, ai_game: ai.AlienInvasion):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.bg_image = pygame.image.load(self.settings.bg_image_path)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen.get_rect().w, self.screen.get_rect().h))
        self.rect_a = self.screen.get_rect()

    def update(self):
        pass

    def draw_background(self):  #
        self.screen.blit(self.bg_image, self.rect_a)
