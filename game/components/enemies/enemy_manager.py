import pygame
from game.components.enemies.enemy import Enemy


class EnemyManager():
    def __init__(self):
        self.enemies = []
        self.time_to_destroy = 500

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

            if enemy.has_been_destroyed:
                if (pygame.time.get_ticks() - enemy.destroyed_time) > self.time_to_destroy:
                    self.enemies.remove(enemy)



    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) == 0:
            enemy = Enemy()
            self.enemies.append(enemy)

    def reset(self):
        self.enemies = []

    def enemy_destroyed(self, enemy):
        enemy.has_been_destroyed = True
        enemy.destroyed_time = pygame.time.get_ticks()