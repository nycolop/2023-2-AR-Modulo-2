import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, ENEMIES

class Enemy(Sprite):
    Y_POS = 10
    X_POS = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    SPEED_Y = [1, 2, 3, 4, 5]
    SPEED_X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    MOV_X = { 0: 'left', 1: 'right' }

    def __init__(self):
        self.model = ENEMIES[random.randint(0, len(ENEMIES) - 1)]
        self.image = self.model['model']
        self.image = pygame.transform.scale(self.image, self.model['size'])
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS[random.randint(0, len(self.X_POS) - 1)]
        self.speed_x = self.SPEED_X[random.randint(0, len(self.SPEED_X) - 1)]
        self.speed_y = self.SPEED_Y[random.randint(0, len(self.SPEED_Y) - 1)]
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.shooting_time = random.randint(100, 150)
        self.type = 'enemy'
        self.shadow = self.model['shadow']
        self.shadow = pygame.transform.scale(self.shadow, self.model['size'])
        self.shadow = pygame.transform.flip(self.shadow, False, True)
        self.has_been_destroyed = False
        self.destroyed_time = 0

    def update(self, ships, game):
        self.rect.y += self.speed_y

        if self.has_been_destroyed:
            if not self.model['explosion']['sound'].get_num_channels():
                self.model['explosion']['sound'].play()
            self.image = self.model['explosion']['model']
            self.image = pygame.transform.scale(self.image, self.model['size'])
        else:
            self.shoot(game.bullet_manager)

            if self.movement_x == 'left':
                self.rect.x -= self.speed_x
            else:
                self.rect.x += self.speed_x

        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        if not self.has_been_destroyed:
            screen.blit(self.shadow, (self.rect.x - 10, self.rect.y))
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1

        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.model['size'][0]):
            self.movement_x = 'left'
            self.move_x_for = random.randint(30, 100)
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.move_x_for = random.randint(30, 100)
            self.index = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)
            self.model['bullet']['sound'].play()