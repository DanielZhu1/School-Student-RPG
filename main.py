import pygame

from protag import Main_Character

from nerd_enemy import Enemy

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Lobster", 20)
game_over_font = pygame.font.SysFont("Impact", 100)
pygame.display.set_caption("School Student RPG")
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode((size))
background = pygame.image.load("start_screen.png")
r = 50
g = 0
b = 100
victory = "You have won the game!"
failure = "You have lost the game."
game_over = False
if Main_Character.hp == 0:
    game_over = True
    game_over_font.render(failure, True, (255, 255, 255))
if Enemy.hp == 0:
    game_over = True
    game_over_font.render(victory, True, (255, 255, 255))
intro = "Welcome to School Student RPG"
display_intro = my_font.render(intro, True, (255, 255, 255))
run = True

while run:
    screen.fill((r, g, b))
    screen.blit(background, (0, 0))
    pygame.display.update()
pygame.quit()
