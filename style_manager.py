import json
from enum import Enum

import pygame
from pygame import Surface


class StyleType(Enum):
    default = "default"
    bonus = "bonus"


class ImageProxy:

    def __init__(self, manager, key: str):
        self.settings = manager.game.settings
        self.manager = manager

        self.key = key
        self.state = None
        self.image = None
        self.rect = None

        self.update()

    def update(self):
        if self.state != self.settings.mushroom_style_bonus:
            self.state = self.settings.mushroom_style_bonus

            if self.state:
                st = StyleType.bonus
            else:
                st = StyleType.default

            rect = self.rect
            self.image = self.manager.get_image(self.key, style=st)
            self.rect = self.image.get_rect()
            if rect:
                self.rect.center = rect.center


class StyleManager():

    def __init__(self, game):
        self.game = game

        screen_rect = game.screen.get_rect()

        # Parse config
        data_str = open('data/styles.json', 'r').read()
        data_str = data_str.replace("\"#screen_width\"", str(screen_rect.width))
        data_str = data_str.replace("\"#screen_height\"", str(screen_rect.height))
        data_json = json.loads(data_str)

        # Load Images
        self.styles = dict()
        for style_name, style_value in data_json.items():
            style = dict()
            self.styles[style_name] = style
            for key, item in style_value.items():
                w = item.get("width")
                h = item.get("height")
                path = item.get("path")
                paths = item.get("paths")
                if path:
                    style[key] = self._load_image(path, (w, h))
                else:
                    images = []
                    for path_item in paths:
                        image = self._load_image(path_item, (w, h))
                        images.append(image)
                    style[key] = images

    def get_image_proxy(self, key: str) -> ImageProxy:
        return ImageProxy(self, key)

    def get_image(self, key: str, angle: float = None, style: StyleType = StyleType.default) -> Surface:
        image = self.styles[style.value][key]
        if angle:
            image = pygame.transform.rotate(image, angle)
        return image

    def get_images(self, key: str, style: StyleType = StyleType.default) -> list:
        images = self.styles[style.value][key]
        return images

    def _load_image(self, path: str, size: tuple, angle: float = None) -> Surface:
        image = pygame.image.load(path)
        if size:
            image = pygame.transform.scale(image, size)
        if angle:
            image = pygame.transform.rotate(image, angle)
        return image
