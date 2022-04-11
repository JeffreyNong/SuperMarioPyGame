import pygame
from pygame.sprite import Sprite


class Blocks(Sprite):
    def __init__(self, screen, settings, block_type):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.blocks = []
        self.image = pygame.Surface((20, 20))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (180, 120, 20, 20))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

        for i in range(6, 13):
            temp_img = pygame.Surface((19, 19))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (180, i * 20, 20, 20))
            temp = pygame.transform.scale(temp_img, (40, 40))
            self.blocks.append(temp)

        self.image = self.blocks[block_type]
        self.rect = self.image.get_rect()
        self.rect.x = 573
        self.rect.y = self.settings.base_level-165

    def blitme(self):
        self.screen.blit(self.image, self.rect)
