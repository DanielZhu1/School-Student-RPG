import pygame

import random

class Enemy:

    hp = 320
    alive = True

    def __init__(self, hp, alive, erm_actually, damage_received):
        self.hp = hp
        self.alive = alive
        self.erm_actually = erm_actually
        self.damage_received = damage_received
        alive = True
    def attacks(self, Main_Character, erm_actually, damage_received):
        self.erm_actually = erm_actually
        self.damage_received = damage_received
        erm_actually = random.randint(20, 25)
        damage_dealt = Main_Character.hp - int(erm_actually)
        if Enemy.hp < 80:
            print("Time to lock in!")
            erm_actually * 2.5
    if hp <= 0:
        game_over = True
