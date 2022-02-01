from pygame.sprite import Sprite

from style_manager import ImageProxy


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.style = ai_game.style

        self.image_proxy: ImageProxy = self.style.get_image_proxy("alien")
        self.image = self.image_proxy.image
        self.rect = self.image_proxy.rect

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        # TODO
        direction = self.settings.fleet_direction
        # direction > 0 - Mowing right
        # direction < 0 - Mowing left
        #  Left                   Right
        if self.rect.left <= 0 or self.rect.right >= screen_rect.right:
            return True

    def update(self):
        self.image_proxy.update()
        self.image = self.image_proxy.image
        self.rect = self.image_proxy.rect

        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
