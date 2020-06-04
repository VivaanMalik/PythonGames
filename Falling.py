import pygame
import random
import os
import csv
import inspect

#comment123
def logtoshell(logstr):
    debug=1
    if (debug ==1):
        cf = currentframe()
        filename = inspect.getframeinfo(cf).filename
        print ("Python says line ", cf.f_lineno, logstr)

highscore =0
pygame.init()
hide = False
nomfallx =0
nomfally = 0
winw = 1020
winh =700
bgcolor = 0
pause = False

gamewindow = pygame.display.set_mode((winw, winh))
pygame.display.set_caption("Blockificisation")
s = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

green = (0, 255, 0)
red=(255, 0, 0)
fontsize = 30
font = pygame.font.SysFont(None, fontsize)
mmenu = True
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
hide = False
g = 1
l = 5
speed = 10 
dirname = os.getcwd()
filename = "gameparameters.csv"
fullfilepath = dirname + "\\"+filename



def writehigh(highscore):
    global fullfilepath
    file = open(fullfilepath, "w")
    writestring = "HIGHSCORE,"+ str(highscore)
    file.write(writestring)
#    print(writestring)
    file.close()
#    logtoshell("ashish")

def readhigh():
    global highscore
    global fullfilepath
    with open(fullfilepath, "r") as file:
        row = file.read()
        elements=row.split(',')
        if "HIGHSCORE" in row:
            highscore = int(elements[1])
        file.close()
        
def msg_to_screen(msg, color, textx, texty):
    screentext = font.render(msg, True, color)
    gamewindow.blit(screentext, [textx, texty])
    

def nomfall(X, Y):
    global hide
    global nomfallx, nomfally
    global s
    global g
    global l
    global speed
    global pause
    global bgolor
    if g == l- 1:
        red = (0, 255, 0)
    else:
        red = (255, 0, 0)
        
    if hide == True:
        nomfally = 0
        nomfallx = (round(random.randrange(0, 950)/50)*50)+10
        pygame.draw.rect(gamewindow, red, [nomfallx, nomfally, 50, 50])
        pygame.display.update
        g+=1
        if g==l:
            l +=1
            g = 0
            t = 0
            s = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
            c = 1
            speed += 5
        hide = False

    elif hide == False:
        pygame.draw.rect(gamewindow, red, [nomfallx, nomfally, 50, 50])
        pygame.display.update
        
    if g == l- 1:
        red = (0, 255, 0)
    else:
        red = (255, 0, 0)
        
def menu():

    global bgcolor
    global mmenu
    pygame.mixer.music.load('C:\\Users\\ashish\\Documents\\GitHub\\PythonGames\\Falling.mp3')
    pygame.mixer.music.play(-1)
    while mmenu == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                colwhite = False
                if event.key == pygame.K_1:
                    gamewindow.fill(black)
                    bgcolor = 0
                    colwhite = False
                    pygame.time.delay(300)
                if event.key == pygame.K_2:
                    gamewindow.fill(white)
                    bgcolor = 1
                    colwhite = True
                    pygame.time.delay(300)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_RETURN:
                    mmenu = False
                elif event.key == pygame.K_o:
                    if bgcolor == 0:
                        msg_to_screen("Avoid all red blocks and damaged areas", white, 300, 380)
                        msg_to_screen("Left Arrow - left   Right Arrow - right", white, 300, 410)
                    else:
                        msg_to_screen("Avoid all red blocks and damaged areas", black, 300, 380)
                        msg_to_screen("Left Arrow - left   Right Arrow - right", black, 300, 410)
            if bgcolor == 0:
                pygame.draw.rect(gamewindow, white, [135, 330, 750, 40])
                msg_to_screen("1,2 - change color   Esc - Exit   Enter - Play   O - objective", black, 225, 340)
            else:
                pygame.draw.rect(gamewindow, black, [135, 330, 750, 40])
                msg_to_screen("1,2 - change color   Esc - Exit   Enter - Play   O - objective", white, 225, 340)
            pygame.display.update()
    pygame.mixer.music.pause()
    gameloop()
    
            
def gameloop():
    score = 0
    i=1
    oer = True
    global hide
    global nomfallx, nomfally
    global s
    global speed
    global pause
    global highscore
    global bgcolor
    hide = False
    catch = False
    Color = 0
    gameover = False
    gamequit = False
    X = winw/2
    Y = 500
    fps = 30
    clock = pygame.time.Clock()
    nomfally = 0
    nomfallx = (round(random.randrange(0, 950)/50)*50)+10
    

    pygame.mixer.music.unpause()
    
    while not gamequit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                writehigh(int(highscore))
                gamequit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    X += -50
                elif event.key == pygame.K_RIGHT:
                    X += 50


        readhigh()

            
        while gameover == True:
            if bgcolor == 0 and oer:
                msg_to_screen("Game Over: Press Enter to Restart or Esc to Quit", white, 20, 350)
                oer = False
            elif bgcolor == 1 and oer:
                msg_to_screen("Game Over: Press Enter to Restart or Esc to Quit", black, 20, 350)
                oer = False
            pygame.display.update()
            pygame.mixer.music.pause()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamequit = True
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        readhigh()
                        gamequit = True
                        gameover = False
                    elif event.key == pygame.K_RETURN:
                        hide = False
                        nomfallx =0
                        nomfally = 0
                        pause = False
                        s = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
                        g = 1
                        l = 5
                        speed = 10
                        readhigh()
                        print(highscore)
                        gameloop()



        if bgcolor == 1 or white == True:
         gamewindow.fill(white)
         col = black
        elif bgcolor == 0:
            gamewindow.fill(black)
            col = white
         
        if X <= 0 or X>=970:
            if X<=0:
                X = 10
            else:
                X = 960


        i=10
        if s[0]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[1]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[2]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[3]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[4]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[5]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[6]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[7]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[8]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[9]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[10]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[11]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[12]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[13]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[14]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[15]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[16]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[17]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[18]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        i+=50
        if s[19]:
            pygame.draw.rect(gamewindow, col, [i, 540, 50, 50])
        
        if nomfally >= 500 and hide == False:
            score+=1
            if nomfallx == 10:
                s[0] = False
                hide = True
            elif nomfallx == 60:
                s[1] = False
                hide = True
            elif nomfallx == 110:
                s[2] = False
                hide = True
            elif nomfallx == 160:
                s[3] = False
                hide = True
            elif nomfallx == 210:
                s[4] = False
                hide = True
            elif nomfallx == 260:
                s[5] = False
                hide = True
            elif nomfallx == 310:
                s[6] = False
                hide = True
            elif nomfallx == 360:
                s[7] = False
                hide = True
            elif nomfallx == 410:
                s[8] = False
                hide = True
            elif nomfallx == 460:
                s[9] = False
                hide = True
            elif nomfallx == 510:
                s[10] = False
                hide = True
            elif nomfallx == 560:
                s[11] = False
                hide = True
            elif nomfallx == 610:
                s[12] = False
                hide = True
            elif nomfallx == 660:
                s[13] = False
                hide = True
            elif nomfallx == 710:
                s[14] = False
                hide = True
            elif nomfallx == 760:
                s[15] = False
                hide = True
            elif nomfallx == 810:
                s[16] = False
                hide = True
            elif nomfallx == 860:
                s[17] = False
                hide = True
            elif nomfallx == 910:
                s[18] = False
                hide = True
            elif nomfallx == 960:
                s[19] = False
                hide = True

        
                
        nomfally += speed
        nomfall(X, Y)
        pygame.draw.rect(gamewindow, blue, [X, Y, 50, 50])
        r = 0
        e = 10
        while r <= 19:
            if s[r] == False and X == e:
                gameover = True
            r+=1
            e+=50
        if highscore >= score:
            highscore=highscore
        elif highscore <= score:
            highscore = score
        if bgcolor == 0:
            msg_to_screen("Score: " + str(score), white, 0, 0)
            msg_to_screen("High Score: " + str(highscore), white, 850, 0)
        else:
            msg_to_screen("Score: " + str(score), black, 0, 0)
            msg_to_screen("High Score: " + str(highscore), black, 850, 0)
        writehigh(int(highscore))

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

    writehigh(int(highscore))
menu()


