import json

import pygame
from pygame import Surface


def save_dictionary(path, data_dict: dict):
    with open(path, 'w') as f:
        json.dump(data_dict, f)


def load_dictionary(path) -> dict:
    with open(path, 'r') as f:
        return json.load(f)


def load_image(path: str, size: tuple) -> Surface:
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, size)
    return image
