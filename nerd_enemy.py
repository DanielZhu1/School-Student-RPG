import pygame

import random

class Enemy:

    hp = 320

    def __init__(self, hp):
        self.hp = hp

    def attacks(self, Main_character):
        Erm_actually = random.randint(20, 25)
        damage_received = Main_character.hp - int(Erm_actually)
        lock_in = Erm_actually * 2.5

    if Enemy.hp < 80:
        lock_in
    if Enemy.hp <= 0:
        game_over = True
