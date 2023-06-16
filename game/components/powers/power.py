import pygame
import random

from game.utils.constants import SCREEN_HEIGHT


class PowerUp:

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_HEIGHT - 120)
        self.rect.y = 0
        self.type = type
        self.start_time = 0

    def update(self, power_ups):
        self.rect.y += 10
        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)


    def draw(self, screen):
        screen.blit(self.image, self.rect)