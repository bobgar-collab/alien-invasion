import pygame
from pygame import Surface


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class StyleManager():

    def __init__(self, ai_game):
        self.screen_rect = ai_game.screen.get_rect()
        self.default = {
            "game_bg": {
                "path": "images/game_bg.jpg",
                "width": self.screen_rect.w,
                "height": self.screen_rect.h
            },
            "menu_bg": {
                "path": "images/menu/menu_bg.png",
                "width": self.screen_rect.w,
                "height": self.screen_rect.h
            },
            # play_button
            "menu_play_button": {
                "path": "images/menu/menu_btn_play.png",
                "width": 280,
                "height": 60
            },
            "menu_play_button_focus": {
                "path": "images/menu/menu_btn_play_focus.png",
                "width": 280,
                "height": 60
            },
            # exit_button
            "menu_exit_button": {
                "path": "images/menu/menu_btn_exit.png",
                "width": 280,
                "height": 60
            },
            "menu_exit_button_focus": {
                "path": "images/menu/menu_btn_exit_focus.png",
                "width": 280,
                "height": 60
            },
            "alien": {
                "path": "images/pixilart-drawing (1).png",
                "width": 80,
                "height": 80
            },
            "ship": {
                "path": "images/ship_2_1.png",
                "width": 80,
                "height": 80
            },
            "explosion": {
                "path": "images/explosion.png",
                "width": 80,
                "height": 80
            },
            # bullet
            "bullet": {
                "path": "images/bullet.png",
                "width": 15,
                "height": 45
            },
            "bullet_green": {
                "path": "images/bullet_green.png",
                "width": 15,
                "height": 45
            },
            # bonus
            "bonus_life": {
                "path": "images/pngwing.com.png",
                "width": 70,
                "height": 70
            },
            "bonus_fire": {
                "path": "images/bullet.png",
                "width": 70,
                "height": 70
            },
            "bonus_mushroom_style": {
                "path": "images/mushroom_style.png",
                "width": 70,
                "height": 70
            },
            "animation_jet": {
                "paths": [
                    'images/jet-anim/jet_1_1.png',
                    'images/jet-anim/jet_1_2.png',
                    'images/jet-anim/jet_1_3.png',
                    'images/jet-anim/jet_1_4.png',
                    'images/jet-anim/jet_1_5.png'
                ],
                "width": 35,
                "height": 45
            }
        }

    def get_style(self, key: str) -> Struct:
        item = self.default[key]
        return Struct(**item)

    def get_image(self, key: str, angle: float = None) -> Surface:
        style = self.get_style(key)
        return self._load_image(style.path, (style.width, style.height), angle)

    def get_animation_images(self, key: str, angle: float = None) -> list:
        animation = self.get_style(key)
        images = []
        for path in animation.paths:
            img = self._load_image(path, (animation.width, animation.height), angle)
            images.append(img)
        return images

    def _load_image(self, path: str, size: tuple, angle: float = None) -> Surface:
        image = pygame.image.load(path)
        if size:
            image = pygame.transform.scale(image, size)
        if angle:
            image = pygame.transform.rotate(image, angle)
        return image
