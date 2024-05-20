import pygame

import random


class Enemy:
    pass

class Enemy:

    Enemy.hp = 320

    def __init__(self, hp, alive):
        self.hp = hp
        self.alive = alive
        alive = True
    def attacks(self, Main_Character, Erm_actually, damage_received):
        Erm_actually = random.randint(20, 25)
        damage_received = Main_Character.hp - int(Erm_actually)
        if Enemy.hp < 80:
            print("Time to lock in!")
            Erm_actually * 2.5
    if Enemy.hp <= 0:
        game_over = True
