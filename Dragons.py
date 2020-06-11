import pygame
import os
import csv
import inspect
import random
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
dl = (480, 512)
red = (255,0, 0)
rank = "Dragon Trainer"
money_count = 0
your_dragon = False

def menu():
    global your_dragon
    menubg = pygame.image.load('Dragons_wallpaper.jpg')
    menubg = pygame.transform.scale(menubg, (1344, 768))
    game.blit(menubg, (0, 0))
    your_dragon_ = 'nothing'
    while your_dragon_ == 'nothing':
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    your_dragon = pygame.image.load('dragons\\Black 4.png')
                elif event.key == pygame.K_2:
                    your_dragon = pygame.image.load('dragons\\Blue 3.png')
                elif event.key == pygame.K_3:
                    you_dragon = pygame.image.load('dragons\\Red 4.png')
                elif event.key == pygame.K_4:
                    your_dragon = pygame.image.load('dragons\\Yellow 2.png')

                elif event.key == pygame.K_RETURN:
                    if your_dragon == False:
                        your_dragon = False
                    else:
                        your_dragon = pygame.transform.scale(your_dragon, (200, 200))
                        gameloop()
                
            
        pygame.display.update()

your_dragon = your_dragon

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


def msg(msg, textx, texty, fontsize):
    i = 0
    while i !=255:
        msg_to_screen(msg, (i, i, i), textx, texty, fontsize)
        i+=1
        pygame.display.update()
    pygame.time.delay(3000)
    while i !=0:
        msg_to_screen(msg, (i, i, i), textx, texty, fontsize)
        i-=1
        pygame.display.update()
    i = 0



def Start():
    start = True
    if start == True:
        msg("You are now in a world full of Dragons", 325, 300, 50)
        msg("Here you are starting as a Dragon Trainer", 300, 300, 50)
        msg("You have only one goal here...", 375, 300, 50)
        msg("To Tame the King of Dragons.", 375, 300, 50)
        msg("You have aldready got the starter Dragon", 300, 300, 50)
        msg("Start you journey - Explore areas and battle your way to the top", 150, 300, 50)
        start = False
    gameloop()

def Battle():
    global your_dragon
    battle_num = random.randrange(1, 16)
    if battle_num == 1:
        battle_dragon = pygame.image.load('dragons\\Blue 1.png')
    elif battle_num == 2:
        battle_dragon = pygame.image.load('dragons\\Blue 2.png')
    elif battle_num == 3:
        battle_dragon = pygame.image.load('dragons\\Blue 3.png')
    elif battle_num == 4:
        battle_dragon = pygame.image.load('dragons\\Blue 4.png')
    elif battle_num == 5:
        battle_dragon = pygame.image.load('dragons\\Red 1.png')
    elif battle_num == 6:
        battle_dragon = pygame.image.load('dragons\\Red 2.png')
    elif battle_num == 7:
        battle_dragon = pygame.image.load('dragons\\Red 3.png')
    elif battle_num == 8:
        battle_dragon = pygame.image.load('dragons\\Red 4.png')
    elif battle_num == 9:
        battle_dragon = pygame.image.load('dragons\\Green 1.png')
    elif battle_num == 10:
        battle_dragon = pygame.image.load('dragons\\Green 2.png')
    elif battle_num == 11:
        battle_dragon = pygame.image.load('dragons\\Green 3.png')
    elif battle_num == 12:
        battle_dragon = pygame.image.load('dragons\\Green 4.png')
    elif battle_num == 13:
        battle_dragon = pygame.image.load('dragons\\Yellow 1.png')
    elif battle_num == 14:
        battle_dragon = pygame.image.load('dragons\\Yellow 2.png')
    elif battle_num == 15:
        battle_dragon = pygame.image.load('dragons\\Yellow 3.png')
    elif battle_num == 16:
        battle_dragon = pygame.image.load('dragons\\Yellow 4.png')
    battle_dragon = pygame.transform.scale(battle_dragon, (200, 200))
        
    pen = pygame.image.load('items\\genericItem_color_025.png')
    pen = pygame.transform.scale(pen, (50, 50))
    camera = pygame.image.load('items\\genericItem_color_045.png')
    camera = pygame.transform.scale(camera, (50, 50))
    healing = pygame.image.load('items\\genericItem_color_102.png')
    healing = pygame.transform.scale(healing, (50, 50))
    trap = pygame.image.load('items\\genericItem_color_105.png')
    trap = pygame.transform.scale(trap, (50, 50))
    pill1 = pygame.image.load('items\\genericItem_color_089.png')
    pill1 = pygame.transform.scale(pill1, (50, 50))
    pill2 = pygame.image.load('items\\genericItem_color_090.png')
    pill2 = pygame.transform.scale(pill2, (50, 50))

    battle = True
    optx = 775
    opty = 495
    bag_items = False
    itemno = 0
    bagitem = [pen, camera, healing, trap, pill1, pill2]
    
    while battle == True:
        pygame.draw.rect(game, white, [336, 192, 672, 380])
        game.blit(battle_dragon, (803, 197))
        game.blit(your_dragon, (341, 192))
        battleopt = pygame.image.load('buttons\\panelInset_brown.png')
        battleopt = pygame.transform.scale(battleopt, (650, 80))
        game.blit(battleopt, (347, 480))
        opt = pygame.image.load('buttons\\arrowBlue_right.png')
        msg_to_screen("Fight", white, 800, 495, 25)
        msg_to_screen("Dragon", white, 800, 525, 25)
        msg_to_screen("Bag", white, 900, 495, 25)
        msg_to_screen("Run", white, 900, 525, 25)
        game.blit(opt, (optx, opty))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if optx == 775:
                        if opty == 495:
                            opty = 525
                        elif opty == 525:
                            optx = 875
                            opty = 495
                    elif optx == 875 and opty == 495:
                        opty = 525
                    else:
                        optx+=0
                        opty+=0
                elif event.key == pygame.K_UP:
                    if optx == 775:
                        opty = 495
                    elif optx == 875:
                        if opty == 495:
                            optx = 775
                            opty = 525
                        elif opty == 525:
                            opty = 495
                    else:
                        opty+=0
                        optx+=0
                elif event.key == pygame.K_RETURN:
                    if optx == 775:
                        if opty == 495:
                            #fight later
                            print(" ")
                        elif opty == 525:
                            # dragons later
                            print(" ")
                    if optx == 875:
                        if opty == 495:
                            #bag now
                            bag_items = True
                        elif opty == 525:
                            #run now
                            game.blit(battleopt, (347, 480))
                            msg_to_screen("You ran away safely", white, 400, 495, 25)
                            pygame.display.update()
                            pygame.time.delay(1000)
                            battle = False
        if bag_items == True:
            print(itemno)
            game.blit(battleopt, (347, 480))
            pygame.draw.rect(game, (50, 50, 50), [400, 495, 50, 50])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    itemno-=1
                    if itemno <= -1:
                        itemno = 0
                    else:
                        itemno+=0
                elif event.key == pygame.K_RIGHT:
                    itemno+=1
                    if itemno >= 6:
                        itemno = 5
                    else:
                        itemno+=0
                elif event.key == pygame.K_ESCAPE:
                    bag_items = False
                    itemno = 0
                else:
                    itemno+=0
            game.blit(bagitem[itemno], (400, 495))
            pygame.time.delay(100)
        pygame.display.update()

def fight(x, y, area):
    global your_dragon
    global dl
    #0 = xsmall   1 = xbig   2 = ysmall   3 = y big
    if x>=area[0] and x<=area[1] and y>=area[2] and y<=area[3]:
        battlechance = random.randrange(0, 10)
        if battlechance == 1:
            Battle()


def gameloop():
    area = [0, 0, 0, 0]
    global dl
    items = False
    IDstart = False
    moneystart = False
    x = 480
    y = 512
    global bg
    global gamequit
    global mapno
    global player
    global rank
    global money_count
    while not gamequit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamequit = True
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(50)


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
                            y = 576
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

                #Map2 movements

                if mapno == 2:
                    if event.key == pygame.K_LEFT:
                        player = pygame.image.load('player_14.png')
                        if x == 0:
                            x+=0
                        else:
                            x += -32
                        fight(x, y, [0, 1280, 0, 320])
                        
                    elif event.key == pygame.K_RIGHT:
                        player = pygame.image.load('player_11.png')
                        if x == 1280:
                            x+=0
                        else:
                            x += 32
                        fight(x, y, [0, 1280, 0, 320])
                        
                    elif event.key == pygame.K_UP:
                        player = pygame.image.load('player_02.png')
                        if y == 0:
                            y+=0
                        else:
                            y += -32
                        fight(x, y, [0, 1280, 0, 320])
                            
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
                        fight(x, y, [0, 1280, 0, 320])
                        
                    
                #Map3 Movements
                            
                if mapno == 3:
                    if event.key == pygame.K_LEFT:
                        
                        player = pygame.image.load('player_14.png')
                        if x == 0:
                            x+=0
                        elif y == 0:
                            if x == 224 or x == 288 or x == 352:
                                x+=0
                            else:
                                x+=-32
                        elif x == 352 and y <= 448 and y >= 224:
                            x+=0
                        elif x == 544 and y == 576:
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
                                x = 576
                                y = 64
                                mapno = 5
                            elif y == 512:
                                x+=0
                            elif y == 576:
                                x+=0
                            elif y == 32:
                                x+=0
                            else:
                                x+=32
                        elif x == 480 and y == 576:
                            x+=0
                        elif x == 224 and y <= 448 and y >= 224:
                            x+=0
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
                        elif x == 576 and y== 544:
                            y+=0
                        elif x == 576 and y == 96 or x == 544 and y == 96:
                            y+=0
                        elif y == 480 and x >= 256 and x <= 320:
                            y+=0
                        elif y == 32:
                            if x == 192 or x == 256 or x == 320:
                                y+=0
                            else:
                                y+=-32
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
                        elif x == 576 and y == 544:
                            y+=0
                        elif x == 544 and y == 32:
                            y+=0
                        elif x == 576 and y == 480:
                            y+=0
                        elif y == 192 and  x >= 256 and x <= 320:
                            y+=0
                        else:
                            y += 32


                        #Map4 Movements

                        
                if mapno == 4:
                    if event.key == pygame.K_LEFT:
                        
                        player = pygame.image.load('player_14.png')
                        if x == 0:
                            x+=0
                        else:
                            x += -32
                        
                    elif event.key == pygame.K_RIGHT:
                        
                        player = pygame.image.load('player_11.png')
                        if x == 256:
                            x+=0
                        else:
                            x += 32
                        
                    elif event.key == pygame.K_UP:
                        
                        player = pygame.image.load('player_02.png')
                        if y == 160:
                            y+=0
                        else:
                            y += -32
                            
                    elif event.key == pygame.K_DOWN:
                        
                        player = pygame.image.load('player_23.png')
                        if y == 576:
                            bg = pygame.image.load('map1.png')
                            bg = pygame.transform.scale(bg, (1344, 768))
                            x = 128
                            y = 480
                            mapno = 1
                        else:
                            y += 32

                        #Map5 Movements


                if mapno == 5:
                    if event.key == pygame.K_LEFT:
                        
                        player = pygame.image.load('player_14.png')
                        if x == 544:
                            if y == 64:
                                bg = pygame.image.load('map3.png')
                                bg = pygame.transform.scale(bg, (640, 640))
                                x = 544
                                y = 64
                                mapno = 3
                            elif y == 32:
                                x+=0
                            else:
                                x+=-32
                        elif x == 0:
                            x+=0
                        else:
                            x+=-32
                    elif event.key == pygame.K_RIGHT:
                        
                        player = pygame.image.load('player_11.png')
                        if x == 576:
                            x+=0
                        elif x == 448 and y==32 or y==64 and x == 448:
                            x+=0
                        else:
                            x+=32
                    elif event.key == pygame.K_UP:
                        
                        player = pygame.image.load('player_02.png')
                        if y == 0:
                            y+=0
                        elif x>=480 and x <= 544 and y == 96:
                            y+=0
                        else:
                            y+=-32
                    elif event.key == pygame.K_DOWN:
                        
                        player = pygame.image.load('player_23.png')
                        if y == 576:
                            y+=0
                        if x >=480 and x<=544 and y == 0:
                            y+=0
                        else:
                            y+=32

                if event.key == pygame.K_i:
                    if items==False:
                        items = True
                    elif items==True:
                        items = False
                        
        pygame.mouse.set_visible(False)
        cursor = pygame.image.load('buttons\\cursorGauntlet_grey.png')
        (X, Y) = pygame.mouse.get_pos()
        #print(x, y)
        game.fill(black)
        game.blit(bg, (0, 0))
        game.blit(player, (x, y))
        game.blit(cursor, (X, Y))





        if items== True:      


            inventory_panel = pygame.image.load('buttons\\panelInset_blue.png')
            inventory_panel = pygame.transform.scale(inventory_panel, (600, 400))
            inventory_x = (round(winw/2)-300)
            inventory_y = (round(winh/2)-200) + 50
            game.blit(inventory_panel,(inventory_x, inventory_y-50))
            
            # original items
            pen = pygame.image.load('items\\genericItem_color_025.png')
            pen = pygame.transform.scale(pen, (50, 50))
            game.blit(pen, ((round(winw/2)-300) +50, inventory_y))
            
            notes = pygame.image.load('items\\genericItem_color_038.png')
            notes = pygame.transform.scale(notes, (50, 50))
            game.blit(notes, ((round(winw/2)-300) +150, inventory_y))
            
            camera = pygame.image.load('items\\genericItem_color_045.png')
            camera = pygame.transform.scale(camera, (50, 50))
            game.blit(camera, ((round(winw/2)-300) +250, inventory_y))
            
            phone = pygame.image.load('items\\genericItem_color_067.png')
            phone = pygame.transform.scale(phone, (50, 50))
            game.blit(phone, ((round(winw/2)-300) +350, inventory_y))
            
            healing = pygame.image.load('items\\genericItem_color_102.png')
            healing = pygame.transform.scale(healing, (50, 50))
            game.blit(healing, ((round(winw/2)-300) +450, inventory_y))
            
            ID = pygame.image.load('items\\genericItem_color_150.png')
            ID = pygame.transform.scale(ID, (50, 50))
            game.blit(ID, ((round(winw/2)-300) +550, inventory_y))
            
            money = pygame.image.load('items\\genericItem_color_157.png')
            money = pygame.transform.scale(money, (50, 50))
            game.blit(money, ((round(winw/2)-300) +50, inventory_y + 100))
            
            compass = pygame.image.load('items\\genericItem_color_162.png')
            compass = pygame.transform.scale(compass, (50, 50))
            game.blit(compass, ((round(winw/2)-300) +150, inventory_y+ 100))
            
            trap = pygame.image.load('items\\genericItem_color_105.png')
            trap = pygame.transform.scale(trap, (50, 50))
            game.blit(trap, ((round(winw/2)-300) +250, inventory_y+ 100))

            knife = pygame.image.load('items\\genericItem_color_134.png')
            knife = pygame.transform.scale(knife, (50, 50))
            game.blit(knife, ((round(winw/2)-300) +350, inventory_y+ 100))

            key = pygame.image.load('items\\genericItem_color_155.png')
            key = pygame.transform.scale(key, (50, 50))
            game.blit(key, ((round(winw/2)-300) +450, inventory_y+ 100))

            injection = pygame.image.load('items\\genericItem_color_093.png')
            injection = pygame.transform.scale(injection, (50, 50))
            game.blit(injection, ((round(winw/2)-300) +550, inventory_y+ 100))

            hammer = pygame.image.load('items\\genericItem_color_023.png')
            hammer = pygame.transform.scale(hammer, (50, 50))
            game.blit(hammer, ((round(winw/2)-300) +50, inventory_y+ 200))

            saw = pygame.image.load('items\\genericItem_color_016.png')
            saw = pygame.transform.scale(saw, (50, 50))
            game.blit(saw, ((round(winw/2)-300) +150, inventory_y+ 200))

            online = pygame.image.load('items\\genericItem_color_049.png')
            online = pygame.transform.scale(online, (50, 50))
            game.blit(online, ((round(winw/2)-300) +250, inventory_y+ 200))

            pendrive = pygame.image.load('items\\genericItem_color_073.png')
            pendrive = pygame.transform.scale(pendrive, (50, 50))
            game.blit(pendrive, ((round(winw/2)-300) +350, inventory_y+ 200))

            pill1 = pygame.image.load('items\\genericItem_color_089.png')
            pill1 = pygame.transform.scale(pill1, (50, 50))
            game.blit(pill1, ((round(winw/2)-300) +450, inventory_y+ 200))

            pill2 = pygame.image.load('items\\genericItem_color_090.png')
            pill2 = pygame.transform.scale(pill2, (50, 50))
            game.blit(pill2, ((round(winw/2)-300) +550, inventory_y+ 200))

            
            game.blit(cursor, (X, Y))
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        if items==False:
                            items = True
                        elif items==True:
                            items = False
                            IDstart = False
                            moneystart = False
                            
            if X>=372+550 and X <= 372+600 and Y >= inventory_y and Y <= inventory_y+50 and pygame.mouse.get_pressed() == (1, 0, 0):
                IDstart =True
                print("ID")
                items = False
                pygame.time.delay(500)
                game.blit(cursor, (X, Y))
                pygame.display.update()


            
            if X>=372+50 and X <= 372+100 and Y >= inventory_y+100 and Y <= inventory_y+150 and pygame.mouse.get_pressed() == (1, 0, 0):
                moneystart =True
                print("money")
                items = False
                pygame.time.delay(500)
                game.blit(cursor, (X, Y))
                pygame.display.update()
            

        if IDstart == True:
            pygame.draw.rect(game, white, [inventory_x, inventory_y-50, 600, 400])
            pygame.draw.rect(game, red, [inventory_x+10, inventory_y - 40, 130, 130])
            profilepic = pygame.image.load('player_23.png')
            profilepic = pygame.transform.scale(profilepic, (100, 100))
            game.blit(profilepic, (inventory_x+25, inventory_y - 25))
            pygame.draw.rect(game, (200, 200, 200), [inventory_x+150, inventory_y-40, 440, 30])
            msg_to_screen(rank, black, inventory_x+160, inventory_y-35, 25)

                
            
            game.blit(cursor, (X, Y))
            pygame.display.update()
        if moneystart == True:
            pygame.draw.rect(game, white, [round((winw/2)-150), round((winh/2)-15), 300, 30])
            msg_to_screen(str(money_count), black, round(winw/2-140), round(winh/2-10), 25)
            game.blit(cursor, (X, Y))
            pygame.display.update()
            
        pygame.display.update()
        clock.tick(30)
        

    pygame.quit()
    quit

menu()
#Start()
#gameloop()
    
