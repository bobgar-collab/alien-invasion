class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры пули
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_img_path = './images/bullet.png'
        self.bullets_allowed = 5

        # Параметры экрана
        self.screen_width = 1200  # разришение
        self.screen_height = 800  # 1900, 1010
        self.bg_color = (230, 230, 230)  # цвет
        # Параметры корабля
        self.ship_speed = 0.5
        #
        self.alien_width = 80
        self.alien_height = 80
        self.fleet_drop_sped = 10
        self.fleet_direction = 1