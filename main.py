import os
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
background_image = pygame.image.load(r'./image/sky.jpeg').convert()    #convert转换image的透明度

'''----- sound -----'''
background_music = pygame.mixer