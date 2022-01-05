class Settings:
    def __init__(self):
        self.record_file_path = 'data/records.json'

        # Параметры экрана
        self.full_screen = True
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_image_path = 'images/bg.png'

        # Параметры пули
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_img_path = 'images/bullet.png'
        # Кол-во пуль
        self.bullets_allowed = 5

        # Параметры корабля
        self.ship_limit = 3

        self.alien_width = 80
        self.alien_height = 80
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 2

        self.delta_time = 0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self._ship_speed = 250
        self._bullet_speed = 300
        self._alien_speed = 200

        self.alien_points = 2

    def increase_speed(self):
        self._ship_speed *= self.speedup_scale
        self._bullet_speed *= self.speedup_scale
        self._alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def get_ship_speed(self):
        return self._ship_speed * self.delta_time

    def get_bullet_speed(self):
        return self._bullet_speed * self.delta_time

    def get_alien_speed(self):
        return self._alien_speed * self.delta_time
