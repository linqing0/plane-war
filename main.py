import pygame
import sys
import traceback

#####初始化#####
pygame.init()
pygame.mixer.init()

background_size = width,height = 480,700
screen = pygame.display.set_mode(background_size)
pygame.display.set_caption('plane war')

background_image = pygame.image.load(r'D:\python\x\plane-war\image\sky.jpeg').convert()    #convert 变换background透明度

background_image.blit()