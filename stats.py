import pygame


class Stats:

    def __init__(self):
        self.game_active = True
        self.game_over = False

        self.reached_pole = False
        self.flag_reach_bot = False

        self.activate_secret = False
        self.activate_main_lvl = True
        self.secret_level = False
        self.main_level = True
        self.return_main_level = False

        self.score = 0
        self.coins = 0
        self.time = 500
        self.lives = 3
        self.timer = 0
        self.playing_victory_sound = False

        self.high_score = 0
        self.wr = open('highscore.txt', 'r+')
        self.current = int(self.wr.read())

        self.tick = pygame.time.get_ticks()

    def update_time(self, radio, clips):
        seconds = (pygame.time.get_ticks() - self.tick)/1000
        if seconds > 1:
            self.tick = pygame.time.get_ticks()
            self.time -= 1
            if self.reached_pole and not self.playing_victory_sound:
                self.playing_victory_sound = True
                radio.stop()
                clips[12].play()
        if self.time is 0:
            self.game_over = True
        elif self.time < -2:
            self.game_over = False
            self.reset_stats()

    def reset_stats(self):
        self.score = 0
        self.coins = 0
        self.time = 500
        self.lives = 3
        self.game_over = False
        self.reached_pole = False
        self.flag_reach_bot = False

        self.activate_secret = False
        self.activate_main_lvl = True
        self.secret_level = False
        self.main_level = True
        self.return_main_level = False

    def update_txt(self):
        self.wr.seek(0)
        self.current = int(self.wr.read())
        self.high_score = self.current
        if self.current < self.score:
            self.wr.seek(0)
            self.wr.truncate()
            self.wr.write(str(self.score))
