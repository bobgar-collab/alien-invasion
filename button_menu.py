import pygame.font

from utils import load_image


class ButtonMenu():

    def __init__(self, ai_game, image_path, image_focused_path, width, height, pos):
        self.screen = ai_game.screen

        self.focused = False

        self.image = load_image(image_path, (width, height))
        self.imageFocused = load_image(image_focused_path, (width, height))

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = pos

    def draw(self):
        if self.focused:
            self.screen.blit(self.imageFocused, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
