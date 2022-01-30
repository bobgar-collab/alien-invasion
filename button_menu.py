import pygame.font


class ButtonMenu():

    def __init__(self, ai_game, image_path, image_focused_path, width, height, pos):
        self.screen = ai_game.screen

        self.focused = False

        # Default image
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        # Focused image
        self.imageFocused = pygame.image.load(image_focused_path)
        self.imageFocused = pygame.transform.scale(self.imageFocused, (width, height))

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = pos

    def draw_button(self):
        if self.focused:
            self.screen.blit(self.imageFocused, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
