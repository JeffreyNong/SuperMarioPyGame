import pygame
from pygame.sprite import Sprite


class Goomba(Sprite):

    def __init__(self, screen, settings, pipes, blocks, ground):
        super(Goomba, self).__init__()
        self.screen = screen
        self.settings = settings
        self.pipes = pipes
        self.blocks = blocks
        self.ground = ground
        self.screen_rect = screen.get_rect()

        self.frames = []
        self.image = pygame.Surface((15, 15))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (0, 0, 15, 16))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.moving_left = False
        self.moving_right = False

        for i in range(0, 4):
            temp_img = pygame.Surface((16, 16))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (0, i*20, 16, 16))
            temp = pygame.transform.scale(temp_img, (40, 40))
            self.frames.append(temp)

        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.x_change = -0.5
        self.y_change = 0.0

        self.frame_counter = 0
        self.enemy_type = 0

    def update(self, mario):
        collision = pygame.sprite.spritecollide(self, self.blocks, False)
        if abs(self.rect.x - mario.rect.x) <= 1500 or not collision:
            self.move()
        if self.frame_counter <= 100:
            self.image = self.frames[0]
            self.frame_counter += 1
        elif self.frame_counter <= 200:
            self.image = self.frames[1]
            self.frame_counter += 1
        else:
            self.frame_counter = 0

    def move(self):
        self.calc_gravity()

        pipe_collide = pygame.sprite.spritecollide(self, self.pipes, False)
        for pipe in pipe_collide:
            if self.x_change > 0:
                self.rect.right = pipe.rect.left - 2
            if self.x_change < 0:
                self.rect.left = pipe.rect.right + 2
            self.x_change *= -1

        block_collide = pygame.sprite.spritecollide(self, self.ground, False)
        for block in block_collide:
            if self.x_change > 0:
                self.rect.right = block.rect.left - 2
            if self.x_change < 0:
                self.rect.left = block.rect.right + 2
            self.x_change *= -1

        self.x += self.x_change
        self.y += self.y_change

        self.rect.x = self.x
        self.rect.y = self.y

    def calc_gravity(self):
        if self.y_change == 0:
            self.y_change = 1
        else:
            self.y_change += .05
        if self.rect.y >= self.settings.base_level - self.rect.height and self.y_change >= 0:
            self.y_change = 0
            self.rect.y = self.settings.base_level - self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)
