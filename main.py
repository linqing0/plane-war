import pygame
import sys
import traceback
from pygame.locals import *    #常量
#####初始化#####
pygame.init()
pygame.mixer.init()

background_size = width,height = 480,700
screen = pygame.display.set_mode(background_size)    #如果直接写size记得set_mode(())
pygame.display.set_caption('plane war')

'''----- image -----'''
background_image = pygame.image.load(r'./image/sky.jpeg').convert()    #convert转换image的透明度

'''----- sound -----'''
pygame.mixer.music.load(r'./sound/春花.mp3')


#####主程序#####
def main():
    pygame.mixer.music.play(-1)    #循环播放
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background_image,(0,0))
        pygame.display.flip()    #flip() 更新整个待显示的Surface对象到屏幕上；update() 更新部分内容显示到屏幕上，如果没有参数，则与flip功能相同
        clock.tick(60)    #设置成60帧

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

