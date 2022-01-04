class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры пули
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_img_path = './images/bullet.png'
        self.bullets_allowed = 1000

        # Параметры экрана
        self.screen_width = 1200  # разришение
        self.screen_height = 800  # 1900, 1010
        self.bg_color = (00, 0, 20)  # цвет
        # Параметры корабля
        self.ship_speed = 1.5
        self.ship_limit = 1
        #
        self.alien_width = 80
        self.alien_height = 80
        self.alien_speed = 2
        self.fleet_drop_speed = 50
        self.fleet_direction = 1

        self.speedup_scale = 1.01
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
