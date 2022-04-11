import pygame
from pygame.sprite import Group
from stats import Stats
import game_functions as gf
from mario import Mario
from settings import Settings
from level import Level
from pipe import Pipe
from display import Display
from map import Map
from flag import Flag
from pole import Pole


def run_game():
    radio = pygame.mixer
    radio.init()
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")

    clips = [radio.Sound('sound/bg_music.wav'), radio.Sound('sound/block_bump.wav'),
             radio.Sound('sound/brick_break.wav'), radio.Sound('sound/coin.wav'),
             radio.Sound('sound/death.wav'), radio.Sound('sound/extra_life.wav'),
             radio.Sound('sound/fireball.wav'), radio.Sound('sound/jump.wav'), radio.Sound('sound/kill.wav'),
             radio.Sound('sound/pipe.wav'), radio.Sound('sound/power_spawn.wav'),
             radio.Sound('sound/powerup.wav'), radio.Sound('sound/stage_clear.wav'), radio.Sound('sound/star.wav')]

    pipes = Group()
    secret_pipes = Group()
    bricks = Group()
    secret_bricks = Group()
    upgrades = Group()
    enemies = Group()
    poles = Group()
    fireballs = Group()
    flags = Group()
    ground = Group()

    stats = Stats()
    for i in range(6, 8):
        pipe = Pipe(screen, settings, i)
        secret_pipes.add(pipe)

    flag = Flag(screen, settings, stats)
    flags.add(flag)
    pole = Pole(screen, settings)
    poles.add(pole)

    mario = Mario(screen, settings, pipes, bricks, upgrades, stats, enemies, poles, radio, clips,
                  fireballs, secret_bricks, secret_pipes, ground)
    lvl_map = None
    level = Level(screen, settings, pipes, lvl_map, bricks, upgrades, enemies, flags, poles)
    display = Display(screen, stats)

    clips[0].play(-1)
    while True:
        if stats.activate_main_lvl:
            lvl_map = Map(screen, settings, bricks, pipes, mario, enemies, ground, upgrades, stats, secret_bricks)
            lvl_map.build_brick()
            for i in range(0, 6):
                pipe = Pipe(screen, settings, i)
                pipes.add(pipe)
            flag = Flag(screen, settings, stats)
            flags.add(flag)
            pole = Pole(screen, settings)
            poles.add(pole)
            stats.activate_main_lvl = False

        if stats.activate_secret:
            pipes.empty()
            bricks.empty()
            enemies.empty()
            poles.empty()
            flags.empty()
            lvl_map = Map(screen, settings, bricks, pipes, mario, enemies, ground, upgrades, stats, secret_bricks)
            lvl_map.build_brick()

            stats.activate_secret = False
            stats.main_level = False

        if stats.game_active:
            gf.check_events(mario, stats, clips, fireballs)
            if mario.rect.right >= 600 and stats.main_level:
                diff = mario.rect.right - 600
                mario.rect.right = 600
                level.shifting_world(-diff)

            gf.update_screen(screen, mario, settings, level, pipes, display, stats, bricks, upgrades, enemies,
                             flags, poles, radio, clips, fireballs, secret_bricks, secret_pipes)
            pygame.display.flip()


run_game()
