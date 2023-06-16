import pygame
import random

from game.components.powers.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD

class PowerHandler:
    def __init__(self):
        self.powers = []
        self.when_appears = random.randint(5000, 10000)
        # self.when_appears = 1000
        self.duration = random.randint(3, 5)

    def generate_power_up(self):
        power = Shield()
        self.when_appears += random.randint(5000, 10000)
        # self.when_appears += 1000
        self.powers.append(power)

    def update(self, player):
        current_time = pygame.time.get_ticks()

        if len(self.powers) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power in self.powers:
            power.update(self.powers)
            if player.rect.colliderect(power.rect):
                power.start_time = pygame.time.get_ticks()
                player.power_type = power.type
                player.has_power = True
                player.power_time = power.start_time + (self.duration * 1000)
                player.set_power_image(SPACESHIP_SHIELD)

    def draw(self, screen):
        for power in self.powers:
            power.draw(screen)