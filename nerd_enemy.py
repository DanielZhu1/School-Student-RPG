import pygame

import random

from mc import MC


class Enemy:
    def __init__(self, hp):
        self.hp = hp
        hp = 320

    def attacks(self):
        Erm_actually = random.randint(20, 25)
        damage_received = MC.hp - int(Erm_actually)

