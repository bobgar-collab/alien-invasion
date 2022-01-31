import pygame.font

from utils import load_image


class ButtonMenu():

    def __init__(self, ai_game, style, style_focus, pos):
        self.screen = ai_game.screen

        self.focused = False

        self.image = load_image(style.path, (style.width, style.height))
        self.imageFocused = load_image(style_focus.path, (style_focus.width, style_focus.height))

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, style.width, style.height)
        self.rect.center = pos

    def draw(self):
        if self.focused:
            self.screen.blit(self.imageFocused, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
