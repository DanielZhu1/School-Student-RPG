import pygame
from protag import Main_Character
from nerd_enemy import Enemy


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Arial", 30)
game_over_font = pygame.font.SysFont("Impact", 100)
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
mc_turn = "It is main char turn!"
enemy_turn = "It is enemy turn!"
intro = "Welcome to School Student RPG"
game_over = False
# Sets up the win and loss conditions
enemy = Enemy(100, 10, 600, 200)
protag = Main_Character(100, 10, 20, 200)
display_intro = my_font.render(intro, True, (255, 255, 255))
display_mc_turn = my_font.render(mc_turn, True, (255, 55, 255))
display_enemy_turn = my_font.render(enemy_turn, True, (255, 255, 25))
display_enemy_hp = my_font.render("ENEMY HP: " + str(enemy.hp), True, (255, 255, 25))
display_mc_hp = my_font.render("MC HP: " + str(protag.hp), True, (255, 255, 25))
run = True
start = False
my_turn = True

while run:

    if protag.hp == 0:
        game_over = True
        game_over_font.render(failure, True, (255, 255, 255))
    if enemy.hp == 0:
        game_over = True
        game_over_font.render(victory, True, (255, 255, 255))

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            start = True

    if not(start):
        screen.blit(background, (0, 0))
    else:
        screen.fill((r, g, b))
        screen.blit(enemy.image, enemy.rect)
        screen.blit(protag.image, protag.rect)
        screen.blit(display_mc_hp, (120, 450))
        screen.blit(display_enemy_hp, (500, 450))
        if my_turn:
            screen.blit(display_mc_turn, (300, 600))
        elif enemy_turn:
            screen.blit(display_enemy_turn, (300, 600))

        # screen.fill((r, g, b))

    pygame.display.update()

pygame.quit()
# Ends the program
