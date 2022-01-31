import pygame


class Animation():

    def __init__(self, ai_game, fps_time: int, name):
        self.screen = ai_game.screen
        self.style = ai_game.style
        self.fps_time = fps_time

        self.images = self.style.get_images(name)

        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.last_tick = 0

    def update(self):
        # Check time offset
        now = pygame.time.get_ticks()
        delta = now - self.last_tick
        if delta < self.fps_time:
            return
        self.last_tick = now

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
