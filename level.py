import pygame


class Level:
    def __init__(self, screen, settings, pipes, lvl_map, bricks, upgrades, enemies, flags, poles):
        self.screen = screen
        self.settings = settings
        self.bricks = bricks
        self.lvl_map = lvl_map
        self.pipes = pipes
        self.upgrades = upgrades
        self.enemies = enemies
        self.flags = flags
        self.poles = poles
        self.image = pygame.image.load('images/level_bg.png')
        self.image = pygame.transform.scale(self.image, (10910, self.settings.screen_height))
        self.rect = self.image.get_rect()

        self.shift_world = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def shifting_world(self, shifting_x):
        self.shift_world += shifting_x

        self.rect.x += shifting_x
        for flag in self.flags:
            flag.rect.x += shifting_x
        for pole in self.poles:
            pole.rect.x += shifting_x

        for brick in self.bricks:
            brick.rect.x += shifting_x
        for pipe in self.pipes:
            pipe.rect.x += shifting_x
        for upgrade in self.upgrades:
            upgrade.rect.x += shifting_x
        for enemy in self.enemies:
            enemy.x += shifting_x
