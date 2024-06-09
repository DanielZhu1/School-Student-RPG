import pygame

class Main_Character:
    def __init__(self, hp, attack, x, y):
        self.hp = hp
        self.x = x
        self.y = y
        self.image = pygame.image.load("protagonist.png")
        self.attack = attack
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 2, self.image_size[1] * 2)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
