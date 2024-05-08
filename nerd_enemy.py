import pygame

import random

class Enemy:
    hp = 320

    def __init__(self, hp):
        self.hp = hp


    def attacks(self, Main_character):
        Erm_actually = random.randint(20, 25)
        damage_received = Main_character.hp - int(Erm_actually)
