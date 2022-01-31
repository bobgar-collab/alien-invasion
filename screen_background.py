import pygame


class ScreenBackground:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Show only on Start a new game
        self.show_bg_menu = True
        self.bg_menu = pygame.image.load(self.settings.menu_bg_path)
        self.bg_menu = pygame.transform.scale(self.bg_menu, (self.screen.get_rect().w, self.screen.get_rect().h))

        self.bg_image = pygame.image.load(self.settings.game_bg_path)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen.get_rect().w, self.screen.get_rect().h))
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

    def draw_background(self):
        self.screen.blit(self.bg_image, self.rect_a)
        if self.show_bg_menu:
            self.screen.blit(self.bg_menu, self.rect_b)
        else:
            self.screen.blit(self.bg_image, self.rect_b)
