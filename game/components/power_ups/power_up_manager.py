import random

import pygame
from game.components.power_ups.health import Health
from game.components.power_ups.shield import Shield
from game.components.power_ups.super_bullet import SuperBullet
from game.utils.constants import DEFAULT_TYPE, HEALTH_TYPE, POWER_UP_SOUND, SHIELD_AURA, SHIELD_TYPE


class PowerUpManager:
    POWER_UPS_LIST = [Shield(), SuperBullet(), Health()]
    
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3000, 5000)
        self.when_appears = random.randint(5000, 10000)

    def update(self, game):
        current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up.rect):
                # if not POWER_UP_SOUND.get_num_channels():
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + self.duration
                POWER_UP_SOUND.play()
                self.power_ups.remove(power_up)

    def draw(self, screen, game):
        for power_up in self.power_ups:
            power_up.draw(screen)

        self.use_power_up(game)

    def generate_power_up(self):
        power_up = self.POWER_UPS_LIST[random.randint(0, len(self.POWER_UPS_LIST) - 1)]
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def reset(self):
        self.power_ups = []

    def use_power_up(self, game):
        if game.player.has_power_up:
            if game.player.power_up_type == SHIELD_TYPE:
                aura = pygame.transform.scale(SHIELD_AURA, (150, 150))
                game.screen.blit(aura, (game.player.rect.x - 25, game.player.rect.y - 15))
            elif game.player.power_up_type == HEALTH_TYPE:
                game.player.lives += 1
                game.player.power_up_type = DEFAULT_TYPE
                game.player.has_power_up = False
                game.player.power_time_up = 0