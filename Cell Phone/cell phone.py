import pygame
import ctypes
import os
#put apple guy
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
font=pygame.font.SysFont('Comic Sans Ms', 30, True, True)
bg=pygame.image.load('background.png')
bg=pygame.transform.scale(bg, (screensize))
textbox=pygame.Surface((winw, winh/8))
textbox.set_alpha(100)
textbox.fill((0,0,0))
battery=pygame.image.load('Battery.png')
battery=pygame.transform.scale(battery, (round(winw/8), round(winh/8)))
Manscale=(int(round((winw/16)*1.4)),int(round((winh/16)*2.5)))
Man=pygame.image.load('ManwithPhone.png')
Man = pygame.transform.scale(Man, (Manscale))
Manx=round(winw/2- (int(round((winw/16)*1.4))/2))
Many=round(winh/1.3)
phone=pygame.image.load('Phone.png')
phonescale=int(winh/1.5)
phone = pygame.transform.scale(phone, (phonescale, phonescale))
bgx=0
bgy=0
Mall=pygame.image.load('Mall.png')
Mall=pygame.transform.scale(Mall, (winw, winh))
Mallx=0-(winw*3)
Mally=0
AppleLogo=pygame.image.load('Apple.png')
AppleLogo=pygame.transform.scale(AppleLogo, (int(winh/4), int(winh/4)))
Applex=int(round(Mallx+(winw/2)+winw/8))
Appley=int(round(Mally+winh/5))
appleguy=pygame.image.load('apple guy.jpg')
applegh=int((winh/8)*2.5)
applegw=int(round(((applegh/5)*6)/2))
appleguy=pygame.transform.scale(appleguy, (applegw, applegh))
appleguyx=int(round(Mallx+(winw/2)))
appleguyy=int(round(winh/1.5))
introduction_of_appleguy=False

def msg_to_screen(orig_msg):
    global bgx, bgy
    global bg, textbox, battery, Man, Manx, Many, Mall, Mallx, Mally, AppleLogo
    #screentext = font.render(msg, True, (255, 255, 255))
    #game.blit(screentext, [0, 0])
    msg=orig_msg
    msg=list(msg)
    fps=5
    text_letter=0
    while text_letter<=len(msg)-1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            screentext=font.render(str(orig_msg), True, (255, 255, 255))
            
            game.blit(bg, (bgx, bgy))
            game.blit(bg, (bgx+winw, bgy))
            game.blit(bg, (bgx-winw, bgy))
            game.blit(Mall, (Mallx, Mally))
            game.blit(AppleLogo,(Applex, Appley))
            game.blit(textbox, (0,0))
            game.blit(Man, (Manx, Many))
            game.blit(appleguy, (appleguyx, appleguyy))
            game.blit(battery, (10, ((winh/8)+10)))
            game.blit(phone, (int(winw/1.4), int(winh/4)))
            game.blit(screentext, [0,0])
            text_letter=len(msg)
            pygame.display.update()
        else:                
            screentext = font.render(msg[text_letter], True, (255, 255, 255))
            game.blit(screentext, [text_letter*30, 0])
            text_letter+=1
            pygame.time.delay(100)
            pygame.display.update()
    pygame.time.delay(1000)
    
    game.blit(bg, (bgx, bgy))
    game.blit(bg, (bgx+winw, bgy))
    game.blit(bg, (bgx-winw, bgy))
    game.blit(Mall, (Mallx, Mally))
    game.blit(AppleLogo,(Applex, Appley))
    game.blit(textbox, (0,0))
    game.blit(Man, (Manx, Many))
    game.blit(appleguy, (appleguyx, appleguyy))
    game.blit(battery, (10, ((winh/8)+10)))
    game.blit(phone, (int(winw/1.4), int(winh/4)))
        
def gameloop():
    Manflip=0#0=left, 1 =right
    clock=pygame.time.Clock()
    fps=30
    msg_display=False
    textbox=pygame.Surface((winw, winh/8))
    textbox.set_alpha(100)
    textbox.fill((0,0,0))
    battery=pygame.image.load('Battery.png')
    battery=pygame.transform.scale(battery, (round(winw/8), round(winh/8)))
    batterycolor=(0, 255, 0)
    batterywidth=round((winw/8)*0.85)
    originalbatterywidth=batterywidth
    battery_percent_multiplier=100
    Manx=round(winw/2- (int(round((winw/16)*1.4))/2))
    Many=round(winh/1.3)
    Manscale=(int(round((winw/16)*1.4)),int(round((winh/16)*2.5)))
    Man=pygame.image.load('ManwithPhone.png')
    Man = pygame.transform.scale(Man, (Manscale))
    


    gamequit=False
    bg=pygame.image.load('background.png')
    bg=pygame.transform.scale(bg, (screensize))
    leftcheck=False
    rightcheck=False
    global Mallx, Mally
    global bgx, bgy, AppleLogo
    
    while not gamequit:
        appleguyx=int(round(Mallx+(winw/2)))
        appleguyy=int(round(winh/1.5))
        Applex=int(round(Mallx+(winw/2)-(winw/16)))
        Appley=int(round(Mally+winh/5))
        if bgx>=winw:
            bgx-=winw
        elif bgx<=0-winw:
            bgx+=winw
        game.blit(bg, (bgx, bgy))
        game.blit(bg, (bgx+winw, bgy))
        game.blit(bg, (bgx-winw, bgy))
        game.blit(Mall, (Mallx, Mally))
        game.blit(AppleLogo,(Applex, Appley))
        game.blit(Man, (Manx, Many))
        game.blit(appleguy, (appleguyx, appleguyy))
        game.blit(textbox, (0,0))
        pygame.draw.rect(game, batterycolor, [15, ((winh/8)+15), batterywidth, round(winh/8-5)])
        game.blit(battery, (10, ((winh/8)+10)))
        game.blit(phone, (int(winw/1.4), int(winh/4)))
        pygame.display.update()
        if batterywidth>=2:
            batterywidth=originalbatterywidth/100
            batterywidth*=battery_percent_multiplier
            battery_percent_multiplier-=1
            if batterywidth<=originalbatterywidth/2:
                batterycolor=(255, 255, 0)
            if batterywidth<=originalbatterywidth/4:
                batterycolor=(255, 0, 0)
        
            pygame.time.wait(50)
        
        game.blit(bg, (bgx, bgy))
        game.blit(bg, (bgx+winw, bgy))
        game.blit(bg, (bgx-winw, bgy))
        game.blit(Mall, (Mallx, Mally))
        game.blit(AppleLogo,(Applex, Appley))
        game.blit(textbox, (0,0))
        game.blit(Man, (Manx, Many))
        game.blit(appleguy, (appleguyx, appleguyy))
        pygame.draw.rect(game, batterycolor, [15, ((winh/8)+15), batterywidth, round(winh/8-5)])
        game.blit(battery, (10, ((winh/8)+10)))
        game.blit(phone, (int(winw/1.4), int(winh/4)))
        pygame.display.update()

        #battery empty
        if batterywidth<=10 and not msg_display==True:
            batterywidth=0
            msg_to_screen("PRESS ENTER IF YOU WANT ME TO SPEAK FASTER")
            msg_to_screen("OH NO!!! MY STUPID PHONE'S BATTERY HAS DIED... UGH!")
            msg_to_screen("WHAT AM I GONNA DO NOW?!")
            msg_to_screen("ANYWAYS, I WAS PLANNING ON BUYING ANOTHER ONE")
            msg_to_screen("SINCE, YOU KNOW, PEOPLE HARDLY USE ONE FOR 2 YEARS")
            msg_to_screen("WELL, ACCORDING TO STATISTICS AT LEAST")
            msg_to_screen("OH HI BY THE WAY!!! I AM BRUCE CELLPHONEYSON.")
            msg_to_screen("YOU CAN CONTROL ME USING THE ARROW KEYS...")
            msg_to_screen("YOU CAN USE NUMBER KEYS TO CHOOSE BETWEEN OPTIONS")
            msg_to_screen("CHECK IT OUT!!!")

            left_check_counts=0
            right_check_counts=0
            while not rightcheck==True and not leftcheck==True:
                if bgx>=winw:
                    bgx-=winw
                elif bgx<=0-winw:
                    bgx+=winw
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gamequit = True
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    bgx += 5
                    if Manflip==1:
                        Man=pygame.transform.flip(Man, True, False)
                        Manflip=0
                        left_check_counts+=1
                        if left_check_counts==3:
                            leftcheck=True
                if keys[pygame.K_RIGHT]:
                    bgx -= 5
                    if Manflip==0:
                        Man=pygame.transform.flip(Man, True, False)
                        Manflip=1
                        right_check_counts+=1
                        if right_check_counts==3:
                            rightcheck=True
                Applex=int(round(Mallx+(winw/2)-(winw/16)))
                Appley=int(round(Mally+winh/5))
                appleguyx=round(Mallx+(winw/4))
                appleguyy=round(winh/1.3)
                game.blit(bg, (bgx, bgy))
                game.blit(bg, (bgx+winw, bgy))
                game.blit(bg, (bgx-winw, bgy))
                game.blit(Mall, (Mallx, Mally))
                game.blit(AppleLogo,(Applex, Appley))
                game.blit(Man, (Manx, Many))
                game.blit(appleguy, (appleguyx, appleguyy))
                game.blit(textbox, (0,0))
                pygame.draw.rect(game, batterycolor, [15, ((winh/8)+15), batterywidth, round(winh/8-5)])
                game.blit(battery, (10, ((winh/8)+10)))
                game.blit(phone, (int(winw/1.4), int(winh/4)))
                pygame.display.update()

            
            msg_to_screen("NOW MOVE LEFT AND GO TO THE APPLE STORE...")
            msg_to_screen("YOU'LL FIND HELP THERE...")
            msg_to_screen("<-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--")
            msg_display=True

        #talking to appleguy
            
        if Manx==appleguyx+applegw:
            msg_to_screen("Press Space to talk")
            while introduction_of_appleguy==False:
                for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                   keys = pygame.key.get_pressed()
                   if keys[pygame.K_SPACE]:
                       msg_to_screen("Well, Hello there!!!")
                       msg_to_screen("I am Bob Cena")
                       msg_to_screen("I will show you 'The Life cycle of a phone'")
                       msg_to_screen("And you can make your own phone too!!!")
                       introduction_of_appleguy=True
                   
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamequit = True
        if msg_display==True:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                bgx += 10
                Mallx+=15
                if Manflip==1:
                    Man=pygame.transform.flip(Man, True, False)
                    Manflip=0

            if keys[pygame.K_RIGHT]:
                bgx -= 10
                Mallx-=15
                if Manflip==0:
                    Man=pygame.transform.flip(Man, True, False)
                    Manflip=1
      
 
        game.blit(bg, (bgx, bgy))
        game.blit(bg, (bgx+winw, bgy))
        game.blit(bg, (bgx-winw, bgy))
        game.blit(Mall, (Mallx, Mally))
        game.blit(AppleLogo,(Applex, Appley))
        game.blit(appleguy, (appleguyx, appleguyy))
        game.blit(Man, (Manx, Many))
        game.blit(textbox, (0,0))
        pygame.draw.rect(game, batterycolor, [15, ((winh/8)+15), batterywidth, round(winh/8-5)])
        game.blit(battery, (10, ((winh/8)+10)))
        game.blit(phone, (int(winw/1.4), int(winh/4)))
        clock.tick(fps)        
        pygame.display.update()
        
    pygame.quit()
    
gameloop()
