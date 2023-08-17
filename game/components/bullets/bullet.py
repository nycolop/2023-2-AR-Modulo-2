import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SUPER_BULLET_TYPE


class Bullet(Sprite):
    SPEED = 20

    def __init__(self, spaceshift):
        self.image = None
        if spaceshift.type == 'player' and spaceshift.power_up_type == SUPER_BULLET_TYPE:
            self.image = spaceshift.model['bullets']['special']
            self.image = pygame.transform.scale(self.image, (40, 50))
        elif spaceshift.type == 'player':
            self.image = spaceshift.model['bullets']['normal']
            self.image = pygame.transform.scale(self.image, (10, 20))
        elif spaceshift.type == 'enemy':
            self.image = spaceshift.model['bullet']['model']
            self.image = pygame.transform.scale(self.image, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.center = spaceshift.rect.center
        self.owner = spaceshift.type

    def update(self, bullets):
        if self.owner == 'player':
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)
        elif self.owner == 'enemy':
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))