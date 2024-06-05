import pygame

import random

from nerd_enemy import Enemy


class Main_Character:
    max_hp = 150
    max_bp = 50
    action_count = 1
    action_wait_time = 90
    if action_count == 0:
        Enemy.action_count += 1
    hp = max_hp - Enemy.damage_received
# Sets up attributes and how the turn system will work 
    
    def __init__(self, hp, bp, max_hp, max_bp, alive, lock_in, blunt_hit, yap_session, math_attack, guard, Using_Skills,
                 action_count, Casting_Skills):
        self.hp = hp
        self.bp = bp
        self.image = pygame.image.load("protagonist.png")
        self.max_hp = max_hp
        self.max_bp = max_bp
        self.alive = alive
        self.lock_in = lock_in
        self.blunt_hit = blunt_hit
        self.yap_session = yap_session
        self.math_attack = math_attack
        self.guard = guard
        self.Using_Skills = Using_Skills
        self.action_count = action_count
        self.Casting_Skills = Casting_Skills
# Initializes everything
    
    def blunt_hit(self, hp, max_hp, Using_Skills, blunt_hit, action_count, Casting_Skills):
        self.hp = hp
        self.max_hp = max_hp
        self.Using_Skills = Using_Skills
        self.blunt_hit = blunt_hit
        self.Casting_Skills = Casting_Skills
        blunt_hit = random.randint(45, 60)
        if Casting_Skills(blunt_hit):
            hp -= 10
            Enemy.hp -= blunt_hit
            action_count -= 1
# Idea behind this skill is an attack slightly more powerful than the Brain power attack except it uses Hp, so it has higher risk but can be used without Bp.
    def yap_session(self, bp, max_bp, Using_Skills, yap_session, action_count, Casting_Skills):
        self.bp = bp
        self.max_bp = max_bp
        self.Using_Skills = Using_Skills
        self.yap_session = yap_session
        self.Casting_Skills = Casting_Skills
        yap_session = random.randint(0, 100)
        if Casting_Skills(yap_session):
            bp -= 8
            action_count -= 1
            if yap_session <= 80:
                Enemy.alive = False
# Idea behind this skill is a random attack in hopes of instantly defeating the enemy out of desperation
    
    def math_attack(self, bp, max_bp, Using_Skills, math_attack, action_count, Casting_Skills):
        self.bp = bp
        self.max_bp = max_bp
        self.Using_Skills = Using_Skills
        self.math_attack = math_attack
        self.Casting_Skills = Casting_Skills
        math_attack = random.randint(45, 55)
        if Casting_Skills(math_attack):
            bp -= 4
            Enemy.hp -= math_attack
            action_count -= 1
# Idea behind this skill is very simple, inexpensive attack that uses small amounts of Bp.
    
    def lock_in(self, bp, lock_in, math_attack, Using_Skills, action_count, Casting_Skills):
        self.bp = bp
        self.lock_in = lock_in
        self.Casting_Skills = Casting_Skills
        self.Using_Skills = Using_Skills
        lock_in = math_attack * 2.5
        if Casting_Skills(lock_in):
            bp -= 20
            math_attack * 2.5
            action_count -= 1
# Idea behind this skill is to charge up the next skill but at the cost of a large amount of Bp so you can continuously strengthen but you will also run out of Bp faster.
    
    def guard(self, hp, action_count):
        self.hp = hp
        guard = Enemy.damage_received * 0.2
        action_count -= 1
# Idea behind this is to guard against the enemy's locked in attack
    
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
        return self.Using_Skills()
# Prevents skill use with inadequate attributes 
    
    if hp > 0:
        action_count += 1

    def Casting_Skills(self, hp, bp, blunt_hit, lock_in, yap_session, math_attack, action_count, action_wait_time):
        while action_count >= action_wait_time:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                Enemy.hp -= blunt_hit
                hp -= 10
            if keys[pygame.K_2]:
                lock_in = True
                bp -= 20
            if keys[pygame.K_3]:
                yap_session = True
                bp -= 8
            if keys[pygame.K_4]:
                Enemy.hp -= math_attack
                bp -= 4
        return self.Casting_Skills()
# Adds key binds to using skills 
    
    if hp <= 0:
        game_over = True
