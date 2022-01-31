from enum import Enum

from pygame.sprite import Sprite


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
        self.style = ai_game.style

        if bonus_type == BonusType.LIFE:
            self.image = self.style.get_image("bonus_life")
        elif bonus_type == BonusType.FIRE:
            self.image = self.style.get_image("bonus_fire")
        elif bonus_type == BonusType.MUSHROOM_STYLE:
            self.image = self.style.get_image("bonus_mushroom_style")
        else:
            raise ValueError(f"Unknown bonus type: {bonus_type}")

        self.rect = self.image.get_rect()
        self.rect.midtop = start_pos
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bonus_speed
        self.rect.y = self.y
