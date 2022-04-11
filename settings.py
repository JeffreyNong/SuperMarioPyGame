class Settings:

    def __init__(self):
        # screen settings
        self.screen_width = 1000
        self.screen_height = 680
        self.bg_color = (0, 0, 0)

        # mario settings
        self.mario_limit = 3
        self.base_level = self.screen_height - 80