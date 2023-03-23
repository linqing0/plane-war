import pygame

class Player(pygame.sprite.Sprite):    #继承sprite类做碰撞检测
    def __init__(self,background_size):
        pygame.sprite.Sprite.__init__()

        self.player_image = pygame.image.load(r'./image/player.png')