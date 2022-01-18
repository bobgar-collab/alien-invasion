import pygame
from pygame.sprite import Sprite


class Bonus(Sprite):

    def __init__(self, ai_game, start_pos, bonus_type: str):
        super().__init__()

        self.bonus_type = bonus_type
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.path = self.settings.bullet_img_path

        path: str
        if bonus_type == "LIFE":
            path = self.settings.bonus_life_img_path
        elif bonus_type == "FIRE":
            path = self.settings.bonus_fire_img_path
        else:
            raise ValueError(f"Unknown bonus type: {bonus_type}")

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (self.settings.bonus_width, self.settings.bonus_height))
        self.rect = self.image.get_rect()

        self.rect.midtop = start_pos

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bonus_speed
        self.rect.y = self.y

    def draw_bonus(self):
        self.screen.blit(self.image, self.rect)
