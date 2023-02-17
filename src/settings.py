class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # Параметры корабля
        self.ship_speed = 1.0
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 1.0
        self.bullet_width = 800
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100

        # Параметры пришельцев
        self.alien_speed = 0.5
        self.fleet_drop_speed = 50
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево.
        self.fleet_direction = 1
