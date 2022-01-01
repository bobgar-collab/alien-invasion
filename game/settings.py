class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры пули
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_img_path = './images/bullet.png'
        self.bullets_allowed = 1000

        # Параметры экрана
        self.screen_width = 1200 # разришение
        self.screen_height = 800 # 1900, 1010
        self.bg_color = (00, 0, 20)  # цвет
        # Параметры корабля
        self.ship_speed = 1.5
        self.ship_limit = 3
        #
        self.alien_width = 80
        self.alien_height = 80
        self.alien_speed = 1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1
