import os
import csv
import inspect
import random
import pygame
pygame.init()

winw = 1344
winh = 768
bgcolor = 0

x = 480
y = 512
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
dragon_health = 1000
original_dragon_health = dragon_health
healing_count = 0
dragon_fight = original_dragon_health/10
dragon_healthbar_length = 200
poison_count = 0
bg2 = "nothing"
knife_get = False
knife_giver = "nothing"

knife_count = False

mission1 = False
knife_count = False

#Only for Testing

#Only for Testing

# Job description

# Not Work in Progress
######     Movement de map 8 (teleportation from platforms to platforms)     ###### 

# Job description


Guard_Yellow = pygame.image.load('dragons\\Yellow 5.png')
Guard_Yellow = pygame.transform.scale(Guard_Yellow, (64, 64))
mission1_dragons = 4


def menu():
    global your_dragon
    your_dragon_color1 = (0, 0, 0)
    your_dragon_color2 = (0, 0, 0)
    your_dragon_color3 = (0, 0, 0)
    your_dragon_color4 = (0, 0, 0)
    your_dragon_color5 = (0, 0, 0)
    menubg = pygame.image.load('Dragons_wallpaper.jpg')
    menubg = pygame.transform.scale(menubg, (1344, 768))
    opt1 = pygame.image.load('dragons\\Black 4.png')
    opt1 = pygame.transform.scale(opt1, (200, 200))
    opt2 = pygame.image.load('dragons\\Blue 3.png')
    opt2 = pygame.transform.scale(opt2, (200, 200))
    opt3 = pygame.image.load('dragons\\Red 4.png')
    opt3 = pygame.transform.scale(opt3, (200, 200))
    opt4 = pygame.image.load('dragons\\Yellow 2.png')
    opt4 = pygame.transform.scale(opt4, (200, 200))
    opt5 = pygame.image.load('dragons\\Green 1.png')
    opt5 = pygame.transform.scale(opt5, (200, 200))
    game.blit(menubg, (0, 0))
    your_dragon_ = 'nothing'
    i = 0
    while your_dragon_ == 'nothing':
        pygame.draw.rect(game, your_dragon_color1, [winw//5-200, 500, 200, 200])
        game.blit(opt1, (winw//5-200, 500))
        pygame.draw.rect(game, your_dragon_color2, [winw//5*2-200, 500, 200, 200])
        game.blit(opt2, (winw//5*2-200, 500))
        pygame.draw.rect(game, your_dragon_color3, [winw//5*3-200, 500, 200, 200])
        game.blit(opt3, (winw//5*3-200, 500))
        pygame.draw.rect(game, your_dragon_color4, [winw//5*4-200, 500, 200, 200])
        game.blit(opt4, (winw//5*4-200, 500))
        pygame.draw.rect(game, your_dragon_color5, [winw-200, 500, 200, 200])
        game.blit(opt5, (winw-200, 500))
        if i !=255:
            msg_to_screen("Number keys to Choose:", (i, i, i), 400, 100, 50)
            i+=1
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    your_dragon_color1 = (255, 255, 255)
                    your_dragon_color2 = (0, 0, 0)
                    your_dragon_color3 = (0, 0, 0)
                    your_dragon_color4 = (0, 0, 0)
                    your_dragon_color5 = (0, 0, 0)
                    your_dragon = pygame.image.load('dragons\\Black 4.png')
                    
                elif event.key == pygame.K_2:
                    your_dragon_color1 = (0, 0, 0)
                    your_dragon_color2 = (255, 255, 255)
                    your_dragon_color3 = (0, 0, 0)
                    your_dragon_color4 = (0, 0, 0)
                    your_dragon_color5 = (0, 0, 0)
                    your_dragon = pygame.image.load('dragons\\Blue 3.png')
                    
                elif event.key == pygame.K_3:
                    your_dragon_color1 = (0, 0, 0)
                    your_dragon_color2 = (0, 0, 0)
                    your_dragon_color3 = (255, 255, 255)
                    your_dragon_color4 = (0, 0, 0)
                    your_dragon_color5 = (0, 0, 0)
                    your_dragon = pygame.image.load('dragons\\Red 4.png')
                    
                elif event.key == pygame.K_4:
                    your_dragon_color1 = (0, 0, 0)
                    your_dragon_color2 = (0, 0, 0)
                    your_dragon_color3 = (0, 0, 0)
                    your_dragon_color4 = (255, 255, 255)
                    your_dragon_color5 = (0, 0, 0)
                    your_dragon = pygame.image.load('dragons\\Yellow 2.png')
                    
                elif event.key == pygame.K_5:
                    your_dragon_color1 = (0, 0, 0)
                    your_dragon_color2 = (0, 0, 0)
                    your_dragon_color3 = (0, 0, 0)
                    your_dragon_color4 = (0, 0, 0)
                    your_dragon_color5 = (255, 255, 255)
                    your_dragon = pygame.image.load('dragons\\Green 1.png')

                elif event.key == pygame.K_RETURN:
                    if your_dragon == False:
                        your_dragon = False
                    else:
                        your_dragon = pygame.transform.scale(your_dragon, (200, 200))
                        your_dragon_ = 'LOL'
                
        pygame.display.update()
    i = 0
    gameloop()
                
            
            

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
    print ("hello, this is line number"+ str(lineno())+__name__ )


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
    global x
    global y
    global knife_giver
    global bg2
    global mission1_dragons
    global mission1
    global dragon_healthbar_length
    global healing_count
    global poison_count
    global your_dragon
    global dragon_health
    global original_dragon_health
    global mapno
    global knife_count
    global knife_get
    global player
    
    if mapno == 2:
        battle_num = random.randrange(1, 21)
        
    elif mapno == 6 and knife_get == False:
        battle_num = random.randrange(13, 17)

    elif mapno == 6 and knife_get == True:
        battle_num = random.randrange(0, 5)
        if battle_num == 0:
            battle_num = 3
        elif battle_num == 1:
            battle_num = 7
        elif battle_num == 2:
            battle_num = 11
        elif battle_num == 3:
            battle_num = 15
        elif battle_num == 4:
            battle_num = 19
                
        
        
    if battle_num == 1:
        battle_dragon = pygame.image.load('dragons\\Blue 1.png')
        opponent_health = 750
        
    elif battle_num == 2:
        battle_dragon = pygame.image.load('dragons\\Blue 2.png')
        opponent_health = 1000
        
    elif battle_num == 3:
        battle_dragon = pygame.image.load('dragons\\Blue 3.png')
        opponent_health = 1250
        
    elif battle_num == 4:
        battle_dragon = pygame.image.load('dragons\\Blue 4.png')
        opponent_health = 1500
        
    elif battle_num == 5:
        battle_dragon = pygame.image.load('dragons\\Red 1.png')
        opponent_health = 750
        
    elif battle_num == 6:
        battle_dragon = pygame.image.load('dragons\\Red 2.png')
        opponent_health = 1000
        
    elif battle_num == 7:
        battle_dragon = pygame.image.load('dragons\\Red 3.png')
        opponent_health = 1250
        
    elif battle_num == 8:
        battle_dragon = pygame.image.load('dragons\\Red 4.png')
        opponent_health = 1500
        
    elif battle_num == 9:
        battle_dragon = pygame.image.load('dragons\\Green 1.png')
        opponent_health = 750
        
    elif battle_num == 10:
        battle_dragon = pygame.image.load('dragons\\Green 2.png')
        opponent_health = 1000
        
    elif battle_num == 11:
        battle_dragon = pygame.image.load('dragons\\Green 3.png')
        opponent_health = 1250
        
    elif battle_num == 12:
        battle_dragon = pygame.image.load('dragons\\Green 4.png')
        opponent_health = 1500
        
    elif battle_num == 13:
        battle_dragon = pygame.image.load('dragons\\Yellow 1.png')
        opponent_health = 750
        
    elif battle_num == 14:
        battle_dragon = pygame.image.load('dragons\\Yellow 2.png')
        opponent_health = 1000
        
    elif battle_num == 15:
        battle_dragon = pygame.image.load('dragons\\Yellow 3.png')
        opponent_health = 1250
        
    elif battle_num == 16:
        battle_dragon = pygame.image.load('dragons\\Yellow 4.png')
        opponent_health = 1500
        
    elif battle_num == 17:
        battle_dragon = pygame.image.load('dragons\\Black 1.png')
        opponent_health = 750
        
    elif battle_num == 18:
        battle_dragon = pygame.image.load('dragons\\Black 2.png')
        opponent_health = 1000
        
    elif battle_num == 19:
        battle_dragon = pygame.image.load('dragons\\Black 3.png')
        opponent_health = 1250
        
    elif battle_num == 20:
        battle_dragon = pygame.image.load('dragons\\Black 4.png')
        opponent_health = 1500
    original_opponent_health = opponent_health   
    battle_dragon = pygame.transform.scale(battle_dragon, (200, 200))
        
    pen = pygame.image.load('items\\genericItem_color_025.png')
    pen = pygame.transform.scale(pen, (50, 50))
    camera = pygame.image.load('items\\genericItem_color_045.png')
    camera = pygame.transform.scale(camera, (50, 50))
    healing = pygame.image.load('items\\genericItem_color_102.png')
    healing = pygame.transform.scale(healing, (50, 50))
    trap = pygame.image.load('items\\genericItem_color_105.png')
    trap = pygame.transform.scale(trap, (50, 50))


    opponent_healthbar_length = 200
    battle = True
    optx = 775
    opty = 495
    bag_items = False
    itemno = 0
    bagitem = [pen, camera, healing, trap]
    
    while battle == True:
        game.blit(bg, (0, 0))
        if bg2 == "nothing":
            bg2 == "nothing"
        else:
            game.blit(bg2, (0, 0))
        if knife_giver == "nothing":
            knife_giver == "nothing"
        else:
            game.blit(knife_giver, (64, 0))
        game.blit(player, (x, y))
        pygame.draw.rect(game, white, [336, 192, 672, 380])
        game.blit(battle_dragon, (803, 197))
        game.blit(your_dragon, (341, 197))
        battleopt = pygame.image.load('buttons\\panelInset_brown.png')
        battleopt = pygame.transform.scale(battleopt, (650, 80))
        game.blit(battleopt, (347, 480))
        opt = pygame.image.load('buttons\\arrowBlue_right.png')
        msg_to_screen("Fight", white, 800, 495, 25)
        msg_to_screen("Dragon", white, 800, 525, 25)
        msg_to_screen("Bag", white, 900, 495, 25)
        msg_to_screen("Run", white, 900, 525, 25)
        game.blit(opt, (optx, opty))
        pygame.draw.rect(game, (100, 100, 100), [341, 450, 200, 20])
        pygame.draw.rect(game, (100, 100, 100), [803, 450, 200, 20])
        pygame.draw.rect(game, (175, 0, 0), [803, 450, opponent_healthbar_length, 20])
        pygame.draw.rect(game, (175, 0, 0), [341, 450, dragon_healthbar_length, 20])    
        msg_to_screen(str(dragon_health), white, 341, 450, 20)
        msg_to_screen(str(opponent_health), white, 803, 450, 20)
        cursor = pygame.image.load('buttons\\cursorGauntlet_grey.png')
        (X, Y) = pygame.mouse.get_pos()
        game.blit(cursor, (X, Y))
        pygame.display.update()
        dragon_health = int(dragon_health)
        opponent_health = int(opponent_health)
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
                            fight_power = random.randrange(1, 4)
                            opponent_health -= fight_power*dragon_fight
                            msg_to_screen("You attacked the opponent Dragon", white, 400, 495, 25)
                            pygame.display.update()
                            pygame.time.delay(1000)
                            game.blit(battleopt, (347, 480))
                            pygame.display.update()
                            if original_opponent_health == 750:
                                opponent_healthbar_length = round(opponent_health/7.5)*2
                            elif original_opponent_health == 1000:
                                opponent_healthbar_length = round(opponent_health/10)*2
                            elif original_opponent_health == 1250:
                                opponent_healthbar_length = round(opponent_health/12.5)*2
                            elif original_opponent_health == 1500:
                                opponent_healthbar_length = round(opponent_health/15)*2
                            else:
                                opponent_healthbar_length+=0
                            fight_power = random.randrange(1, 4)
                            dragon_health-=(original_opponent_health/10)*fight_power
                            msg_to_screen("The opponent dragon attaked you", white, 400, 495, 25)
                            pygame.display.update()
                            pygame.time.delay(1000)
                            game.blit(battleopt, (347, 480))
                            pygame.display.update()
                            dragon_health_bar = round(original_dragon_health/(round(original_dragon_health/10)))
                            dragon_healthbar_length = round(dragon_health/dragon_health_bar)*2
                            if dragon_health <= 0:
                                msg_to_screen("You Lost!!!", white, 400, 495, 25)
                                pygame.display.update()
                                pygame.time.delay(1000)
                                game.blit(battleopt, (347, 480))
                                dragon_health = 0
                                battle = False
                            elif opponent_health <= 0:
                                original_dragon_health+=10
                                msg_to_screen("You Won!!!", white, 400, 495, 25)
                                pygame.display.update()
                                pygame.time.delay(1000)
                                game.blit(battleopt, (347, 480))
                                healing_get = random.randrange(1, 4)
                                if healing_get == 1:
                                    msg_to_screen("You get a first-aid-kit!!!", white, 400, 495, 25)
                                    pygame.display.update()
                                    pygame.time.delay(1000)
                                    healing_count += 1
                                else:
                                    healing_count += 0
                                game.blit(battleopt, (347, 480))
                                poison_get = random.randrange(1, 6)
                                msg_to_screen("You get a Vial of Poison!!!", white, 400, 495, 25)
                                pygame.display.update()
                                pygame.time.delay(1000)
                                poison_count+=1
                                if battle_num == 1 or battle_num == 5 or battle_num == 9 or battle_num == 13 or battle_num == 17:
                                    mission1_dragons-=1

                                if mission1_dragons == 0:
                                    mission1 = True
                                if knife_get == True:
                                    knife_get = False
                                    knife_count = True
                                    msg_to_screen("You Just got a Knife!!!", white, 400, 495, 25)
                                    pygame.display.update()
                                    pygame.time.delay(1000)
                                game.blit(battleopt, (347, 480))
                                battle = False
                            else:
                                battle = True
                            pygame.display.update()
                            
                        elif opty == 525:
                            if battle_num == 1:
                                msg_to_screen("Shadow Wing(small)", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 2:
                                msg_to_screen("Sea Shocker", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 3:
                                msg_to_screen("Deadly Nadder", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 4:
                                msg_to_screen("Blue Death", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 5:
                                msg_to_screen("Fire Terror", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 6:
                                msg_to_screen("Change Wing", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 7:
                                msg_to_screen("Singe Tail", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 8:
                                msg_to_screen("Monstrous Nightmare", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 9:
                                msg_to_screen("Hideous Zippleback", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 10:
                                msg_to_screen("Rumle Horn", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 11:
                                msg_to_screen("Submaripper", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 12:
                                msg_to_screen("Shadow Wing(Big)", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 13:
                                msg_to_screen("Terrible Terror", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 14:
                                msg_to_screen("Gronkle", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 15:
                                msg_to_screen("Fireworm Queen", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 16:
                                msg_to_screen("Deathsong", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 17:
                                msg_to_screen("Night Terror", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 18:
                                msg_to_screen("Cavern Crasher", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 19:
                                msg_to_screen("Eruptodon", white, 400, 495, 25)
                                pygame.display.update()
                                
                            elif battle_num == 20:
                                msg_to_screen("Night Fury", white, 400, 495, 25)
                                pygame.display.update()
                            pygame.time.delay(1000)
                            game.blit(battleopt, (347, 480))
                            pygame.display.update()
                    if optx == 875:
                        if opty == 495:
                            bag_items = True
                            pygame.time.delay(200)
                            pygame.event.clear()
                            while bag_items:
                                cursor = pygame.image.load('buttons\\cursorGauntlet_grey.png')
                                pygame.draw.rect(game, (50, 50, 50), [400, 495, 50, 50])
                                pygame.draw.rect(game, (50, 50, 50), [400, 550, 60, 20])
                                msg_to_screen("Enter-Use", white, 400, 555, 20)
                                game.blit(bagitem[itemno], (400, 495))
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_LEFT:
                                            itemno-=1
                                            if itemno <= -1:
                                                itemno = 0
                                            else:
                                                itemno+=0
                                        elif event.key == pygame.K_RIGHT:
                                            itemno+=1
                                            if itemno >= 4:
                                                itemno = 3
                                            else:
                                                itemno+=0
                                        elif event.key == pygame.K_ESCAPE:
                                            itemno = 0
                                            bag_items = False
                                        elif event.key == pygame.K_RETURN:
                                            if itemno == 0:
                                                msg_to_screen("Notes Made!!", white, 475, 495, 25)
                                                msg_to_screen("(This will affect nothing)", white, 475, 515, 25)
                                                pygame.display.update()
                                                pygame.time.delay(1000)
                                                bag_items = False
                                            elif itemno == 1:
                                                msg_to_screen("It's Original Health is " + str(original_opponent_health) + "!!", white, 475, 495, 25)
                                                pygame.display.update()
                                                pygame.time.delay(1000)
                                                bag_items=False
                                            elif itemno == 2:
                                                if healing_count>=1:
                                                    dragon_health = original_dragon_health
                                                    healing_count-=1
                                                    msg_to_screen("First Aid Kit Used!!!", white, 475, 495, 25)
                                                    pygame.display.update()
                                                    pygame.time.delay(1000)
                                                    game.blit(battleopt, (347, 480))
                                                    game.blit(bg, (0, 0))
                                                    pygame.draw.rect(game, white, [336, 192, 672, 380])
                                                    game.blit(battle_dragon, (803, 197))
                                                    game.blit(your_dragon, (341, 197))
                                                    battleopt = pygame.image.load('buttons\\panelInset_brown.png')
                                                    battleopt = pygame.transform.scale(battleopt, (650, 80))
                                                    game.blit(battleopt, (347, 480))
                                                    opt = pygame.image.load('buttons\\arrowBlue_right.png')
                                                    msg_to_screen("Fight", white, 800, 495, 25)
                                                    msg_to_screen("Dragon", white, 800, 525, 25)
                                                    msg_to_screen("Bag", white, 900, 495, 25)
                                                    msg_to_screen("Run", white, 900, 525, 25)
                                                    game.blit(opt, (optx, opty))
                                                    pygame.draw.rect(game, (100, 100, 100), [341, 450, 200, 20])
                                                    pygame.draw.rect(game, (100, 100, 100), [803, 450, 200, 20])
                                                    pygame.draw.rect(game, (175, 0, 0), [803, 450, opponent_healthbar_length, 20])
                                                    pygame.draw.rect(game, (175, 0, 0), [341, 450, dragon_healthbar_length, 20])
                                                    msg_to_screen(str(dragon_health), white, 341, 450, 20)
                                                    msg_to_screen(str(opponent_health), white, 803, 450, 20)
                                                    cursor = pygame.image.load('buttons\\cursorGauntlet_grey.png')
                                                    (X, Y) = pygame.mouse.get_pos()
                                                    game.blit(cursor, (X, Y))
                                                    pygame.display.update()
                                                    msg_to_screen("Health is Restored!!!", white, 475, 495, 25)
                                                    dragon_healthbar_length = 200
                                                    pygame.draw.rect(game, (175, 0, 0), [341, 450, dragon_healthbar_length, 20])
                                                    msg_to_screen(str(dragon_health), white, 341, 450, 20)
                                                    pygame.display.update()
                                                    pygame.time.delay(1000)
                                                    bag_items=False
                                                elif healing_count == 0:
                                                    msg_to_screen("No First Aid Kit!!!", white, 475, 495, 25)
                                                    pygame.display.update()
                                                    pygame.time.delay(1000)
                                                    bag_items=False
                                            elif itemno == 3:
                                                if poison_count>=1:
                                                    opponent_health -= 250
                                                    poison_count-=1
                                                    msg_to_screen("Poison Used!!!", white, 475, 495, 25)
                                                    if original_opponent_health == 750:
                                                        opponent_healthbar_length = round(opponent_health/7.5)*2
                                                    elif original_opponent_health == 1000:
                                                        opponent_healthbar_length = round(opponent_health/10)*2
                                                    elif original_opponent_health == 1250:
                                                        opponent_healthbar_length = round(opponent_health/12.5)*2
                                                    elif original_opponent_health == 1500:
                                                        opponent_healthbar_length = round(opponent_health/15)*2
                                                    else:
                                                        opponent_healthbar_length+=0
                                                    pygame.display.update()
                                                    pygame.time.delay(1000)
                                                    game.blit(battleopt, (347, 480))
                                                    game.blit(bg, (0, 0))
                                                    pygame.draw.rect(game, white, [336, 192, 672, 380])
                                                    game.blit(battle_dragon, (803, 197))
                                                    game.blit(your_dragon, (341, 197))
                                                    battleopt = pygame.image.load('buttons\\panelInset_brown.png')
                                                    battleopt = pygame.transform.scale(battleopt, (650, 80))
                                                    game.blit(battleopt, (347, 480))
                                                    opt = pygame.image.load('buttons\\arrowBlue_right.png')
                                                    msg_to_screen("Fight", white, 800, 495, 25)
                                                    msg_to_screen("Dragon", white, 800, 525, 25)
                                                    msg_to_screen("Bag", white, 900, 495, 25)
                                                    msg_to_screen("Run", white, 900, 525, 25)
                                                    game.blit(opt, (optx, opty))
                                                    pygame.draw.rect(game, (100, 100, 100), [341, 450, 200, 20])
                                                    pygame.draw.rect(game, (100, 100, 100), [803, 450, 200, 20])
                                                    pygame.draw.rect(game, (175, 0, 0), [803, 450, opponent_healthbar_length, 20])
                                                    pygame.draw.rect(game, (175, 0, 0), [341, 450, dragon_healthbar_length, 20])
                                                    msg_to_screen(str(dragon_health), white, 341, 450, 20)
                                                    msg_to_screen(str(opponent_health), white, 803, 450, 20)
                                                    cursor = pygame.image.load('buttons\\cursorGauntlet_grey.png')
                                                    (X, Y) = pygame.mouse.get_pos()
                                                    game.blit(cursor, (X, Y))
                                                    pygame.display.update()                                                        
                                                    msg_to_screen("Opponent Dragon lost 250 HP!!!", white, 475, 495, 25)
                                                    pygame.display.update()
                                                    pygame.time.delay(1000)
                                                    game.blit(battleopt, (347, 480))
                                                    bag_items=False
                                                    if opponent_health <= 0:
                                                        original_dragon_health+=10
                                                        msg_to_screen("You Won!!!", white, 400, 495, 25)
                                                        pygame.display.update()
                                                        pygame.time.delay(1000)
                                                        game.blit(battleopt, (347, 480))
                                                        healing_get = random.randrange(1, 4)
                                                        if healing_get == 1:
                                                            msg_to_screen("You get a first-aid-kit!!!", white, 400, 495, 25)
                                                            pygame.display.update()
                                                            pygame.time.delay(1000)
                                                            healing_count += 1
                                                        else:
                                                            healing_count += 0
                                                        game.blit(battleopt, (347, 480))
                                                        poison_get = random.randrange(1, 6)
                                                        msg_to_screen("You get a Vial of Poison!!!", white, 400, 495, 25)
                                                        pygame.display.update()
                                                        pygame.time.delay(1000)
                                                        poison_count+=1
                                                        game.blit(battleopt, (347, 480))
                                                        if battle_num == 1 or battle_num == 5 or battle_num == 9 or battle_num == 13 or battle_num == 17:
                                                            mission1_dragons-=1

                                                        if mission1_dragons == 0:
                                                            mission1 = True
                                                        if knife_get == True:
                                                            knife_get = False
                                                            knife_count = True
                                                            msg_to_screen("You Just got a Knife!!!", white, 400, 495, 25)
                                                            pygame.display.update()
                                                            pygame.time.delay(1000)
                                                            game.blit(battleopt, (347, 480))
                                                            battle = False
                                                        else:
                                                            battle = True
                                                        pygame.display.update()
                                                        battle = False
                                                elif poison_count == 0:
                                                    msg_to_screen("No Poison!!!", white, 475, 495, 25)
                                                    pygame.display.update()
                                                    pygame.time.delay(1000)
                                                    bag_items=False

                                                else:
                                                    healing_count+=0
                                            else:
                                                healing_count+=0
                                        else:
                                            itemno+=0
                                        
                                game.blit(bagitem[itemno], (400, 495))
                                pygame.time.delay(100)
                                pygame.display.update()
                        elif opty == 525:
                            game.blit(battleopt, (347, 480))
                            msg_to_screen("You ran away safely", white, 400, 495, 25)
                            pygame.display.update()
                            pygame.time.delay(1000)
                            battle = False
                    pygame.event.clear()
    if healing_count == 0 and dragon_health <= 0:
        dragon_healthbar_length = 0
        battle = False
        player = pygame.image.load('player_23.png')
        dragon_health = 1000
        original_dragon_health = dragon_health
        healing_count = 0
        dragon_healthbar_length = 200
        poison_count = 0




def fight(x, y, area):
    global your_dragon
    global dl
    #0 = xsmall   1 = xbig   2 = ysmall   3 = y big
    if x>=area[0] and x<=area[1] and y>=area[2] and y<=area[3]:
        battlechance = random.randrange(0, 20)
        if battlechance == 1:
            Battle()
            
            

def gameloop():
    global knife_count
    global knife_giver
    global knife_get
    global mission1_part_1
    global mission1
    global mission1_dragons 
    area = [0, 0, 0, 0]
    global dl
    items = False
    IDstart = False
    moneystart = False
    global x
    global y
    global bg
    global bg2
    global gamequit
    global mapno
    global player
    global rank
    global money_count
    mission1_msg = False
    
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
                        if x == 0:
                            if mission1 == False:
                                x+=0
                                mission1_msg = True
                            else:
                                x+=-32
                        elif x == 608 and y <= 448 and y >= 352:
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
                        elif mission1 == True:
                            if x <= 0:
                                bg = pygame.image.load('map6.png')
                                bg = pygame.transform.scale(bg, (1344, 768))
                                x = 1280
                                y = 128
                                mapno = 6
                            else:
                                x+=-32
                        else:
                            x += -32
                        
                    elif event.key == pygame.K_RIGHT:
                        mission1_msg = False
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

                # Map 6 movements
                
                if mapno == 6:
                    if event.key == pygame.K_LEFT:
                        player = pygame.image.load('player_14.png')
                        if x == 0:
                            x+=0
                        elif y == 0 and x == 192:
                            x+=0
                        else:
                            x += -32
                            
                    elif event.key == pygame.K_RIGHT:
                        player = pygame.image.load('player_11.png')
                        if x == 1280:
                            bg = pygame.image.load('map1.png')
                            bg = pygame.transform.scale(bg, (1344, 768))
                            x = 0
                            y = 512
                            mapno = 1
                        else:
                            x += 32
                        
                    elif event.key == pygame.K_UP:
                        player = pygame.image.load('player_02.png')
                        if y == 0:
                            y+=0
                        elif x == 64 and y == 32 and knife_count == True:
                            bg = pygame.image.load('map miniboss 1.png')
                            bg = pygame.transform.scale(bg, (1344, 768))
                            x = 640
                            y = 704
                            mapno = 7
                        elif x == 64 and y == 32 and knife_count == False:
                            y+=0
                            knife_get = True
                            Battle()
                        elif y == 32:
                            if x == 0 or x == 32 or x == 96 or x == 128 or x == 160:
                                y+=0
                            else:
                                y+=-32
                        else:
                            y += -32
                            
                    elif event.key == pygame.K_DOWN:
                        player = pygame.image.load('player_23.png')
                        if y == 704:
                            y+=0
                        else:
                            y += 32
                    fight(x, y, [640, 1280, 0, 64])
                    fight(x, y, [640, 704, 96, 448])
                    fight(x, y, [896, 1280, 224, 704])
                    fight(x, y, [256, 602, 352, 448])
                    fight(x, y, [0, 864, 608, 704])
                    fight(x, y, [0, 64, 96, 576])
                    fight(x, y, [96, 448, 96, 192])

                    #Map 7 movements

                    
                if mapno == 7:
                    if event.key == pygame.K_LEFT:
                        player = pygame.image.load('player_14.png')
                        if x == 0:
                            x+=0
                        elif x == 192 or x == 576 or x == 896 or x == 1280:
                            if y >= 0 and y <= 192:
                                x+=0
                            else:
                                x+=-32
                        else:
                            x += -32
                            
                    elif event.key == pygame.K_RIGHT:
                        player = pygame.image.load('player_11.png')
                        if x == 1280:
                            x+=0
                        elif x == 0 or x == 384 or x == 704 or x == 1088:
                            if y >= 0 and y <= 192:
                                x+=0
                            else:
                                x+=32
                        else:
                            x += 32
                        
                    elif event.key == pygame.K_UP:
                        player = pygame.image.load('player_02.png')
                        if y == 0:
                            y+=0
                        elif y == 224:
                            if x == 32 or x == 416 or x == 736 or x == 1120 or x == 160 or x == 544 or x == 864 or x == 1248:
                                y+=0
                            else:
                                y+=-32
                        elif y == 192:
                            # go to map 8 - Figt Area
                            if x >=32 and x <= 160:
                                bg = pygame.image.load('miniboss Battle map 8 part 1.png')
                                bg = pygame.transform.scale(bg, (1344, 768))
                                x = 640
                                y = 640
                                mapno = 8
                            elif x >=416 and x <= 544 or x >=736 and x <= 864 or x >=1120 and x <= 1248:
                                y+=0                            
                            else:
                                y+=-32
                        else:
                            y += -32
                            
                    elif event.key == pygame.K_DOWN:
                        player = pygame.image.load('player_23.png')
                        if y == 704:
                            bg = pygame.image.load('map6.png')
                            bg = pygame.transform.scale(bg, (1344, 768))
                            x = 64
                            y = 32
                            mapno = 6
                        else:
                            y += 32

                # Map 8 Movements

                if mapno == 8:
                    if event.key == pygame.K_LEFT:
                        
                        player = pygame.image.load('player_14.png')
                        if x == 640 and y == 576:
                            x = 64
                        elif x == 384 and y == 448:
                            x = 64
                        elif x == 1088 and y == 640:
                            x = 384
                        
                        else:
                            x += -64
                        
                    elif event.key == pygame.K_RIGHT:
                        
                        player = pygame.image.load('player_11.png')
                        if x == 1280:
                            x+=0
                        elif x == 64 and y == 576:
                            x = 640
                        elif x == 64 and y == 448:
                            x = 384
                        elif x == 384 and y == 640:
                            x = 1088
                        else:
                            x += 64
                        
                    elif event.key == pygame.K_UP:
                        
                        player = pygame.image.load('player_02.png')
                        if y == 0:
                            y+=0
                        elif x == 64 and y == 576:
                            y = 448
                        else:
                            y += -64
                            
                    elif event.key == pygame.K_DOWN:
                        player = pygame.image.load('player_23.png')
                        if x == 640 and y == 576:
                            bg = pygame.image.load('map miniboss 1.png')
                            bg = pygame.transform.scale(bg, (1344, 768))
                            x = 96
                            y = 192
                            mapno = 7
                        elif x == 64 and y == 448:
                            y = 576
                        else:
                            y += 64
                    
                if event.key == pygame.K_i:
                    if items==False:
                        items = True
                    elif items==True:
                        items = False


                     
        pygame.mouse.set_visible(False)
        cursor = pygame.image.load('buttons\\cursorGauntlet_grey.png')
        (X, Y) = pygame.mouse.get_pos()
        print(x, y)
        game.fill(black)
        game.blit(bg, (0, 0))
        
        if mapno == 6 and knife_count == False:
            game.blit(player, (x, y))
            bg2 = pygame.image.load('map 6 knife.png')
            bg2 = pygame.transform.scale(bg2, (1344, 768))
            game.blit(bg2, (0, 0))
            knife_giver = pygame.image.load('characters\\character_femaleAdventurer_idle.png')
            knife_giver = pygame.transform.scale(knife_giver, (64, 64))
            game.blit(knife_giver, (64, 0))
            pygame.display.update
        elif mapno == 7:
            game.blit(player, (x, y))
            bg2 = pygame.image.load('map miniboss 1 top.png')
            bg2 = pygame.transform.scale(bg2, (1344, 768))
            game.blit(bg2, (0, 0))
            pygame.display.update
        else:
            bg2 = "nothing"
            knife_giver = "nothing"
            game.blit(player, (x, y))

            
        
        if mapno == 1:
            if mission1 == False:
                game.blit(Guard_Yellow, (0, 416))
            if mission1_msg == True:
                pygame.draw.rect(game, black, [64, 416, 500, 40])
                if mission1_dragons >= 1: 
                    msg_to_screen(("kill " + str(mission1_dragons) + " dragons of 750 HP"), white, 64, 416, 50)
                mission1_dragons = int(mission1_dragons)
                pygame.display.update
        
        game.blit(cursor, (X, Y))





        if items== True:      


            inventory_panel = pygame.image.load('buttons\\panelInset_blue.png')
            inventory_panel = pygame.transform.scale(inventory_panel, (600, 400))
            inventory_x = (round(winw/2)-300)
            inventory_y = (round(winh/2)-200) + 50
            game.blit(inventory_panel,(inventory_x, inventory_y-50))
            
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
            msg_to_screen(str(healing_count), black, (round(winw/2)-300) +455, (inventory_y), 75)
            int(healing_count)
            
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
            msg_to_screen(str(poison_count), black, (round(winw/2)-300) +250, (inventory_y+ 100), 75)
            int(poison_count)

            knife = pygame.image.load('items\\genericItem_color_134.png')
            knife = pygame.transform.scale(knife, (50, 50))
            game.blit(knife, ((round(winw/2)-300) +350, inventory_y+ 100))
            if knife_count == True:
                msg_to_screen("1", black, (round(winw/2)-300) +350, (inventory_y+ 100), 75)
            else:
                msg_to_screen("0", black, (round(winw/2)-300) +350, (inventory_y+ 100), 75)
                
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
                items = False
                pygame.time.delay(500)
                game.blit(cursor, (X, Y))
                pygame.display.update()


            
            if X>=372+50 and X <= 372+100 and Y >= inventory_y+100 and Y <= inventory_y+150 and pygame.mouse.get_pressed() == (1, 0, 0):
                moneystart =True
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

    

menu()
