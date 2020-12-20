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
Many=round(winh/1.5)
phone=pygame.image.load('Phone.png')
phonescale=int(winh/1.5)
phone = pygame.transform.scale(phone, (phonescale, phonescale))

def msg_to_screen(orig_msg):
    global bg, textbox, battery, Man, Manx, Many
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
            game.blit(bg, (0, 0))
            game.blit(textbox, (0,0))
            game.blit(Man, (Manx, Many))
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
    game.blit(bg, (0, 0))
    game.blit(textbox, (0,0))
    game.blit(Man, (Manx, Many))
    game.blit(battery, (10, ((winh/8)+10)))
    game.blit(phone, (int(winw/1.4), int(winh/4)))
        
def gameloop():
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
    Many=round(winh/1.5)
    Manscale=(int(round((winw/16)*1.4)),int(round((winh/16)*2.5)))
    Man=pygame.image.load('ManwithPhone.png')
    Man = pygame.transform.scale(Man, (Manscale))
    gamequit=False
    bg=pygame.image.load('background.png')
    bg=pygame.transform.scale(bg, (screensize))
    
    while not gamequit:
        game.blit(bg, (0, 0))
        game.blit(Man, (Manx, Many))
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
        
        game.blit(bg, (0, 0))
        game.blit(textbox, (0,0))
        game.blit(Man, (Manx, Many))
        pygame.draw.rect(game, batterycolor, [15, ((winh/8)+15), batterywidth, round(winh/8-5)])
        game.blit(battery, (10, ((winh/8)+10)))
        game.blit(phone, (int(winw/1.4), int(winh/4)))
        pygame.display.update()    
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
            msg_display=True

        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamequit = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            Manx -= 5

        if keys[pygame.K_RIGHT]:
            Manx += 5
 
        game.blit(bg, (0, 0))
        game.blit(Man, (Manx, Many))
        game.blit(textbox, (0,0))
        pygame.draw.rect(game, batterycolor, [15, ((winh/8)+15), batterywidth, round(winh/8-5)])
        game.blit(battery, (10, ((winh/8)+10)))
        game.blit(phone, (int(winw/1.4), int(winh/4)))
        
        pygame.display.update()
        
    pygame.quit()
    
gameloop()
