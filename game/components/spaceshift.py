from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SHIP_SIZE, SHIP_WIDTH, SCREEN_HEIGHT
import pygame

class Spaceshift(Sprite):
    SPACESHIFT_INITIAL_Y = 500
    SHIP_LIMITS = {
        "TOP_LIMIT": 50,
        "BOTTOM_LIMIT": SCREEN_HEIGHT - 100,
        "LEFT_LIMIT": -SHIP_WIDTH,
        "RIGHT_LIMIT": SCREEN_WIDTH + SHIP_WIDTH
    }

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, SHIP_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - SHIP_WIDTH
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
        # Possible ToDo: add diagonal movement

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_left(self):
        if self.rect.x == self.SHIP_LIMITS["LEFT_LIMIT"]:
            self.rect.x = SCREEN_WIDTH + SHIP_WIDTH
            return
        self.rect.x -= 10

    def move_right(self):
        if self.rect.x == self.SHIP_LIMITS["RIGHT_LIMIT"]:
            self.rect.x = -SHIP_WIDTH
            return
        self.rect.x += 10

    def move_up(self):
        if self.rect.y == self.SHIP_LIMITS["TOP_LIMIT"]:
            return
        self.rect.y -= 10

    def move_down(self):
        if self.rect.y == self.SHIP_LIMITS["BOTTOM_LIMIT"]:
            return
        self.rect.y += 10