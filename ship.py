import pygame
from pygame.sprite import Sprite
from animation import Animation


class Ship(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.anim_offset_x = 3
        self.anim_offset_y = 35

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.show_ship_img()
        self.jet = Animation(self.screen, 100, (35, 45), [
            'images/jet-anim/jet_1_1.png',
            'images/jet-anim/jet_1_2.png',
            'images/jet-anim/jet_1_3.png',
            'images/jet-anim/jet_1_4.png',
            'images/jet-anim/jet_1_5.png',
        ])

        self.rect = self.image.get_rect()
        self.jet_rect = self.jet.get_rect()
        self.show_jet = True

        self._init_position()

        self.jet_x = float(self.jet_rect.x)
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def _init_position(self):
        self.jet_rect.midbottom = self.screen_rect.midbottom
        x, y = self.jet_rect.midtop
        self.rect.midbottom = [x + self.anim_offset_x, y + self.anim_offset_y]

    def show_ship_img(self):
        self.image = pygame.image.load('images/ship_2_1.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.show_jet = True

    def show_explosion_ship_img(self):
        self.image = pygame.image.load('images/explosion.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.show_jet = False

    def update(self):
        self.jet.update()

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.jet_x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.jet_x -= self.settings.ship_speed

        self.rect.x = self.x
        self.jet_rect.x = self.jet_x

    def draw_ship(self):
        self.screen.blit(self.image, self.rect)
        if self.show_jet:
            self.jet.draw_animation()

    def center_ship(self):
        self._init_position()

        self.jet_x = float(self.jet_rect.x)
        self.x = float(self.rect.x)
