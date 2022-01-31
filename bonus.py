from enum import Enum

import pygame
from pygame.sprite import Sprite

from utils import load_image


class BonusType(Enum):
    LIFE = "LIFE"
    FIRE = "FIRE"
    MUSHROOM_STYLE = "MUSHROOM_STYLE"


class Bonus(Sprite):

    def __init__(self, ai_game, start_pos, bonus_type: BonusType):
        super().__init__()

        self.bonus_type = bonus_type
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.path = self.settings.bullet_img_path

        path: str
        if bonus_type == BonusType.LIFE:
            path = self.settings.bonus_life_img_path
        elif bonus_type == BonusType.FIRE:
            path = self.settings.bonus_fire_img_path
        elif bonus_type == BonusType.MUSHROOM_STYLE:
            path = self.settings.bonus_mushroom_style_img_path
        else:
            raise ValueError(f"Unknown bonus type: {bonus_type}")

        self.image = load_image(path, (self.settings.bonus_width, self.settings.bonus_height))
        self.rect = self.image.get_rect()

        self.rect.midtop = start_pos

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bonus_speed
        self.rect.y = self.y
