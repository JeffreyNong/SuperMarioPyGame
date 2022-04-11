import pygame
from pygame.sprite import Sprite


class Brick(Sprite):
    BRICK_SIZE = 40

    def __init__(self, screen, settings, block_type):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.block_type = block_type
        self.change_brick = False

        self.sz = Brick.BRICK_SIZE
        self.brick = "images/Red_Brick.png"
        self.itembrick = "images/Item_Brick.png"
        self.floorbrick = "images/Red_Brick.png"
        self.stairbrick = "images/stairbrick.png"
        self.emptybrick = "images/Empty_Brick.png"
        self.invisibrick = "images/Invisible_Block.png"
        self.bluebrick = "images/bluebrick.png"
        self.understone = "images/understone.png"

        # Checks what type of brick needs to be drawn
        if block_type == 0:
            self.image = pygame.image.load(self.brick)
        if block_type == 1:
            self.image = pygame.image.load(self.itembrick)
        if block_type == 2:
            self.image = pygame.image.load(self.itembrick)
        if block_type == 3:
            self.image = pygame.image.load(self.floorbrick)
        if block_type == 4:
            self.image = pygame.image.load(self.stairbrick)
        if block_type == 5:
            self.image = pygame.image.load(self.brick)
        if block_type == 6:
            self.image = pygame.image.load(self.invisibrick)
        if block_type == 7:
            self.image = pygame.image.load(self.bluebrick)
        if block_type == 8:
            self.image = pygame.image.load(self.understone)
        if block_type == 9:
            self.image = pygame.image.load(self.brick)

        self.image = pygame.transform.scale(self.image, (self.sz, self.sz))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.og_pos = self.rect.y
        self.frame_counter = 0
        self.bouncing = False

    def change(self):
        self.image = pygame.image.load(self.emptybrick)
        self.image = pygame.transform.scale(self.image, (self.sz, self.sz))

    def update(self):
        if self.bouncing:
            if self.frame_counter <= 5:
                self.rect.y -= 1
            elif self.frame_counter <= 10:
                self.rect.y += 1
            else:
                self.frame_counter = 0
                self.bouncing = False
            self.frame_counter += 1
