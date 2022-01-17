import pygame


class Animation(pygame.sprite.Sprite):

    def __init__(self, screen, fps_time: int, scale_factor: tuple):
        super(Animation, self).__init__()

        self.screen = screen
        self.fps_time = fps_time

        sources = [
            'images/explosion.png',
            'images/explosion_1.png'
        ]

        self.images = []
        for path in sources:
            img = pygame.image.load(path)
            img = pygame.transform.scale(img, scale_factor)
            self.images.append(img)

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

    def draw_animation(self):
        self.screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
