import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.show_ship_img()

        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def show_ship_img(self):
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (80, 80))

    def show_explosion_ship_img(self):
        self.image = pygame.image.load('images/explosion.png')
        self.image = pygame.transform.scale(self.image, (80, 80))

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.get_ship_speed()
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.get_ship_speed()

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
