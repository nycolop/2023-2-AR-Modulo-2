import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.enemies.obstacle_manager import ObstacleManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.spaceshift import Spaceshift

from game.utils.constants import BG, FONT_STYLE, GAME_OVER, ICON, MUSIC, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 2
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceshift()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.score = 0
        self.death_count = 0
        self.menu = Menu(self.screen, 'Press any key to start...')
        self.accumulator_score = 0
        self.max_score = 0
        self.power_up_manager = PowerUpManager()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.running = True
        pygame.mixer.music.load(MUSIC['menu'])
        pygame.mixer.music.play(-1)

        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset_game()

        pygame.mixer.music.load(MUSIC['in_game'])
        pygame.mixer.music.play(-1)

        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        else:
            pygame.mixer.music.load(MUSIC['menu'])
            pygame.mixer.music.play(-1)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        if self.score >= self.max_score:
            self.max_score = self.score + 1

        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        # pygame.display.update()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_stats()
        self.power_up_manager.draw(self.screen, self)
        self.draw_power_up_time()
        self.obstacle_manager.draw(self.screen)
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        icon = None

        # self.menu.reset_screen_color(self.screen)

        self.menu.draw(self.screen)

        if self.death_count > 0:
            self.menu.update_message(f'M: {self.death_count} | PA: {self.accumulator_score + self.score} | PF: {self.score} | MP: {self.max_score}')
            icon = pygame.transform.scale(GAME_OVER, (400, 200))
            self.screen.blit(icon, (half_screen_width - 200, half_screen_height - 200))
        else:
            icon = pygame.transform.scale(ICON, (100, 120))
            self.screen.blit(icon, (half_screen_width -  50, half_screen_height - 120))

        self.menu.update(self)

    def update_score(self):
        self.score += 1

    def draw_stats(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text_score = font.render(f'Score: {self.score}', True, (255, 255, 255))
        text_lives = font.render(f'Lives: {self.player.lives}', True, (255, 255, 255))
        text_score_rect = text_score.get_rect()
        text_lives_rect = text_lives.get_rect()
        text_score_rect.center = (100, 100)
        text_lives_rect.center = (100, 150)
        self.screen.blit(text_score, text_score_rect)
        self.screen.blit(text_lives, text_lives_rect)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 30)
                text = font.render(f'Power up enable for: {time_to_show} seconds', True, (255, 255, 255))
                text_rect = text.get_rect()
                self.screen.blit(text, (540, 50))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.power_time_up = 0
                self.player.set_image()
        else:
            self.player.has_power_up = False
            self.player.power_up_type = DEFAULT_TYPE
            self.player.set_image()
            self.player.power_time_up = 0

    def reset_game(self):
        self.death_count += 1
        self.accumulator_score += self.score
        self.score = 0
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.power_up_manager.reset()
        self.player.reset()
        self.obstacle_manager.reset()