class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.alien_points = None
        self.fleet_direction = None
        self.alien_speed_factor = None
        self.bullet_speed_factor = None
        self.ship_speed_factor = None

        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # Параметры корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 25

        # Параметры пришельцев
        self.fleet_drop_speed = 15

        # Темп ускорения игры
        self.speedup_scale = 1.2

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.0
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 0.75

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        if self.ship_speed_factor < 3:
            self.ship_speed_factor *= self.speedup_scale
        else:
            self.ship_speed_factor = 3

        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
