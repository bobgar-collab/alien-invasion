import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.path = self.settings.bullet_img_path

        # TODO move to method params
        angle = 0
        speed = self.settings.get_bullet_speed()
        start_pos = ai_game.ship.rect.midtop

        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))
        # Rotate image
        self.image = pygame.transform.rotate(self.image, -angle)

        # start_pos is a center of the sprite.
        self.rect = self.image.get_rect(center=start_pos)

        # To apply an offset to the start position,
        # create another vector and rotate it as well.
        offset = Vector2(0, -30).rotate(angle)
        # Then add the offset vector to the position vector.
        self.pos = Vector2(start_pos) + offset
        # Rotate the direction vector (1, 0) by the angle.
        # Multiply by desired speed.
        self.velocity = Vector2(0, -1).rotate(angle) * speed

    def update(self):
        # Add velocity to pos to move the sprite.
        self.pos += self.velocity
        # Update rect coords.
        self.rect.center = self.pos

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
