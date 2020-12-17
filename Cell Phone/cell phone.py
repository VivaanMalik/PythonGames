import pygame
import ctypes
import os
winx=0
winy=30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (winx,winy)
pygame.init()
Icon=pygame.image.load('Phone Icon.png')
pygame.display.set_icon(Icon)
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)-30
winw=user32.GetSystemMetrics(0)
winh=user32.GetSystemMetrics(1)
game = pygame.display.set_mode((screensize))
pygame.display.set_caption("Life Cycle of a Phone!!!")

def gameloop():
    textbox=pygame.Surface((winw, winh/8))
    textbox.set_alpha(100)
    textbox.fill((0,0,0))
    
    Manx=round(winw/2- (int(round((winw/16)*1.4))/2))
    Many=round(winh/1.5)
    Manscale=(int(round((winw/16)*1.4)),int(round((winh/16)*2.5)))
    Man=pygame.image.load('ManwithPhone.png')
    Man = pygame.transform.scale(Man, (Manscale))
    gamequit=False
    bg=pygame.image.load('background.png')
    bg=pygame.transform.scale(bg, (screensize))
    while not gamequit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamequit = True
        game.blit(bg, (0, 0))
        game.blit(Man, (Manx, Many))
        game.blit(textbox, (0,0))
        #pygame.draw.rect(game, pygame.Color(0,0,0, 128),[0,0,winw, winh/8])
        


        pygame.display.update()
        
    pygame.quit()
    
gameloop()
