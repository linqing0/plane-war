import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,backfground_size):
        pygame.sprite.Sprite.__init__()
        self.enemy1 = pygame.image.load(r'./image/enemy_lv1.png')
        self.rect1 = self.enemy1.get_rect()


        self.enemy2 = pygame.image.load(r'./image/enemy_lv2.png')
        self.enemy3 = pygame.image.load(r'./image/enemy_lv3.png')
        self.enemy4 = pygame.image.load(r'./image/enemy_lv4.png')


        # self.rect2 = self.enemy2.get_rect()
        # self.rect3 = self.enemy3.get_rect()
        # self.rect4 = self.enemy4.get_rect()