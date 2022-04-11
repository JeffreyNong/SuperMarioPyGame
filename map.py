from bricks import Brick
from goomba import Goomba
from koopa import Koopa
from upgrade import Upgrade


class Map:
    BRICK_SIZE = 40

    def __init__(self, screen, settings, bricks, pipes, mario, enemies, ground, upgrades, stats, secret_bricks):
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.bricks = bricks
        self.secret_bricks = secret_bricks
        self.pipes = pipes
        self.mario = mario
        self.upgrades = upgrades
        self.enemies = enemies
        self.ground = ground  # +
        self.main_level = 'images/level_loc.txt'
        self.secret_level = 'images/Underground_Level.txt'

        if not self.stats.activate_secret:
            with open(self.main_level, 'r') as f:
                self.rows = f.readlines()
                if self.stats.return_main_level:
                    self.mario.rect.x = 7210
                    self.mario.rect.y = 500
        if self.stats.activate_secret:
            with open(self.secret_level, 'r') as f:
                self.rows = f.readlines()
                self.mario.rect.x = 100
                self.mario.rect.y = 100

        self.brick = None
        self.goomba = None
        self.koopa = None
        self.coin = None
        self.deltax = self.deltay = Map.BRICK_SIZE

    def build_brick(self):
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'B':
                    Map.create_brick(self, ncol*dx, nrow*dy, 0)
                if col == '?':
                    Map.create_brick(self, ncol * dx, nrow * dy, 1)
                if col == 'X':
                    Map.create_brick(self, ncol * dx, nrow * dy, 3)
                if col == 'M':
                    Map.create_brick(self, ncol * dx, nrow * dy, 2)
                if col == 'R':
                    Map.create_brick(self, ncol * dx, nrow * dy, 4)
                if col == 'S':
                    Map.create_brick(self, ncol*dx, nrow*dy, 5)
                if col == 'I':
                    Map.create_brick(self, ncol*dx, nrow*dy, 6)
                if col == 'G':
                    Map.create_enemy(self, ncol*dx, nrow*dy, 0)
                if col == 'K':
                    Map.create_enemy(self, ncol*dx, nrow*dy, 1)
                if col == 'A':
                    Map.create_secret_brick(self, ncol * dx, nrow * dy, 7)
                if col == 'N':
                    Map.create_secret_brick(self, ncol * dx, nrow * dy, 8)
                if col == 'C':
                    Map.create_coin(self, ncol * dx, nrow * dy, 4)
                if col == 'L':
                    Map.create_brick(self, ncol*dx, nrow*dy, 9)

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)

    def create_brick(self, x, y, num):
        self.brick = Brick(self.screen, self.settings, num)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.bricks.add(self.brick)
        if num == 4:  # +
            self.ground.add(self.brick)  # +

    def create_secret_brick(self, x, y, num):
        self.brick = Brick(self.screen, self.settings, num)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.secret_bricks.add(self.brick)

    def create_coin(self, x, y, num):
        self.coin = Upgrade(self.screen, self.settings, self.pipes, self.bricks, x, y, num)
        self.upgrades.add(self.coin)

    def create_enemy(self, x, y, num):
        if num == 0:
            self.goomba = Goomba(self.screen, self.settings, self.pipes, self.bricks, self.ground)  # +
            self.goomba.x = x
            self.goomba.y = y
            self.enemies.add(self.goomba)
        if num == 1:
            self.koopa = Koopa(self.screen, self.settings, self.pipes, self.bricks, self.enemies, self.mario)
            self.koopa.x = x
            self.koopa.y = y - 1
            self.enemies.add(self.koopa)
