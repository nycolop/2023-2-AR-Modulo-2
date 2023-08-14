from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH
import pygame

class Spaceshift(Sprite):
    SPACESHIFT_WIDTH = 40
    SPACESHIFT_HEIGHT = 60
    SPACESHIFT_INITIAL_Y = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIFT_WIDTH, self.SPACESHIFT_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - self.SPACESHIFT_WIDTH
        self.rect.y = self.SPACESHIFT_INITIAL_Y

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_left(self):
        if self.rect.x <= -self.SPACESHIFT_WIDTH:
            self.rect.x = SCREEN_WIDTH + self.SPACESHIFT_WIDTH
            return
        self.rect.x -= 10

    def move_right(self):
        if self.rect.x >= SCREEN_WIDTH + self.SPACESHIFT_WIDTH:
            self.rect.x = -self.SPACESHIFT_WIDTH
            return
        self.rect.x += 10

    def move_up(self):
        if self.rect.y <= 50:
            return
        self.rect.y -= 10

    def move_down(self):
        if self.rect.y == self.SPACESHIFT_INITIAL_Y:
            return
        self.rect.y += 10