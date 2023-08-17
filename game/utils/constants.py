import pygame
import os

pygame.init()
pygame.mixer.init()

pygame.mixer.music.set_volume(0.5)

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "player/models/normal.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/background.png'))


DEFAULT_TYPE = "default"

SHIELD_TYPE = 'shield'
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'power_ups/shield.png'))
SHIELD_AURA = pygame.image.load(os.path.join(IMG_DIR, 'power_ups/shield_aura.png'))

SUPER_BULLET_TYPE = 'super_bullet'
SUPER_BULLET = pygame.image.load(os.path.join(IMG_DIR, 'power_ups/speed.png'))


HEALTH = pygame.image.load(os.path.join(IMG_DIR, 'power_ups/SmallHeart.png'))
HEALTH_TYPE = 'health'


ENEMY_SHOOT_1 = pygame.mixer.Sound(os.path.join(IMG_DIR, "sound/effects/shoot_enemy.wav"))
ENEMY_SHOOT_2 = pygame.mixer.Sound(os.path.join(IMG_DIR, "sound/effects/cg1.wav"))
ENEMY_SHOOT_1.set_volume(0.2)
ENEMY_SHOOT_2.set_volume(0.2)

ENEMY_EXPLOSION_1 = pygame.mixer.Sound(os.path.join(IMG_DIR, "sound/effects/explode_mini.wav"))
ENEMY_EXPLOSION_2 = pygame.mixer.Sound(os.path.join(IMG_DIR, "sound/effects/explode.wav"))
ENEMY_EXPLOSION_1.set_volume(0.8)
ENEMY_EXPLOSION_2.set_volume(0.8)
ENEMIES = [
    {
        'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/aircraft_1/model.png")),
        'shadow': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/aircraft_1/shadow.png")),
        'bullet': {
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/aircraft_1/bullet.png")),
            'sound': ENEMY_SHOOT_1
        },
        'explosion': {
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/explosion.png")),
            'sound': ENEMY_EXPLOSION_1
        },
        'size': (60, 80),
        'type': 'normal',
        'difficulty': 1
    },
    {
        'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/aircraft_2/model.png")),
        'shadow': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/aircraft_2/shadow.png")),
        'bullet': {
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/aircraft_2/bullet.png")),
            'sound': ENEMY_SHOOT_1
        },
        'explosion': {
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/explosion.png")),
            'sound': ENEMY_EXPLOSION_1
        },
        'size': (60, 80),
        'type': 'normal',
        'difficulty': 1
    },
    {
        'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/aircraft_3/model.png")),
        'shadow': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/aircraft_3/shadow.png")),
        'bullet': {
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/aircraft_3/bullet.png")),
            'sound': ENEMY_SHOOT_1
        },
        'explosion': {
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/normal/explosion.png")),
            'sound': ENEMY_EXPLOSION_1
        },
        'size': (60, 80),
        'type': 'normal',
        'difficulty': 1
    },
    {
        'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/special/aircraft_1/model.png")),
        'shadow': pygame.image.load(os.path.join(IMG_DIR, "enemies/special/aircraft_1/shadow.png")),
        'explosion': {
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/special/explosion.png")),
            'sound': ENEMY_EXPLOSION_2
        },
        'bullet': {
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/special/rocket.png")),
            'sound': ENEMY_SHOOT_2
        },
        'size': (100, 120),
        'type': 'special',
        'difficulty': 2
    },
    {
        'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/special/aircraft_2/model.png")),
        'shadow': pygame.image.load(os.path.join(IMG_DIR, "enemies/special/aircraft_2/shadow.png")),
        'explosion': {
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/special/explosion.png")),
            'sound': ENEMY_EXPLOSION_2
        },
        'bullet': { 
            'model': pygame.image.load(os.path.join(IMG_DIR, "enemies/special/rocket.png")),
            'sound': ENEMY_SHOOT_2
        },
        'size': (100, 120),
        'type': 'special',
        'difficulty': 2
    }
]

PLAYER = {
    'bullets': {
        'normal': pygame.image.load(os.path.join(IMG_DIR, "player/bullets/normal.png")),
        'special': pygame.image.load(os.path.join(IMG_DIR, "player/bullets/special.png")),
        'sound': pygame.mixer.Sound(os.path.join(IMG_DIR, "sound/effects/shoot_762.mp3"))
    },
    'models': {
        'normal': pygame.image.load(os.path.join(IMG_DIR, "player/models/normal.png")),
        'broken_1': pygame.image.load(os.path.join(IMG_DIR, "player/models/broken_1.png")),
        'broken_2': pygame.image.load(os.path.join(IMG_DIR, "player/models/broken_2.png")),
        'broken_3': pygame.image.load(os.path.join(IMG_DIR, "player/models/broken_3.png")),
        'broken_4': pygame.image.load(os.path.join(IMG_DIR, "player/models/broken_4.png")),
        'shadow': pygame.image.load(os.path.join(IMG_DIR, "player/shadow.png"))
    },
    'explosion': pygame.image.load(os.path.join(IMG_DIR, "player/explosion.png")),
    'size': (100, 120)
}

FONT_STYLE = 'freesansbold.ttf'

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

MUSIC = {
    'in_game': os.path.join(IMG_DIR, "sound/music/in_game.mp3"),
    'menu': os.path.join(IMG_DIR, "sound/music/menu.mp3")
}

ZEPPELIN = pygame.image.load(os.path.join(IMG_DIR, "Other/zeppelin.svg"))


GENERIC_EXPLOSION_SOUND = ENEMY_EXPLOSION_2
GENERIC_EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion0.png"))

POWER_UP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "sound/effects/boost.wav"))