class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        self.record_file_path = 'data/records.json'

        # Параметры экрана
        self.full_screen = False
        self.screen_width = 1200  # разришение
        self.screen_height = 800  # 1900, 1010
        self.bg_color = (00, 0, 20)  # цвет
        self.bg_image_path = 'images/bg.png'

        # Параметры пули
        # self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_img_path = 'images/bullet.png'
        # Кол-во пуль
        if self.full_screen:
            self.bullets_allowed = 15
        else:
            self.bullets_allowed = 5

        # Параметры корабля
        # self.ship_speed = 1.5
        self.ship_limit = 1
        #
        self.alien_width = 80
        self.alien_height = 80
        # self.alien_speed = 2
        self.fleet_drop_speed = 10
        # self.fleet_direction = 1

        self.speedup_scale = 1.2
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        if self.full_screen:
            self.bullet_speed = 3
        else:
            self.bullet_speed = 1
        self.alien_speed = 2
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
