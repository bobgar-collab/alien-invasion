import pygame.font


class Button():

    def __init__(self, ai_game, msg, width, height, pos):
        self.screen = ai_game.screen

        # Назначение размеров и свойств кнопок.
        self.button_color = (240, 120, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = pos

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
