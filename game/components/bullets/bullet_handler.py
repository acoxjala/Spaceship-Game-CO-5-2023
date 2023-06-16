from game.components.bullets.bullet_enemy import BulletEnemy
from game.utils.constants import BULLET_ENEMY_TYPE

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player):
        for bullet in self.bullets:
            bullet.update(player)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))

    def reset(self):
        self.bullets = []