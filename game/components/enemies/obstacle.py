import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_WIDTH, ZEPPELIN, GENERIC_EXPLOSION_SOUND, GENERIC_EXPLOSION


class Obstacle(Sprite):
    ZEP_WIDTH = 100
    ZEP_HEIGHT = 120
    ZEP_Y = [100, 200, 300, 400, 500]

    def __init__(self):
        self.image = ZEPPELIN
        self.image = pygame.transform.scale(self.image, (self.ZEP_WIDTH, self.ZEP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = self.ZEP_Y[random.randint(0, len(self.ZEP_Y) - 1)]
        self.rect.x = SCREEN_WIDTH - self.ZEP_WIDTH
        self.speed_x = 3
        self.has_been_destroyed = False
        self.destroyed_time = 0
        self.lives = 3
        self.difficulty = 5

    def update(self, obstacles, game):
        self.rect.x -= self.speed_x

        self.destroy_obstacle()

        for bullet in game.bullet_manager.bullets:
            if self.rect.colliderect(bullet.rect):
                self.lives -= 1
                game.bullet_manager.bullets.remove(bullet)

        if self.lives == 0:
            self.has_been_destroyed = True
            self.destroyed_time = pygame.time.get_ticks()
            if self.difficulty != 0:
                game.score += 100 * self.difficulty
                self.difficulty = 0

        if self.rect.x <= -100:
            obstacles.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def destroy_obstacle(self):
        if self.has_been_destroyed:
            if not GENERIC_EXPLOSION_SOUND.get_num_channels():
                GENERIC_EXPLOSION_SOUND.play()
            self.image = GENERIC_EXPLOSION
            self.image = pygame.transform.scale(self.image, (self.ZEP_WIDTH, self.ZEP_HEIGHT))