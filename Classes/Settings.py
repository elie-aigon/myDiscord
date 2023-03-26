import pygame, sys, random, json, random, socket
from threading import Thread

pygame.init()
pygame.mixer.init()

windowsize = (800, 500)
# Color

white = (255, 255, 255)
red = (255, 0, 0)
grey = (56,52,60)
grey_black = (43, 42, 45)
grey_white = (91, 90, 94)

# Font
font_mid = pygame.font.Font("Data/Font/LEMONMILK-MediumItalic.otf", 12)
font_big = pygame.font.Font("Data/Font/LEMONMILK-MediumItalic.otf", 39)
font_small = pygame.font.Font("Data/Font/LEMONMILK-MediumItalic.otf", 10)
font_title = pygame.font.Font("Data/Font/LEMONMILK-MediumItalic.otf", 75)