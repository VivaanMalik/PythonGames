import pygame
import ctypes
import os
winx=0
winy=30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (winx,winy)
pygame.init()
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)-30

gamewindow = pygame.display.set_mode((screensize))
pygame.display.set_caption("Life Cycle of a Phone!!!")

def gameloop():
    gamequit=False
    while not gamequit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamequit = True
    pygame.quit()
gameloop()
