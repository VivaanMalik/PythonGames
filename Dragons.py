import pygame
import os
import csv
import inspect
pygame.init()

winw = 1344
winh = 768
bgcolor = 0


game = pygame.display.set_mode((winw, winh))
pygame.display.set_caption("Dragons")

fulfilepath = os.getcwd() + "\\" + "Dragonssave.csv"
mmenu = True
white = (255, 255, 255)
black = (0, 0, 0)
mapno = 1
gamequit = False
clock = pygame.time.Clock()
bg = pygame.image.load('map1.png')
bg = pygame.transform.scale(bg, (1344, 768))
player = pygame.image.load('player_23.png')


def msg_to_screen(msg, color, textx, texty, fontsize):
    font = pygame.font.SysFont(None, fontsize)
    screentext = font.render(msg, True, color)
    game.blit(screentext, [textx, texty])
    
def writehigh(highscore):
    global fullfilepath
    file = open(fullfilepath, "w")
    writestring = "HIGHSCORE,"+ str(highscore)
    file.write(writestring)
    file.close()

def readhigh():
    global highscore
    global fullfilepath
    with open(fullfilepath, "r") as file:
        row = file.read()
        elements=row.split(',')
        if "HIGHSCORE" in row:
            highscore = int(elements[1])
        file.close()


def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

#print ("hello, this is line number"+ str(lineno())+__name__ )
        
def gameloop():
    x = 480
    y = 512
    global bg
    global gamequit
    global mapno
    global player
    while not gamequit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamequit = True
            if event.type == pygame.KEYDOWN:


            #Map1 movements
                
                if mapno == 1:
                    if event.key == pygame.K_LEFT:
                        player = pygame.image.load('player_14.png')
                        if x == 608 and y <= 448 and y >= 352:
                            x+=0
                        elif y == 480 and x == 352 or y == 480 and x == 672:
                            x+=0
                        elif x== 704:
                            if y <= 448 and y >= 352:
                                x+=0
                            else:
                                x+=-32
                        elif x == 192 and y <= 448 and y >= 352:
                            x+=0
                        elif x == 1216 and y <= 448 and y >= 352:
                            x+=0
                        elif x == 640 or x == 1056:
                            if y >= 608 and y <=672:
                                x+=0
                            else:
                                x+=-32
                        elif x == 64 and y == 224:
                            x+=0
                        else:
                            x += -32
                        
                    elif event.key == pygame.K_RIGHT:
                        player = pygame.image.load('player_11.png')
                        if x == 352:
                            if y <= 448 and y >=352:
                                x+=0
                            else:
                                x+=32
                        elif y == 480 and x == 288 or y == 480 and x == 608:
                            x+=0
                        elif x == 256:
                            if y <= 448 and y >= 352:
                                x+=0
                            else:
                                x+=32
                        elif x == 64 and y <= 448 and y >= 352:
                            x+=0
                        elif x == 768 and y <= 448 and y >= 352:
                            x+=0
                        elif x == 672 or x == 1088:
                            if y >= 608 and y <=672:
                                x+=0
                            else:
                                x+=32
                        elif x == 512 and y == 224:
                            x+=0
                        else:
                            x += 32
                        
                    elif event.key == pygame.K_UP:
                        player = pygame.image.load('player_02.png')
                        if x >= 640 and x <=1280 and y == 256:
                            y += 0
                        elif y == 224:
                            if x == 512 or x == 448 or x == 384 or x == 320 or x == 256 or x == 192 or x == 128 or x == 64:
                                bg = pygame.image.load('map2.png')
                                bg = pygame.transform.scale(bg, (1344, 768))
                                x = 640
                                y = 640
                                mapno = 2
                            elif x<=512 and x>=64:
                                y+=0
                            else:
                                y += -32
                        elif y == 256 and x == 0 or x == 32 and y == 256 or x == 544 and y == 256 or x == 576 and y == 256 or x == 608 and y == 256:
                            y+=0
                        elif y == 480 and x == 480:
                            bg = pygame.image.load('map3.png')
                            bg = pygame.transform.scale(bg, (640, 640))
                            x = 320
                            y = 576
                            mapno = 3
                        elif y == 480 and x>=384 and x <= 448:
                            y+=0
                        elif y == 480 and x>=512 and x <= 576:
                            y+=0
                        elif y == 512 and x == 320 or y == 512 and x == 640:
                            y+=0
                        elif y == 480 and x <= 1184 and x >= 800:
                            y+=0
                        elif y == 480 and x == 96 or y == 480 and x == 160:
                            y+=0
                        elif y == 480 and x == 288 or y == 480 and x == 352 or y == 480 and x == 608 or y == 480 and x == 672:
                                y+=0
                        elif x == 128 and y == 480:
                            bg = pygame.image.load('map4.png')
                            bg = pygame.transform.scale(bg, (320, 640))
                            x = 128
                            y = 512
                            mapno = 4
                        else:
                            y += -32
                            
                    elif event.key == pygame.K_DOWN:
                        player = pygame.image.load('player_23.png')
                        if y == 320:
                            if x >= 64 and x <= 192 or x >= 288 and x <= 672 or x >= 768 and x <= 1216:
                                y+=0
                            else:
                                y+=32
                        elif y == 576:
                            if x >= 0 and x <= 608 or x >= 704 and x <= 1024 or x >= 1120 and x <= 1280:
                                y+=0
                            else:
                                y+=32
                        else:
                            y += 32



                if mapno == 2:
                    if event.key == pygame.K_LEFT:
                        player = pygame.image.load('player_14.png')
                        if x == 0:
                            x+=0
                        else:
                            x += -32
                        
                    elif event.key == pygame.K_RIGHT:
                        player = pygame.image.load('player_11.png')
                        if x == 1280:
                            x+=0
                        else:
                            x += 32
                        
                    elif event.key == pygame.K_UP:
                        player = pygame.image.load('player_02.png')
                        if y == 0:
                            y+=0
                        else:
                            y += -32
                            
                    elif event.key == pygame.K_DOWN:
                        player = pygame.image.load('player_23.png')
                        if y == 704:
                            bg = pygame.image.load('map1.png')
                            bg = pygame.transform.scale(bg, (1344, 768))
                            x = 256
                            y = 224
                            mapno = 1
                        else:
                            y += 32


                            
                if mapno == 3:
                    if event.key == pygame.K_LEFT:
                        player = pygame.image.load('player_14.png')
                        if x == 0:
                            x+=0
                        else:
                            x += -32
                        
                    elif event.key == pygame.K_RIGHT:
                        player = pygame.image.load('player_11.png')
                        if x == 576:
                            x+=0
                        elif x == 544:
                            if y == 0:
                                x+=0
                            elif y == 64:
                                bg = pygame.image.load('map5.png')
                                bg = pygame.transform.scale(bg, (640, 640))
                                x += 32
                                mapno = 5
                            elif y == 512:
                                x+=0
                            elif y == 576:
                                x+=0
                            else:
                                x+=32
                        elif x == 480 and y == 576:
                            x+=0
                        elif x == 224:
                            if y == 448 or y == 384 or y == 320 or y == 256:
                                x+=0
                            else:
                                x+=32
                        elif y == 0:
                            if x == 160 or x == 224 or x == 288:
                                x+=0
                            else:
                                x+= 32
                        else:
                            x += 32
                        
                    elif event.key == pygame.K_UP:
                        player = pygame.image.load('player_02.png')
                        if y == 0:
                            y+=0
                        else:
                            y += -32
                            
                    elif event.key == pygame.K_DOWN:
                        player = pygame.image.load('player_23.png')
                        if y == 576:
                            bg = pygame.image.load('map1.png')
                            bg = pygame.transform.scale(bg, (1344, 768))
                            x = 480
                            y = 480
                            mapno = 1
                        else:
                            y += 32

                                

        print(x, y)
        game.fill(black)
        game.blit(bg, (0, 0))
        game.blit(player, (x, y))
        pygame.display.update()
        clock.tick(15)
    pygame.quit()
    quit

    
gameloop()
