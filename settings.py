class Settings:

    def __init__(self):
        self.record_file_path = 'data/records.json'

        # Параметры экрана
        self.full_screen = False
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_image_path = 'images/space_bg2.jpg.'

        # Параметры пули
        self.bullet_width = 15
        self.bullet_height = 45
        self.bullet_img_path = 'images/bullet.png'
        self.alien_bullet_img_path = 'images/bullet_green.png'
        # Кол-во пуль
        self.bullets_allowed = 5

        # Параметры корабля
        self.ship_limit = 3

        self.alien_width = 80
        self.alien_height = 80
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 2.0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bg_image_speed = 0.5
        self.ship_speed = 3.0
        self.bullet_speed = 4.0
        self.alien_speed = 2.0

        self.alien_points = 10

    def increase_speed(self):
        self.bg_image_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
