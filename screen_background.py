import pygame

import alien_invasion as ai


class ScreenBackground:
    def __init__(self, ai_game: ai.AlienInvasion):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.bg_image = pygame.image.load(self.settings.bg_image_path)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen.get_rect().w, self.screen.get_rect().h))
        self.rect_a = self.screen.get_rect()
        self.rect_b = self.screen.get_rect()
        self.h = self.screen.get_rect().h
        self.y = 0.0

    def update(self):
        self.y += self.settings.bg_image_speed
        self.rect_a.y = int(self.y) - self.h
        self.rect_b.y = int(self.y)
        if self.y >= self.h:
            self.y = 0.0

    def draw_background(self):
        self.screen.blit(self.bg_image, self.rect_a)
        self.screen.blit(self.bg_image, self.rect_b)
