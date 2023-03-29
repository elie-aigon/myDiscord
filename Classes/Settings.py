import pygame, sys, random, json, random, socket, mysql.connector
from threading import Thread
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox

ip = "127.0.0.1"

pygame.init()
pygame.mixer.init()

windowsize = (800, 500)
# Color

white = (255, 255, 255)
red = (255, 0, 0)
green = (74,184,97)
grey = (56,52,60)
grey_black = (43, 42, 45)
grey_black_hexa = "#2B2A2D"
grey_white = (91, 90, 94)
grey_white_hexa = "#5B5A5E"

# Font
font_mid = pygame.font.Font("Data/Font/LEMONMILK-MediumItalic.otf", 12) # message font
font_big = pygame.font.Font("Data/Font/LEMONMILK-MediumItalic.otf", 20) # status font
font_small = pygame.font.Font("Data/Font/LEMONMILK-MediumItalic.otf", 10) # input font
font_title = pygame.font.Font("Data/Font/LEMONMILK-MediumItalic.otf", 75)