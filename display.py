
import pygame


class Display:
    def __init__(self, screen, stats):
        self.font = pygame.font.SysFont('None', 50)
        self.white = (255, 255, 255)

        # SCORE
        self.score = self.font.render("SCORE", True, self.white)
        self.score_rect = self.score.get_rect()
        self.score_rect.centerx = screen.get_rect().centerx - 400
        self.score_rect.centery = screen.get_rect().top + 20

        # CURRENT SCORE
        self.current_score = self.font.render(str(stats.score), True, self.white)
        self.current_score_rect = self.current_score.get_rect()
        self.current_score_rect.centerx = screen.get_rect().centerx - 400
        self.current_score_rect.centery = screen.get_rect().top + 45

        # COINS
        self.coins = self.font.render("COINS", True, self.white)
        self.coins_rect = self.coins.get_rect()
        self.coins_rect.centerx = screen.get_rect().centerx - 250
        self.coins_rect.centery = screen.get_rect().top + 20

        # CURRENT COINS
        self.current_coins = self.font.render(str(stats.coins), True, self.white)
        self.current_coins_rect = self.current_coins.get_rect()
        self.current_coins_rect.centerx = screen.get_rect().centerx - 250
        self.current_coins_rect.centery = screen.get_rect().top + 45

        # WORLD
        self.world = self.font.render("WORLD", True, self.white)
        self.world_rect = self.world.get_rect()
        self.world_rect.centerx = screen.get_rect().centerx - 100
        self.world_rect.centery = screen.get_rect().top + 20

        # CURRENT WORLD
        self.current_world = self.font.render("1-1", True, self.white)
        self.current_world_rect = self.current_world.get_rect()
        self.current_world_rect.centerx = screen.get_rect().centerx - 100
        self.current_world_rect.centery = screen.get_rect().top + 45

        # TIME
        self.time = self.font.render("TIME", True, self.white)
        self.time_rect = self.time.get_rect()
        self.time_rect.centerx = screen.get_rect().centerx + 40
        self.time_rect.centery = screen.get_rect().top + 20

        # CURRENT TIME
        self.current_time = self.font.render(str(stats.time), True, self.white)
        self.current_time_rect = self.current_time.get_rect()
        self.current_time_rect.centerx = screen.get_rect().centerx + 40
        self.current_time_rect.centery = screen.get_rect().top + 45

        # LIVES
        self.lives = self.font.render("LIVES", True, self.white)
        self.lives_rect = self.lives.get_rect()
        self.lives_rect.centerx = screen.get_rect().centerx + 180
        self.lives_rect.centery = screen.get_rect().top + 20

        # CURRENT LIVES
        self.current_lives = self.font.render(str(stats.lives), True, self.white)
        self.current_lives_rect = self.current_lives.get_rect()
        self.current_lives_rect.centerx = screen.get_rect().centerx + 180
        self.current_lives_rect.centery = screen.get_rect().top + 45

        # HIGH SCORE
        self.high = self.font.render("HIGH SCORE", True, self.white)
        self.high_rect = self.high.get_rect()
        self.high_rect.centerx = screen.get_rect().centerx + 350
        self.high_rect.centery = screen.get_rect().top + 20

        # CURRENT HIGH SCORE
        self.current_high = self.font.render("0", True, self.white)
        self.current_high_rect = self.current_high.get_rect()
        self.current_high_rect.centerx = screen.get_rect().centerx + 350
        self.current_high_rect.centery = screen.get_rect().top + 45

        # GAME OVER
        self.over = self.font.render("GAME OVER", True, self.white)
        self.over_rect = self.over.get_rect()
        self.over_rect.centerx = screen.get_rect().centerx
        self.over_rect.centery = screen.get_rect().centery

        # GIVE SCORE
        self.give = self.font.render("0", True, self.white)
        self.give_rect = self.give.get_rect()
        self.give_rect.centerx = screen.get_rect().centerx
        self.give_rect.centery = screen.get_rect().centery

        # GIVE SCORE
        self.give = self.font.render("0", True, self.white)
        self.give_rect = self.give.get_rect()
        self.give_rect.centerx = screen.get_rect().centerx
        self.give_rect.centery = screen.get_rect().centery

    def score_blit(self, screen, stats):
        # Update current score numbers
        self.current_score = self.font.render(str(stats.score), True, self.white)
        self.current_coins = self.font.render(str(stats.coins), True, self.white)
        self.current_time = self.font.render(str(stats.time), True, self.white)
        self.current_lives = self.font.render(str(stats.lives), True, self.white)
        self.current_high = self.font.render(str(stats.high_score), True, self.white)

        screen.blit(self.score, self.score_rect)
        screen.blit(self.current_score, self.current_score_rect)
        screen.blit(self.coins, self.coins_rect)
        screen.blit(self.current_coins, self.current_coins_rect)
        screen.blit(self.world, self.world_rect)
        screen.blit(self.current_world, self.current_world_rect)
        screen.blit(self.time, self.time_rect)
        screen.blit(self.current_time, self.current_time_rect)
        screen.blit(self.lives, self.lives_rect)
        screen.blit(self.current_lives, self.current_lives_rect)
        screen.blit(self.high, self.high_rect)
        screen.blit(self.current_high, self.current_high_rect)

    def over_blit(self, screen):
        screen.blit(self.over, self.over_rect)

    def give_score(self, screen, stats, x, y, score):
        self.give = self.font.render(str(score), True, self.white)
        self.give_rect.centerx = x
        self.give_rect.centery = y
        stats.score += score
        screen.blit(self.give, self.give_rect)
