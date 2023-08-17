from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE, SHIELD_AURA, SHIELD_TYPE, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER, SUPER_BULLET_TYPE
import pygame

class Spaceshift(Sprite):
    SPACESHIFT_INITIAL_Y = 500
    SHIP_WIDTH = PLAYER['size'][0]
    SHIP_HEIGHT = PLAYER['size'][1]
    SHIP_LIMITS = {
        "TOP_LIMIT": 50,
        "BOTTOM_LIMIT": SCREEN_HEIGHT - 100,
        "LEFT_LIMIT": -SHIP_WIDTH,
        "RIGHT_LIMIT": SCREEN_WIDTH + SHIP_WIDTH
    }

    def __init__(self):
        self.model = PLAYER
        self.image = pygame.transform.scale(PLAYER['models']['normal'], PLAYER['size'])
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - self.SHIP_WIDTH
        self.rect.y = self.SPACESHIFT_INITIAL_Y
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.bullets_capacity = 1
        self.has_power_up = False
        self.power_time_up = 0
        self.shadow = pygame.transform.scale(PLAYER['models']['shadow'], PLAYER['size'])
        self.lives = 3

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT] and user_input[pygame.K_UP]:
            self.move_left()
            self.move_up()
        elif user_input[pygame.K_LEFT] and user_input[pygame.K_DOWN]:
            self.move_left()
            self.move_down()
        elif user_input[pygame.K_RIGHT] and user_input[pygame.K_UP]:
            self.move_right()
            self.move_up()
        elif user_input[pygame.K_RIGHT] and user_input[pygame.K_DOWN]:
            self.move_right()
            self.move_down()
        elif user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)

        for enemy in game.enemy_manager.enemies:
            if (game.player.rect.colliderect(enemy.rect)) or (enemy.rect.colliderect(game.player.rect)):
                if game.player.power_up_type != SHIELD_TYPE and not enemy.has_been_destroyed:
                    game.enemy_manager.enemy_destroyed(enemy)
                    self.lives -= 1
                    break
                game.enemy_manager.enemy_destroyed(enemy)

        for obstacle in game.obstacle_manager.obstacles:
            if (game.player.rect.colliderect(obstacle.rect)) or (obstacle.rect.colliderect(game.player.rect)):
                if game.player.power_up_type != SHIELD_TYPE and not obstacle.has_been_destroyed:
                    game.obstacle_manager.obstacle_destroyed(obstacle)
                    self.lives -= 1
                    break
                game.obstacle_manager.obstacle_destroyed(obstacle)

        if self.power_up_type == SUPER_BULLET_TYPE:
            self.bullets_capacity = 3
        else:
            self.bullets_capacity = 1

        if self.lives == 0:
            game.playing = False

    def draw(self, screen):
        screen.blit(self.shadow, (self.rect.x - 10, self.rect.y))
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_left(self):
        if self.rect.x == self.SHIP_LIMITS["LEFT_LIMIT"]:
            self.rect.x = SCREEN_WIDTH + self.SHIP_WIDTH
            return
        self.rect.x -= 10

    def move_right(self):
        if self.rect.x == self.SHIP_LIMITS["RIGHT_LIMIT"]:
            self.rect.x = -self.SHIP_WIDTH
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

    def shoot(self, bullet_manager):
        if len(bullet_manager.bullets) < self.bullets_capacity:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.model['bullets']['sound'].play()

    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGHT), image = PLAYER['models']['normal']):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def reset(self):
        self.rect.x = (SCREEN_WIDTH // 2) - self.SHIP_WIDTH
        self.rect.y = self.SPACESHIFT_INITIAL_Y
        self.has_power_up = False
        self.power_up_type = DEFAULT_TYPE
        self.lives = 3