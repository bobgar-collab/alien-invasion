import pygame.font


class ButtonMenu():

    def __init__(self, ai_game, style, pos):
        self.screen = ai_game.screen
        self.style = ai_game.style

        self.focused = False

        self.images = self.style.get_images(style)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.images[0].get_rect().width, self.images[0].get_rect().height)
        self.rect.center = pos

    def update(self):
        pass

    def draw(self):
        if self.focused:
            self.screen.blit(self.images[1], self.rect)
        else:
            self.screen.blit(self.images[0], self.rect)
