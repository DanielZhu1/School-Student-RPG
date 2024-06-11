import pygame
import random
from protag import Main_Character
from nerd_enemy import Enemy


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Arial", 30)
game_over_font = pygame.font.SysFont("Impact", 65)
pygame.display.set_caption("School Student RPG")
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode((size))
background = pygame.image.load("start_screen.png")
# Sets up the screen and background

r = 50
g = 0
b = 100

victory = "You have won the game!"
failure = "You have lost the game."
mc_turn = "It is your turn!"
enemy_turn = "It is the enemy turn!"
intro = "Welcome to School Student RPG"
mc_attack_tutorial = "Press left click to attack!"
enemy_attack_tutorial = "The enemy hits you with "
game_over = False

# Sets up the win and loss conditions
enemy = Enemy(100, 10, 600, 200)
protag = Main_Character(100, 10, 20, 200)
display_intro = my_font.render(intro, True, (255, 255, 255))
display_mc_turn = my_font.render(mc_turn, True, (5, 255, 5))
display_enemy_turn = my_font.render(enemy_turn, True, (255, 25, 25))
display_enemy_hp = my_font.render("ENEMY HP: " + str(enemy.hp), True, (255, 255, 25))
display_mc_hp = my_font.render("MC HP: " + str(protag.hp), True, (255, 255, 25))
display_mc_attack = my_font.render(mc_attack_tutorial, True, (5, 255, 5))

run = True
start = False
my_turn = True
count = 1
win = False

while run:

    if protag.hp <= 0:
        game_over = True
        display_lose = game_over_font.render(failure, True, (0, 0, 255))
        win = False
    if enemy.hp <= 0:
        game_over = True
        display_win = game_over_font.render(victory, True, (139, 0, 0))
        win = True

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if start and my_turn:
                enemy.hp -= random.randint(10, 14)
                display_enemy_hp = my_font.render("ENEMY HP: " + str(enemy.hp), True, (255, 255, 25))
                my_turn = False
                enemy_turn = True
            if start and enemy_turn:
                if count == 1:
                    enemy_attack = random.randint(10, 15)
                    display_enemy_attack = my_font.render(enemy_attack_tutorial + str(enemy_attack) + " damage!", True, (255, 25, 25))
                    count += 1
                elif count == 2:
                    protag.hp -= enemy_attack
                    display_mc_hp = my_font.render("MC HP: " + str(protag.hp), True, (255, 255, 25))
                    count += 1
                elif count == 3:
                    enemy_turn = False
                    my_turn = True
                    count = 1

            start = True



    if not(start):
        screen.blit(background, (0, 0))
    elif start and not game_over:
        screen.fill((r, g, b))
        screen.blit(enemy.image, enemy.rect)
        screen.blit(protag.image, protag.rect)
        screen.blit(display_mc_hp, (60, 450))
        screen.blit(display_enemy_hp, (550, 450))
        if my_turn:
            screen.blit(display_mc_turn, (280, 600))
            screen.blit(display_mc_attack, (270, 650))
        elif enemy_turn:
            screen.blit(display_enemy_turn, (280, 600))
            screen.blit(display_enemy_attack, (220, 650))
    elif game_over:
        screen.fill((r, g, b))
        if win:
            screen.blit(display_win, (100, 400))
        elif not(win):
            screen.blit(display_lose, (100, 400))

        # screen.fill((r, g, b))

    pygame.display.update()

pygame.quit()
# Ends the program
