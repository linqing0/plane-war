import pygame
import sys
import traceback

#####初始化#####
pygame.init()
pygame.mixer.init()

background_size = width,height = 480,700
screen = pygame.display.set_mode(background_size)
pygame.display.set_caption('plane war')

'''----- image -----'''
background_image = pygame.image.load(r'./image/sky.jpeg')    #convert转换image的透明度

'''----- sound -----'''
pygame.mixer.music.load(r'./sound/春花.mp3')



#####主程序#####
def main():
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                pygame.quit()
                sys.exit()

        screen.blit(background_image,(0,0))
        pygame.display.flip()
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