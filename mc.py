import pygame

import random
class MC:
    def __init__(self, hp, bp, xp):
        self.hp = hp
        self.bp = bp
        self.xp = xp
        hp = 120
        bp = 50
        xp = 0

    def skills(self, hp, bp):
        self.hp = hp
        self.bp = bp
        blunt_hit = random.randint(50, 70)
        blunt_hit.cost = 10 hp
        lock_in = damage_dealt * 2.5
        lock_in.cost = 20 bp
        yap_session = random.randint(0, 100)
        if yap_session > 75:
            enemy.defeated
        yap_session.cost = 8 bp
    def Using_Skills(self, hp, bp):
        self.hp = hp
        self.bp = bp
        current_hp = self.hp - damage_taken
        current_bp = self.bp - skill_cost
        
