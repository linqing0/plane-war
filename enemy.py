import pygame
from random import *


class Enemy_Lv1(pygame.sprite.Sprite):
    def __init__(self,backfground_size):
        pygame.sprite.Sprite.__init__(self)
        self.enemy = pygame.image.load(r'./image/enemy_lv1.png')
        self.rect = self.enemy.get_rect()
        self.width ,self.height = backfground_size[0],backfground_size[1]
        self.speed = 15
        self.rect.left , self.rect.top = randint(0,self.width - self.width) , randint(-3*self.height, 0)

    def move_down(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.remove()


class Enemy_Lv2(pygame.sprite.Sprite):
    def __init__(self,backfground_size):
        pygame.sprite.Sprite.__init__(self)
        self.enemy = pygame.image.load(r'./image/enemy_lv1.png')
        self.rect = self.enemy.get_rect()
        self.width ,self.height = backfground_size[0],backfground_size[1]
        self.speed = 15
        self.rect.left , self.rect.top = randint(0,self.width - self.width) , randint(-3*self.height, 0)

    def move_down(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.remove()