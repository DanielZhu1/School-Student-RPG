import pygame

import random

from nerd_enemy import Enemy


class Main_character:
    max_hp = 120
    max_bp = 50
    action_cooldown = 0
    action_wait_time = 90
    hp = max_hp - Enemy.damage_received

    def __init__(self, hp, bp, max_hp, max_bp, alive):
        self.hp = hp
        self.bp = bp
        self.max_hp = max_hp
        self.max_bp = max_bp
        self.alive = alive

    def skills(self, hp, bp, ):
        self.hp = hp
        self.bp = bp
        blunt_hit = random.randint(50, 70)
        blunt_hit.cost = hp - 10
        yap_session = random.randint(0, 100)
        if yap_session > 85:
            Enemy.hp = 0
        yap_session.cost = bp - 6
        math_attack = random.randint(45, 65)
        math_attack.cost = bp - 4
        lock_in = math_attack * 2.5
        lock_in.cost = bp - 20

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
    if hp > 0:
        action_cooldown += 1

    def Casting_Skills(self, hp, bp, blunt_hit, lock_in, yap_session, math_attack, action_cooldown, action_wait_time):
        while action_cooldown >= action_wait_time:
            if keys.[pygame.K_1]:
                Enemy.hp - blunt_hit
                hp - 10
            if keys.[pygame.K_2]:
                self.lock_in
                bp - 20
            if keys.[pygame.K_3]:
                yap_session
                bp - 8
            if keys[pygame.K_4]:
                Enemy.hp - math_attack
                bp - 4
                    
                
            
    if hp <= 0:
        game_over = True
        
