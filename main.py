import pygame
import sys
import traceback
import player
import enemy
from pygame.locals import *    #常量
##### 初始化 #####
pygame.init()
pygame.mixer.init()

background_size = width,height = 480,700
screen = pygame.display.set_mode(background_size)    #如果直接写size记得set_mode(())
pygame.display.set_caption('plane war')

'''----- image -----'''
background_image = pygame.image.load(r'./image/sky.jpeg').convert()    #convert转换image的透明度,将图片进行surface对象，pygame现在会自动处理

'''----- sound -----'''
pygame.mixer.music.load(r'./sound/Un Amico.mp3')
bullet_sound = pygame.mixer.Sound(r'./sound/bullet.wav')
bullet_sound.set_volume(0.2)
missile = pygame.mixer.Sound('./sound/missile.wav')
missile.set_volume(0.2)

##### method #####
'''----- add enemies -----'''
def add_enemies_lv1(group1,group2,number):
    for i in range(number):
        lv1 = enemy.Enemy_Lv1(background_size)
        group1.add(lv1)
        group2.add(lv1)

def add_enemies_lv2(group1,group2,number):
    for i in range(number):
        lv2 = enemy.Enemy_Lv2(background_size)
        group1.add(lv2)
        group2.add(lv2)

def add_enemies_lv3(group1,group2,number):
    for i in range(number):
        lv3 = enemy.Enemy_Lv3(background_size)
        group1.add(lv3)
        group2.add(lv3)

##### 主程序 #####
def main():
    pygame.mixer.music.play(-1)    #循环播放
    clock = pygame.time.Clock()
    delay = 100  # 用于延时
    switch_image = True  # 切换显示image
    running = True

    me = player.Player(background_size)    #Player类实例化

    enemies = pygame.sprite.Group()    #所有的enemy建一个组，只要检测me跟这个组的碰撞就行
    enemies_lv1 = pygame.sprite.Group()
    add_enemies_lv1(enemies_lv1,enemies,15)
    enemies_lv2 = pygame.sprite.Group()
    add_enemies_lv2(enemies_lv2, enemies, 5)
    enemies_lv3 = pygame.sprite.Group()
    add_enemies_lv3(enemies_lv3, enemies, 2)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        '''----- 监听keyboard -----'''    #响应键盘操作：（1）通过检测事件消息如key_down消息，那么就是按下了按键。适用偶然按下！！！ （2）调用key模块里的get_press方法，使用会返回包含该按键bool值的序列 如果是True就说明按键按下。适用一直按着按键！！！
        key_pressed = pygame.key.get_pressed()    #包含整个键盘的bool类型值
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.move_up()
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            me.move_down()
        elif key_pressed[K_a] or key_pressed[K_LEFT]:
            me.move_left()
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.move_right()

        screen.blit(background_image, (0, 0))    #background image必须写在player image前面，反之则会遮挡display player
        '''----- switch display player -----'''
        delay -= 1
        if not delay:
            delay = 100

        if not(delay % 5):
            switch_image = not switch_image  # 取反(符号：~) 实现图片不断切换。这里不能使用更改判定bool值方法。
                                             # Python中，因为 True 等价于 1，而False等价于0，所以若变量a为True(即a=1),则 ~a 并不等于False，而是-2(因为a=11111110是-2的补码)

        if switch_image:
            screen.blit(me.player_image1,me.rect)
        else:
            screen.blit(me.player_image2,me.rect)

        '''----- display enemies -----'''

        for each in enemies_lv1:
            each
            screen.blit(each.image,each.rect)


        pygame.display.flip()  # flip() 更新整个待显示的Surface对象到屏幕上；update() 更新部分内容显示到屏幕上，如果没有参数，则与flip功能相同
        clock.tick(60)  # 设置成60帧

''''----- traceback error -----'''
if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

