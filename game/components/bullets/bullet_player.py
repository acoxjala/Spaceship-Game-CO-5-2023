import pygame

from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_PLAYER, BULLET_PLAYER_TYPE

class BulletPlayer(Bullet):
    WIDTH = 10
    HEIGHT = 20
    SPEED = 5

    def __init__(self, center):
        self.image = BULLET_PLAYER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center, BULLET_PLAYER_TYPE)

    def update(self, enemy):
        self.rect.y -= self.SPEED
        if self.rect.y <= 0:
            self.is_alive = False
        super().update(enemy)
        if not self.is_alive:
            enemy.is_destroyed = True

