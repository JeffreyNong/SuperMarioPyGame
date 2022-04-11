import pygame


class Images:
    def __init__(self, screen, height, width):
        self.screen = screen
        self.height = height
        self.width = width

        self.image = pygame.Surface((self.height, self.width))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (60, 0, self.height, self.width))
        self.image = pygame.transform.scale(self.image, (self.height, self.width))

        self.rect = self.image.get_rect()

    def __str__(self):
        return 'imagerect(' + str(self.image) + str(self.rect) + ')'

    def blit(self): self.screen.blit(self.image, self.rect)
