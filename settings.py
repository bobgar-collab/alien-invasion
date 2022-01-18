from utils import load_dictionary


class Settings:

    def __init__(self):
        # Load config data and initialize properties.
        config_path = 'data/config.json'

        self.config_dict = load_dictionary(config_path)

        self.record_file_path = self.config_dict["record_file_path"]

        # Параметры экрана
        self.full_screen = self.config_dict["full_screen"]
        self.screen_width = self.config_dict["screen_width"]
        self.screen_height = self.config_dict["screen_height"]
        self.bg_image_path = self.config_dict["bg_image_path"]

        # TODO Move to config file
        # Параметры бонуса
        self.bonus_width = self.config_dict["bonus_width"]
        self.bonus_height = self.config_dict["bonus_height"]
        self.bonus_speed = self.config_dict["bonus_speed"]
        self.bonus_life_img_path = self.config_dict["bonus_life_img_path"]
        self.bonus_fire_img_path = self.config_dict["bonus_fire_img_path"]

        # Параметры пули
        self.bullet_width = self.config_dict["bullet_width"]
        self.bullet_height = self.config_dict["bullet_height"]
        self.bullet_img_path = self.config_dict["bullet_img_path"]
        self.alien_bullet_img_path = self.config_dict["alien_bullet_img_path"]
        # Кол-во пуль
        self.bullets_allowed = self.config_dict["bullets_allowed"]

        # Параметры корабля
        self.ship_limit = self.config_dict["ship_limit"]

        self.alien_width = self.config_dict["alien_width"]
        self.alien_height = self.config_dict["alien_height"]
        self.fleet_drop_speed = self.config_dict["fleet_drop_speed"]
        self.fleet_direction = self.config_dict["fleet_direction"]

        self.speedup_scale = self.config_dict["speedup_scale"]
        self.score_scale = self.config_dict["score_scale"]

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bg_image_speed = self.config_dict["bg_image_speed"]
        self.ship_speed = self.config_dict["ship_speed"]
        self.bullet_speed = self.config_dict["bullet_speed"]
        self.alien_speed = self.config_dict["alien_speed"]

        self.alien_points = 10

        self.ship_fire_bonus = False

    def increase_speed(self):
        self.bg_image_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
