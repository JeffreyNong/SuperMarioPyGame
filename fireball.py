import pygame
from pygame.sprite import Sprite


class Fireball(Sprite):
    def __init__(self, screen, mario, x_spd):
        super().__init__()
        self.screen = screen
        self.mario = mario
        self.x_spd = x_spd
        sheet = pygame.image.load('images/allsprites.png')

        self.image = pygame.Surface((10, 10))
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (180, 280, 10, 10))
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.mario.rect.x
        self.rect.y = self.mario.rect.y + 25

        self.frame_counter = 0
        self.fire_timer = 0
        self.bouncing = False

    def update(self):
        if self.fire_timer <= 250:
            self.rect.x += self.x_spd
            if self.frame_counter <= 20:
                self.rect.y -= 2
            elif self.frame_counter <= 40:
                self.rect.y += 2
            elif self.frame_counter > 10:
                self.frame_counter = 0
            self.frame_counter += 1
        else:
            self.kill()
        self.fire_timer += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
