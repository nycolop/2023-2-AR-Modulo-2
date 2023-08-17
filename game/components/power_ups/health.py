from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEALTH_TYPE, HEALTH


class Health(PowerUp):
    def __init__(self):
        super().__init__(HEALTH, HEALTH_TYPE)

