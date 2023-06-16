from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer
from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemies):
        for bullet in self.bullets:
            if not bullet.is_alive:
                self.remove_bullet(bullet)
            else:
                if bullet.type == BULLET_ENEMY_TYPE:
                    bullet.update(player)

                if bullet.type == BULLET_PLAYER_TYPE:
                    for enemy in enemies:
                        bullet.update(enemy)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_PLAYER_TYPE:
            self.bullets.append(BulletPlayer(center))
    
    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def reset(self):
        self.bullets = []