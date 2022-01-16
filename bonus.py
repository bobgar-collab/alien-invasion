import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite


class Bonus(Sprite):

    def __init__(self, ai_game, start_pos, angle, path):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        speed = self.settings.bonus_speed

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (self.settings.bonus_width, self.settings.bonus_height))
        # Rotate image
        self.image = pygame.transform.rotate(self.image, angle)

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

    def draw_bonus(self):
        self.screen.blit(self.image, self.rect)
