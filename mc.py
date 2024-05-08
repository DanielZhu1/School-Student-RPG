import pygame

import random

from nerd_enemy import Enemy
class Main_character:
    hp = 120
    bp = 50

    def __init__(self, hp, bp):
        self.hp = hp
        self.bp = bp

    def skills(self, hp, bp):
        self.hp = hp
        self.bp = bp
        blunt_hit = random.randint(50, 70)
        blunt_hit.cost = hp - 10
        lock_in = 50 * 2.5
        lock_in.cost = bp - 20
        yap_session = random.randint(0, 100)
        if yap_session > 85:
            Enemy.hp = 0
        yap_session.cost = bp - 6
        math_attack = random.randint(45, 65)
        math_attack.cost = bp - 4

    def Guard(self, hp):
        self.hp = hp
        Enemy.damage_received * 0.2

    def Using_Skills(self, hp, bp, blunt_hit, lock_in, yap_session, math_attack):
        self.hp = hp
        self.bp = bp
        if hp <= str(blunt_hit.cost):
            print("You do not have enough HP!")
        if bp < str(lock_in.cost):
            print("You do not have enough BP!")
        if bp < str(yap_session.cost):
            print("You do not have enough BP!")
        if bp < str(math_attack.cost):
            print("You do not have enough BP!")
