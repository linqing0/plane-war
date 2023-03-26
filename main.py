import pygame
import sys
import traceback
import player
from pygame.locals import *    #常量
#####初始化#####
pygame.init()
pygame.mixer.init()

background_size = width,height = 480,700
screen = pygame.display.set_mode(background_size)    #如果直接写size记得set_mode(())
pygame.display.set_caption('plane war')

'''----- image -----'''
background_image = pygame.image.load(r'./image/sky.jpeg').convert()    #convert转换image的透明度,将图片进行surface对象，pygame现在会自动处理

'''----- sound -----'''
pygame.mixer.music.load(r'./sound/春花.mp3')
bullet_sound = pygame.mixer.Sound(r'./sound/bullet.wav')
bullet_sound.set_volume(0.2)
missile = pygame.mixer.Sound('./sound/missile.wav')
missile.set_volume(0.2)

#####主程序#####
def main():
    pygame.mixer.music.play(-1)    #循环播放
    clock = pygame.time.Clock()
    '''----- 生存player -----'''
    me = player.Player(background_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background_image, (0, 0))
        pygame.display.flip()  # flip() 更新整个待显示的Surface对象到屏幕上；update() 更新部分内容显示到屏幕上，如果没有参数，则与flip功能相同
        clock.tick(60)  # 设置成60帧

        '''----- 监听键盘 -----'''    #响应键盘操作：（1）通过检测事件消息如key_down消息，那么就是按下了按键。适用偶然按下！！！ （2）调用key模块里的get_press方法，使用会返回包含该按键bool值的序列 如果是True就说明按键按下。适用一直按着按键！！！
        key_pressed = pygame.key.get_pressed()    #包含整个键盘的bool类型值
        if key_pressed[K_w] or key_pressed[K_UP]:
            pass



if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

