import pygame.font


class ButtonMenu():

    def __init__(self, ai_game, style, style_focus, pos):
        self.screen = ai_game.screen
        self.style = ai_game.style

        self.focused = False

        self.image = self.style.get_image(style)
        self.imageFocused = self.style.get_image(style_focus)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.image.get_rect().width, self.image.get_rect().height)
        self.rect.center = pos

    def draw(self):
        if self.focused:
            self.screen.blit(self.imageFocused, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
