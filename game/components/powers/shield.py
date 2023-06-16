from game.components.powers.power import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE

class Shield(PowerUp):

    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)