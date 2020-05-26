import pygame
import random

pygame.init()
winw = 800
winh = 600

game = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The python in python")
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

pygame.display.update()

clock = pygame.time.Clock()
squarew = 10
squareh = 10
menu = False
FPS = 30
fontsize = 50
font = pygame.font.SysFont(None, fontsize)

def snake(squarew, squareh, snakelist):
    for XY in snakelist:
        pygame.draw.rect(game, green, [XY[0], XY[1], squarew, squareh])
    
def msg_to_screen(msg, color):
    screentext = font.render(msg, True, color)
    game.blit(screentext, [0, round(winh/4)])

def gameloop():
    gameover = False
    bgcolor = 0
    leadx = round(winw/2)
    leady = round(winh/2)
    x = 0
    snakeList = []
    snakeLen = 1
    y = 0
    applex = (round(random.randrange(0, winw - squarew)))#/10)*10)
    appley = (round(random.randrange(0, winh - squareh)))#/10)*10)
    gamequit = False
    while not gamequit:

        while gameover == True:
            msg_to_screen("Game Over Press C to Countinue or Q to Quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamequit = True
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gamequit = True
                        gameover = False
                    elif event.key == pygame.K_c:
                        gameloop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamequit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = -squarew
                    y = 0
                elif event.key == pygame.K_RIGHT:
                    x = squarew
                    y = 0
                elif event.key == pygame.K_UP:
                    y = -squareh
                    x = 0
                elif event.key == pygame.K_DOWN:
                    y = squareh
                    x = 0

        if leadx >= winw or leadx < 0 or leady >= winh or leady < 0:
            gameover = True

        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN:                 
                if event.key == pygame.K_TAB and bgcolor == 1 and menu:
                    game.fill(black)
                    bgcolor = 0
                    pygame.time.delay(300)
                elif event.key == pygame.K_TAB and bgcolor == 0 and menu:
                    game.fill(white)
                    bgcolor = 1
                    pygame.time.delay(300)

        if bgcolor == 1:
            game.fill(white)
        elif bgcolor == 0:
            game.fill(black)
        
        leadx += x
        leady += y
        if not gameover:

            applet = 30
            pygame.draw.rect(game, red, [applex, appley, applet, applet])

            
            snakeHead = []
            snakeHead.append(leadx)
            snakeHead.append(leady)
            snakeList.append(snakeHead)
            
            if len(snakeList) > snakeLen:
                del snakeList[0]

            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    gameover = True

                
            snake(squarew, squareh, snakeList)

                 
            pygame.display.update()

##            if leadx == applex and leady == appley:
##                applex = (round(random.randrange(0, winw - squarew)/10)*10)
##                appley = (round(random.randrange(0, winh - squareh)/10)*10)
##                snakeLen += 1
            
            if leadx >= applex and leadx <= applex + applet:
                if leady >= appley and leady <= appley + applet:
                    applex = (round(random.randrange(0, winw - squarew)))#/10)*10)
                    appley = (round(random.randrange(0, winh - squareh)))#/10)*10)
                    snakeLen += 1
                
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()

gameloop()

