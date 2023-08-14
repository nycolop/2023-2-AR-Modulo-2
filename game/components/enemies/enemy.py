import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SHIP_SIZE, SHIP_WIDTH, ENEMIES

class Enemy(Sprite):
    Y_POS = 10
    X_POS = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    SPEED_Y = [1, 2, 3, 4, 5]
    SPEED_X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    MOV_X = { 0: 'left', 1: 'right' }
    # RANDOM_ENEMY = ENEMIES[random.randint(0, len(ENEMIES) - 1)]
    # Duda, si lo ponemos como constante, el enemigo random, no funciona

    def __init__(self):
        self.image = ENEMIES[random.randint(0, len(ENEMIES) - 1)]
        self.image = pygame.transform.scale(self.image, SHIP_SIZE)
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS[random.randint(0, len(self.X_POS) - 1)]
        self.speed_x = self.SPEED_X[random.randint(0, len(self.SPEED_X) - 1)]
        self.speed_y = self.SPEED_Y[random.randint(0, len(self.SPEED_Y) - 1)]
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0

    def update(self, ships):
        self.rect.y += self.speed_y

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1

        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - SHIP_WIDTH):
            self.movement_x = 'left'
            self.move_x_for = random.randint(30, 100)
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.move_x_for = random.randint(30, 100)
            self.index = 0