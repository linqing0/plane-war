import pygame
from random import *


class Enemy_Lv1(pygame.sprite.Sprite):
    def __init__(self,backfground_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'./image/enemy_lv1.png')
        self.rect = self.image.get_rect()
        self.width ,self.height = backfground_size[0],backfground_size[1]
        self.speed = 5
        self.rect.left , self.rect.top = randint(0,self.width - self.width) , randint(-3 * self.height, 0)    #进场时机

    def move_down(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.remove()


class Enemy_Lv2(pygame.sprite.Sprite):
    def __init__(self,backfground_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'./image/enemy_lv2.png')
        self.rect = self.image.get_rect()
        self.width ,self.height = backfground_size[0],backfground_size[1]
        self.speed = 2
        self.rect.left , self.rect.top = randint(0,self.width - self.width) , randint(-8 * self.height, -self.height)

    def move_down(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.remove()


class Enemy_Lv3(pygame.sprite.Sprite):
    def __init__(self,backfground_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load(r'./image/enemy_lv3.png')
        self.image2 = pygame.image.load(r'./image/enemy_lv3_02.png')
        self.rect = self.image1.get_rect()
        self.width ,self.height = backfground_size[0],backfground_size[1]
        self.speed = 1
        self.rect.left , self.rect.top = randint(0,self.width - self.width) , randint(-13 * self.height, -5 * self.height)

    def move_down(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.remove()