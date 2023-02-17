class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (135, 206, 250)

        # Параметры экрана
        self.ship_speed = 1

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
