from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SUPER_BULLET, SUPER_BULLET_TYPE


class SuperBullet(PowerUp):
    def __init__(self):
        super().__init__(SUPER_BULLET, SUPER_BULLET_TYPE)