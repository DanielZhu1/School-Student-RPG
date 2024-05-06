import pygame

from mc import MC

pygame.init()
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 700
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode((size))
r= 50
g= 0
b= 100
game_over = False
if MC.hp  == 0:
    game_over = True

print("Welcome to School Student RPG")
run = True

while run:
    screen.fill((r, g, b))
    pygame.display.update()
pygame.quit()
