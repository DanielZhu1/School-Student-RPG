import pygame

import random

from protag import Main_Character


class Enemy:
    hp = 320
    action_count = 1
    damage_received = Main_Character.hp - 20
    if action_count == 0:
        Main_Character.action_count += 1
    alive = True

    def __init__(self, hp, alive, erm_actually, damage_received):
        self.hp = hp
        self.alive = alive
        self.erm_actually = erm_actually
        self.damage_received = damage_received
        alive = True

    def attacks(self, Main_Character, erm_actually, damage_received, damage_dealt):
        self.erm_actually = erm_actually
        self.damage_received = damage_received
        self.damage_dealt = damage_dealt
        erm_actually = random.randint(20, 25)
        damage_dealt = Main_Character.hp - int(erm_actually)
        if Enemy.hp < 80:
            print("Time to lock in!")
            erm_actually * 2.5

    if hp <= 0:
        game_over = True
