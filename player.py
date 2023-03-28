import pygame

class Player(pygame.sprite.Sprite):    #继承sprite类做碰撞检测
    def __init__(self,background_size):    #back_ground约束player移动位置的范围
        pygame.sprite.Sprite.__init__(self)    #初始化，加self

        self.width, self.height = background_size[0], background_size[1]    #480,700
        self.player_image1 = pygame.image.load(r'./image/player_01.png')   #保留了alpha通道，使图片变成不规则形状
        self.player_image2 = pygame.image.load(r'./image/player_02.png')
        self.rect = self.player_image1.get_rect()   #获取player的现定矩形
        # self.rect.left ,self.rect.top = (self.width - self.rect.width )//2,self.height - self.rect.height - 60

        self.speed = 10

    def move_up(self):
        if self.rect.top > 0:
            self.rect.top -=self.speed
        else:
            self.rect.top = 0

    def move_down(self):
        if self.rect.bottom < self.height-60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height -60

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def move_right(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width
