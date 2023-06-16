import pygame

from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_PLAYER, BULLET_PLAYER_TYPE

class BulletPlayer(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20

    def __init__(self, center):
        self.image = BULLET_PLAYER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center, BULLET_PLAYER_TYPE)

    def update(self, enemy_handler):
        self.rect.y -= self.SPEED
        for enemy in enemy_handler.enemies:
            if(self.rect.colliderect(enemy.rect)):
                enemy_handler.remove_enemy(enemy)

