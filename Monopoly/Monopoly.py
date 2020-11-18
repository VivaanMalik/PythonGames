#GivingPlayersValue
#TypesOfFakePeople@Jordindian
#XD
#LOL
global Player_no
import random
Player1name = input(print("Enter name of Player 1"))
Player2name = input(print("Enter name of Player 2"))
Player3name = input(print("Enter name of Player 3"))
Player4name = input(print("Enter name of Player 4"))


Players = [{ "name":Player1name, "current_balance":15000, "position":0, "jail":False, "round":0, "go_collections":0}, 
           { "name":Player2name, "current_balance":15000, "position":0, "jail":False, "round":0, "go_collections":0},
           { "name":Player3name, "current_balance":15000, "position":0, "jail":False, "round":0, "go_collections":0},
           { "name":Player4name, "current_balance":15000, "position":0, "jail":False, "round":0, "go_collections":0}]
Player1 = Players[0]
Player2 = Players[1]
Player3 = Players[2]
Player4 = Players[3]
     
def Chance(): 
    Chance_cards=[{"text":"Another player files a court case against you. Choose which player and pay them 500."},
                  {"text":"Advance to GO."},
                  {"text":"Advance to the nearest station space. If unowned, you may buy it from the bank. If owned, pay the owner twice the rental to which they are otherwise entitled. If you pass GO collect 2000."},
                  {"text":"Advance to the nearest station space. If unowned, you may buy it from the bank. If owned, pay the owner twice the rental to which they are otherwise entitled. If you pass GO collect 2000."},
                  {"text":"Advance to the Utility. If unowned, you may buy it from the bank. If owned, throw dice and pay owner a total 10,000 times amount thrown. If you pass GO collect 2000."},
                  {"text":"Summoned for jury duty. Go back 3 spaces."},
                  {"text":"Accept the position of CEO ataa a high-powered investment banking firm. Collect a signing bonus of 1500."},
                  {"text":"Convicted of Identity Theft. Go to Jail. Do not pass GO, do not collect 2000."},
                  {"text":"Get a tax break for driving a hybrid. Collect 500."},
                  {"text":"Splash out on a trip to Pall Mall. If yoou pass GO, collect 2000."},
                  {"text":"Ride first-class to King Cross Station. If you pass GO, collect 2000."},
                  {"text":"You are acquitted. GET OUT OF JAIL FREE. This may be kept until needed or traded."},
                  {"text":"Make a donation for disaster relief. Pay 150."},
                  {"text":"Your city does a tax revaluation. Pay 250 for each house and 1000 for each hotel you own."},
                  {"text":"Jump on a plane to Trafalgar Square. if you pass GO, collect 2000."},
                  {"text":"Take a helicopter ride to Mayfair."}
        ]
    #card_no=random.randrange(1,17)-1
    card_no=0
    print(Chance_cards[card_no]["text"])
    if card_no+1 ==1:
        player_output = input(print("type the player number from 1 to 4"))
        while player_output==Player_no+1:
            player_output = input(print("type the player number from 1 to 4"))
        Players[Player_no]["current_balance"]-=500
        Players[player_output-1]["current_balance"]+=500        
        
        
            
        

Properties = [{ "name":"Old Kent Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":600, "base_rent":20, "mortgage_value":300, "unmortgage_value":330, "house1rent":100, "house2rent":300, "house3rent":900, "house4rent":1600, "Hotelrent":2500, "colorset":40, "house price":500},
              { "name":"Whitechapel Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":600, "base_rent":40, "mortgage_value":300, "unmortgage_value":330, "house1rent":200, "house2rent":600, "house3rent":1800, "house4rent":3200, "Hotelrent":4500, "colorset":80, "house price":500},
              { "name":"The Angel Islington", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1000, "base_rent":60, "mortgage_value":500, "unmortgage_value":550, "house1rent":300, "house2rent":900, "house3rent":2700, "house4rent":4000, "Hotelrent":5500, "colorset":120,  "house price":500},
              { "name":"Euston Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1000, "base_rent":60, "mortgage_value":500, "unmortgage_value":550, "house1rent":300, "house2rent":900, "house3rent":2700, "house4rent":4000, "Hotelrent":5500, "colorset":120,  "house price":500},
              { "name":"Pentonville Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1200, "base_rent":80, "mortgage_value":600, "unmortgage_value":660, "house1rent":400, "house2rent":1000, "house3rent":3000, "house4rent":4500, "Hotelrent":6000, "colorset":160, "house price":500},
              { "name":"Pall Mall", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1400, "base_rent":100, "mortgage_value":700, "unmortgage_value":770, "house1rent":500, "house2rent":1500, "house3rent":4500, "house4rent":6250, "Hotelrent":7500, "colorset":200, "house price":1000},
              { "name":"White Hall", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1400, "base_rent":100, "mortgage_value":700, "unmortgage_value":770, "house1rent":500, "house2rent":1500, "house3rent":4500, "house4rent":6250, "Hotelrent":7500, "colorset":200, "house price":1000},
              { "name":"Northumberland Avenue", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1600, "base_rent":120, "mortgage_value":800, "unmortgage_value":880, "house1rent":600, "house2rent":1800, "house3rent":5000, "house4rent":7000, "Hotelrent":9000, "colorset":240, "house price":1000},
              { "name":"Bow Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1800, "base_rent":140, "mortgage_value":900, "unmortgage_value":990, "house1rent":700, "house2rent":2000, "house3rent":5500, "house4rent":7500, "Hotelrent":9500, "colorset":280, "house price":1000},
              { "name":"Marlborough Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1800, "base_rent":140, "mortgage_value":900, "unmortgage_value":990, "house1rent":700, "house2rent":2000, "house3rent":5500, "house4rent":7500, "Hotelrent":9500, "colorset":280, "house price":1000},
              { "name":"Vine Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2000, "base_rent":160, "mortgage_value":1000, "unmortgage_value":1100, "house1rent":800, "house2rent":2200, "house3rent":6000, "house4rent":8000, "Hotelrent":10000, "colorset":320, "house price":1000},
              { "name":"Strand", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2200, "base_rent":180, "mortgage_value":1100, "unmortgage_value":1210, "house1rent":900, "house2rent":2500, "house3rent":7000, "house4rent":8750, "Hotelrent":10500, "colorset":360, "house price":1500},
              { "name":"Fleet Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2200, "base_rent":180, "mortgage_value":1100, "unmortgage_value":1210, "house1rent":900, "house2rent":2500, "house3rent":7000, "house4rent":8750, "Hotelrent":10500, "colorset":360, "house price":1500},
              { "name":"Trafalgar Square", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2400, "base_rent":200, "mortgage_value":1200, "unmortgage_value":1320, "house1rent":1000, "house2rent":3000, "house3rent":7500, "house4rent":9250, "Hotelrent":11000, "colorset":400, "house price":1500},
              { "name":"Leicester Square", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2600, "base_rent":220, "mortgage_value":1300, "unmortgage_value":1430, "house1rent":1100, "house2rent":3300, "house3rent":8000, "house4rent":9750, "Hotelrent":11500, "colorset":440, "house price":1500},
              { "name":"Coventry Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2600, "base_rent":220, "mortgage_value":1300, "unmortgage_value":1430, "house1rent":1100, "house2rent":3300, "house3rent":8000, "house4rent":9750, "Hotelrent":11500, "colorset":440, "house price":1500},
              { "name":"Piccadilly", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2800, "base_rent":240, "mortgage_value":1400, "unmortgage_value":1540, "house1rent":1200, "house2rent":3600, "house3rent":8500, "house4rent":10250, "Hotelrent":12000, "colorset":480, "house price":1500},
              { "name":"Regent Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3000, "base_rent":260, "mortgage_value":1500, "unmortgage_value":1650, "house1rent":1300, "house2rent":3900, "house3rent":9000, "house4rent":11000, "Hotelrent":12750, "colorset":520, "house price":2000},
              { "name":"Oxford Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3000, "base_rent":260, "mortgage_value":1500, "unmortgage_value":1650, "house1rent":1300, "house2rent":3900, "house3rent":9000, "house4rent":11000, "Hotelrent":12750, "colorset":520, "house price":2000},
              { "name":"Bond Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3200, "base_rent":280, "mortgage_value":1600, "unmortgage_value":1760, "house1rent":1500, "house2rent":4500, "house3rent":10000, "house4rent":12000, "Hotelrent":14000, "colorset":560, "house price":2000},
              { "name":"Park Lane", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3500, "base_rent":350, "mortgage_value":1750, "unmortgage_value":1930, "house1rent":1750, "house2rent":5000, "house3rent":11000, "house4rent":13000, "Hotelrent":15000, "colorset":700, "house price":2000},
              { "name":"Mayfair", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":4000, "base_rent":500, "mortgage_value":2000, "unmortgage_value":2200, "house1rent":2000, "house2rent":6000, "house3rent":14000, "house4rent":17000, "Hotelrent":20000, "colorset":1000, "house price":2000}
]    
i = 0          
              
# =============================================================================
# while i != 22:
#     if Properties[i]["mortgaged"]==False:
#         Properties[i]["base_rent"]=0
#     i+=1
# next chance: To see if the next player should play his chance
# =============================================================================
Run = True
same_roll_count=0
Playername = Player1name
chance_count = 0
Player_no =0
dice_roll_1=9
dice_roll_2=10
while Run:
    if Playername==Player1name:
        Player_no=0
    elif Playername==Player2name:
        Player_no=1
    elif Playername==Player3name:
        Player_no=2
    elif Playername==Player4name:
        Player_no=3
    next_chance=False
    while next_chance==False:
        Players[Player_no]["jail"]=False
        if dice_roll_1==dice_roll_2:
            chance_count-=1

        dice_roll_1=random.randrange(1,7)
        dice_roll_2=random.randrange(1,7)


        

        chance_count+=1
        Player_no=chance_count-1
        if chance_count==1:
            Playername=Player1name
        elif chance_count==2:
            Playername=Player2name
        elif chance_count==3:
            Playername=Player3name
        elif chance_count==4:
            Playername=Player4name
            chance_count=0
        if dice_roll_1==dice_roll_2:
            next_chance=False
            same_roll_count+=1
            if same_roll_count==3:
                next_chance=True
                same_roll_count=0
                chance_count+=1
                Player_no=chance_count-1
                Players[Player_no]["jail"]=True
        else: 
            next_chance=True
            same_roll_count=0
            Players[Player_no]["jail"]=False
        
            
        dice_roll = dice_roll_1 + dice_roll_2
        print(Playername + " got " + str(dice_roll_1)+" and "+ str(dice_roll_2)+ " which is "+str(dice_roll)) 
        print("jail for " + Playername + " is "+ str(Players[Player_no]["jail"]))
        print(Player_no)
        if Players[Player_no]["jail"]==False:
            Players[Player_no]["position"]+=dice_roll
            if Players[Player_no]["position"]>=40:
                Players[Player_no]["position"]-=40
                Players[Player_no]["round"]+=1
        print(str(Players[Player_no]["name"])+" is on "+str(Players[Player_no]["position"]))
        int(Players[Player_no]["position"])
        if Players[Player_no]["position"]>=0 and Players[Player_no]["round"]!=Players[Player_no]["go_collections"]:
            Players[Player_no]["current_balance"]  +=2000
            Players[Player_no]["go_collections"]
        if Players[Player_no]["position"]==4:
            Players[Player_no]["current_balance"]-=2000
        if Players[Player_no]["position"]==38:
            Players[Player_no]["current_balance"]-=1000
        if Players[Player_no]["position"]==7:
            Chance()
            
        print(Players[Player_no]["current_balance"]) 
        
        x=input(print("Continue"))
            

 
