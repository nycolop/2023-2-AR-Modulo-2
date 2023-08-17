import pygame

from game.components.enemies.obstacle import Obstacle

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.time_to_destroy = 500

    def update(self, game):
        self.add_obstacle()

        for obstacle in self.obstacles:
            obstacle.update(self.obstacles, game)

            if obstacle.has_been_destroyed:
                if (pygame.time.get_ticks() - obstacle.destroyed_time) > self.time_to_destroy:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def add_obstacle(self):
        if len(self.obstacles) == 0:
            obstacle = Obstacle()
            self.obstacles.append(obstacle)

    def reset(self):
        self.obstacles = []

    def obstacle_destroyed(self, obstacle):
        obstacle.has_been_destroyed = True
        obstacle.destroyed_time = pygame.time.get_ticks()