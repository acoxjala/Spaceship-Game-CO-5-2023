import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, DEFAULT_TYPE

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.power_type = DEFAULT_TYPE
        self.has_power = False
        self.power_time = 0

    def update(self, user_input, bullet_handler):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        self.rect.x -= 10
        if self.rect.left < 0 - self.SPACESHIP_WIDTH:
            self.rect.x = SCREEN_WIDTH
            
    def move_right(self):
        self.rect.x += 10
        if self.rect.right > SCREEN_WIDTH + self.SPACESHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += 10

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
    
    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)

    def set_power_image(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))

    def set_default_image(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
