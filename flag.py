import pygame
from pygame.sprite import Sprite


class Flag(Sprite):
    def __init__(self, screen, settings, stats):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.screen_rect = screen.get_rect()

        self.image = pygame.Surface((30, 30))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (340, 0, 30, 16))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 7930
        self.rect.y = 170

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.stats.reached_pole and self.rect.y != 508:
            self.rect.y += 1
        if self.rect.y == 508:
            self.stats.flag_reach_bot = True
