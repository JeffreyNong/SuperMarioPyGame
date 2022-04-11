import pygame
from pygame.sprite import Sprite


class Koopa(Sprite):

    def __init__(self, screen, settings, pipes, blocks, enemies, mario):
        super(Koopa, self).__init__()
        self.screen = screen
        self.settings = settings
        self.pipes = pipes
        self.blocks = blocks
        self.screen_rect = screen.get_rect()
        self.enemies = enemies
        self.mario = mario

        self.frames = []
        self.image = pygame.Surface((15, 15))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (19, 0, 16, 23))
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

        self.moving_left = True
        self.kicked = False

        for i in range(0, 5):
            temp_img = pygame.Surface((16, 23))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (19, i*30, 16, 23))
            temp = pygame.transform.scale(temp_img, (40, 60))
            self.frames.append(temp)

        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.x_change = -0.5
        self.y_change = 0.0
        self.x = self.rect.x
        self.y = self.rect.y

        self.frame_counter = 0
        self.stunned = False
        self.set_direction = False

        self.enemy_type = 1

    def update(self, mario):
        if self.stunned:
            self.image = self.frames[4]
            if self.kicked:

                if self.rect.x >= self.mario.rect.x:
                    if not self.set_direction:
                        self.x_change = 1
                        self.set_direction = True
                    self.move()
                if self.kicked and self.rect.x <= self.mario.rect.x:
                    if not self.set_direction:
                        self.x_change = -1
                        self.set_direction = True
                    self.move()
                collide_enemies = pygame.sprite.spritecollide(self, self.enemies, False)
                for enemy in collide_enemies:
                    if enemy.enemy_type == 0:
                        self.enemies.remove(enemy)

        else:
            self.move()
            if self.frame_counter <= 100:
                if self.moving_left:
                    self.image = self.frames[0]
                else:
                    self.image = self.frames[3]
                self.frame_counter += 1
            elif self.frame_counter <= 200:
                if self.moving_left:
                    self.image = self.frames[1]
                else:
                    self.image = self.frames[2]
                self.frame_counter += 1
            else:
                self.frame_counter = 0

    def move(self):
        collision = pygame.sprite.spritecollide(self, self.blocks, False)
        if abs(self.rect.x - self.mario.rect.x) <= 2000 or not collision:
            self.calc_gravity()

            pipe_collide = pygame.sprite.spritecollide(self, self.pipes, False)
            for pipe in pipe_collide:
                if self.x_change > 0:
                    self.rect.right = pipe.rect.left - 2
                if self.x_change < 0:
                    self.rect.left = pipe.rect.right + 2
                self.x_change *= -1
                self.swap_bool()

            block_collide = pygame.sprite.spritecollide(self, self.blocks, False)
            for block in block_collide:
                if self.x_change > 0:
                    self.rect.right = block.rect.left
                if self.x_change < 0:
                    self.rect.left = block.rect.right
                self.x_change *= -1
                self.swap_bool()

            block_collide = pygame.sprite.spritecollide(self, self.blocks, False)
            for block in block_collide:
                if self.y_change > 0:
                    self.rect.bottom = block.rect.top
                self.y_change = 0

            if self.stunned:
                self.x += self.x_change * 8
                self.y += self.y_change * 8
            else:
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

    def swap_bool(self):
        if self.moving_left:
            self.moving_left = False
        else:
            self.moving_left = True
