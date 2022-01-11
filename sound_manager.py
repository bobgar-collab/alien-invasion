import pygame


class SoundManager():

    def __init__(self):
        self.sound = {
            'shot': pygame.mixer.Sound('sound/shot.wav'),
            'explosion': pygame.mixer.Sound('sound/explosion.wav'),
            'explosion_ship': pygame.mixer.Sound('sound/explosion_ship.wav'),
            'explosion_bullets': pygame.mixer.Sound('sound/explosion_bullets.wav')
        }

    def play_music(self):
        pygame.mixer.music.load('sound/background.mp3')
        pygame.mixer.music.play(-1, 0.0)

    def stop_music(self):
        pygame.mixer.music.stop()

    def play(self, key: str):
        self.sound[key].play()
