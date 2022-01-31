from utils import load_image


class ScreenBackground():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.style = ai_game.style

        # Show only on Start a new game
        self.show_bg_menu = True
        menu_bg_style = self.style.get_style("menu_bg")
        self.bg_menu = load_image(menu_bg_style.path, (menu_bg_style.width, menu_bg_style.height))

        game_bg_style = self.style.get_style("game_bg")
        self.bg_image = load_image(game_bg_style.path, (game_bg_style.width, game_bg_style.height))

        self.rect_a = self.screen.get_rect()
        self.rect_b = self.screen.get_rect()
        self.h = self.screen.get_rect().h
        self.y = 0.0

    def reset_state(self):
        self.show_bg_menu = True

    def update(self):
        self.y += self.settings.bg_image_speed
        self.rect_a.y = int(self.y) - self.h
        self.rect_b.y = int(self.y)
        if self.y >= self.h:
            self.y = 0.0
            self.show_bg_menu = False

    def draw(self):
        self.screen.blit(self.bg_image, self.rect_a)
        if self.show_bg_menu:
            self.screen.blit(self.bg_menu, self.rect_b)
        else:
            self.screen.blit(self.bg_image, self.rect_b)
