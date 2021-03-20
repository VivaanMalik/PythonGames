#GivingPlayersValue
#TypesOfFakePeople@Jordindian
#XD
#LOL
#Credits:VivaanDaGr8
#Ya bro  its true
global Player_no
import random
import sys
global Utilities
global same_roll_count

while True:
    try:
        players_playing=int(input("Enter the number of players who wanna play: "))
        while players_playing<=1 or players_playing>=11:
            players_playing=int(input("Enter the number of players who wanna play: "))
        break
    except ValueError:
        print("Try checking the digit you enetred...and type only 2 to 10...")
        continue
Players=[]

players_name_entering=0
while players_name_entering!=players_playing:
    while True:
        try:
            player_name = input(print("Enter name of Player "+ (str(players_name_entering+1)) + ": "))
            o=0
            while o!= players_name_entering:
                while player_name=="Nobody" or player_name==Players[o]["name"]:
                    print("Don't enter Nobody and don't repeat names")
                    player_name = input(print("Enter name of Player "+ (str(players_name_entering+1)) + ": "))
                                                   
                o+=1
            break
        except ValueError:
            print("Don't enter Nobody and don't repeat names")
            continue
    Players.append({ "name":player_name, "current_balance":15000, "position":0, "jail":False, "round":0, "go_collections":0, "jail_card":False, "House_no":0, "Hotel_no":0, "tmp_chance_multiplier":False, "jail_count":0, "dice_roll":0, "items":[]})        
    players_name_entering+=1

players_playing=str(players_playing)
     
def Chance(): 
    Chance_cards=[{"text":"Another player files a court case against you. Choose which player and pay them 500."},
                  {"text":"Advance to GO."},
                  {"text":"Advance to the nearest station space. If unowned, you may buy it from the bank. If owned, pay the owner twice the rental to which they are otherwise entitled. If you pass GO collect 2000."},
                  {"text":"Advance to the nearest station space. If unowned, you may buy it from the bank. If owned, pay the owner twice the rental to which they are otherwise entitled. If you pass GO collect 2000."},
                  {"text":"Advance to the nearest Utility. If unowned, you may buy it from the bank. If owned, throw dice and pay owner a total 10,000 times amount thrown. If you pass GO collect 2000."},
                  {"text":"Summoned for jury duty. Go back 3 spaces."},
                  {"text":"Accept the position of CEO at a high-powered investment banking firm. Collect a signing bonus of 1500."},
                  {"text":"Convicted of Identity Theft. Go to Jail. Do not pass GO, do not collect 2000."},
                  {"text":"Get a tax break for driving a hybrid. Collect 500."},
                  {"text":"Splash out on a trip to Pall Mall. If you pass GO, collect 2000."},
                  {"text":"Ride first-class to King Cross Station. If you pass GO, collect 2000."},
                  {"text":"You are acquitted. GET OUT OF JAIL FREE. This may be kept until needed or traded."},
                  {"text":"Make a donation for disaster relief. Pay 150."},
                  {"text":"Your city does a tax revaluation. Pay 250 for each house and 1000 for each hotel you own."},
                  {"text":"Jump on a plane to Trafalgar Square. if you pass GO, collect 2000."},
                  {"text":"Take a helicopter ride to Mayfair."}
        ]

    card_no=random.randrange(1,17)-1
    card_no=random.randrange(1,17)-1 # Change this to len(Chance_cards)

    print(Chance_cards[card_no]["text"])
    if card_no+1 ==1:
        player_output=0
        while True:
            try:
                tmp_player_output = int(input("type the player number from 1 to "+players_playing+": "))
                player_output=tmp_player_output-1
                while player_output==Player_no or player_output>=int(players_playing) or player_output<=-1:
                    tmp_player_output = int(input("type the player number from 1 to "+players_playing+": "))
                    player_output=tmp_player_output-1
                break
            except ValueError:
                print("Enter a number from 1 to "+players_playing+"...")
                continue

        
        Players[Player_no]["current_balance"] -=500
        Players[int(player_output)]["current_balance"]+=500
    elif card_no+1==2:
        Players[Player_no]["position"]=0
        Players[Player_no]["current_balance"]+=2000
    elif card_no+1==3 or card_no+1==4:
        while not Players[Player_no]["position"]%10==5:
            Players[Player_no]["position"]+=1
        if Players[Player_no]["position"]>=40:
            Players[Player_no]["position"]-=40
            Players[Player_no]["round"]+=1
        Players[Player_no]["tmp_chance_multiplier"]=True
        Station()
    elif card_no+1==5:
        if Players[Player_no]["position"]>=13 and Players[Player_no]["position"]<=28:
            Players[Player_no]["position"]=28
            if not Utilities[1]["Owner"]=="Nobody":
                Utilities[1]["rent_multiplier"]=10
        if Players[Player_no]["position"]>=40:
            Players[Player_no]["position"]-=40
            Players[Player_no]["round"]+=1
        else:
            Players[Player_no]["position"]=12
            if not Utilities[0]["Owner"]=="Nobody":
                Utilities[0]["rent_multiplier"]=10
        Utility()
    elif card_no+1==6:
        Players[Player_no]["position"]-=3
    elif card_no+1==7:
        Players[Player_no]["current_balance"]+=1500
    elif card_no+1==8:
        Players[Player_no]["jail"]=True
    elif card_no+1==9:
        Players[Player_no]["current_balance"]+=500
    elif card_no+1==10:
        if Players[Player_no]["position"]<=11:
            Players[Player_no]["position"]=11
        else:
            Players[Player_no]["position"]=11
            Players[Player_no]["current_balance"]+=2000
    elif card_no+1==11:
        if Players[Player_no]["position"]<=5:
            Players[Player_no]["position"]=5
        else:
            Players[Player_no]["position"]=5
            Players[Player_no]["current_balance"]+=2000
    elif card_no+1==12:
        Players[Player_no]["jail_card"]=True
        #v b like "M gonna write da code for dis later coz m bingin rn while hearin #ESBR - #Eat. Sleep. Binge. Repeat. LOL XD" 
    elif card_no+1==13:
       Players[Player_no]["current_balance"]-=150        
    elif card_no+1==14:
        Players[Player_no]["current_balance"]-=((Players[Player_no]["House_no"]*250)+(Players[Player_no]["Hotel_no"]*1000))
    elif card_no+1==15:
        if Players[Player_no]["position"]>=25:
            Players[Player_no]["current_balance"]+=2000
            Players[Player_no]["position"]=24
        else:
            Players[Player_no]["position"]=24
    elif card_no+1==16:
        Players[Player_no]["position"]=39
        
def Community_Chest():
    Community_Chest_cards=[
        {"text":"Make it big in Hollywood. Collect 2000 in a Movie Deal."},
        {"text":"Take dance lessons from a celerity coach. Pay 500."},
        {"text":"Recieve a royal pardon. Get out of jail free. This may be used when needed or traded"},
        {"text":"Arrested for insider trading. Go to jail. Do not pass GO. Do not Collect 2000."},
        {"text":"You owe back taxes. Pay 500."},
        {"text":"You are runner up on a reality TV show. Collect 100."},
        {"text":"Sell your lifetime tickets. Collect 200."},
        {"text":"Your trust fund becomes available. Collect 500."},
        {"text":"Advance to GO. Collect 2000."},
        {"text":"Run for mayor. Collect 100 from each player to fund your campaign"},
        {"text":"You are chosen as mascot for your team's big game at Wembley. Collect 250 for your services."},
        {"text":"Win the lottery. Collect 1000."},
        {"text":"Redo the landscaping at all your properties. Pay 400 per house and 1150 per hotel you own."},
        {"text":"Your computer network hits with a virus. Pay 1000."},
        {"text":"Promote your new book on the morning news. Recieve 100 in bonus sales."},
        {"text":"Win big at the Casino. Collect 1000."  }
        
        ]
    card_no=random.randrange(1,17)-1

    print(Community_Chest_cards[card_no]["text"])
    if card_no+1 ==1:
        Players[Player_no]["current_balance"]+=2000
    elif card_no+1==2:
        Players[Player_no]["current_balance"]-=500
    elif card_no+1==3:
        Players[Player_no]["jail_card"]=True
    elif card_no+1==4:
        Players[Player_no]["jail"]=True
    elif card_no+1==5:
        Players[Player_no]["current_balance"]-=500
    elif card_no+1==6:
        Players[Player_no]["current_balance"]+=100
    elif card_no+1==7:
        Players[Player_no]["current_balance"]+=200
    elif card_no+1==8:
        Players[Player_no]["current_balance"]+=500
    elif card_no+1==9:
        Players[Player_no]["current_balance"]+=2000
        Players[Player_no]["position"]=0
    elif card_no+1==10:
        i=0
        while int(i) !=int(players_playing)-1:
            Players[Player_no]["current_balance"]+=100
            Players[i]["current_balance"]-=100
            i+=1
    elif card_no+1==11:
        Players[Player_no]["current_balance"]+=250
    elif card_no+1==12:
        Players[Player_no]["current_balance"]+=1000
    elif card_no+1==13:
        Players[Player_no]["current_balance"]-=((Players[Player_no]["House_no"]*400)+(Players[Player_no]["Hotel_no"]*1150))
    elif card_no+1==14:
        Players[Player_no]["current_balance"]-=1000
    elif card_no+1==15:
        Players[Player_no]["current_balance"]+=100
    elif card_no+1==16:
        Players[Player_no]["current_balance"]+=1000

        
Properties_backup = [{ "name":"Old Kent Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":600, "base_rent":20, "mortgage_value":300, "unmortgage_value":330, "house1rent":100, "house2rent":300, "house3rent":900, "house4rent":1600, "Hotelrent":2500, "colorset":40, "house price":500, "Housescheck":5},
              { "name":"Whitechapel Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":600, "base_rent":40, "mortgage_value":300, "unmortgage_value":330, "house1rent":200, "house2rent":600, "house3rent":1800, "house4rent":3200, "Hotelrent":4500, "colorset":80, "house price":500, "Housescheck":5},
              { "name":"The Angel Islington", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1000, "base_rent":60, "mortgage_value":500, "unmortgage_value":550, "house1rent":300, "house2rent":900, "house3rent":2700, "house4rent":4000, "Hotelrent":5500, "colorset":120,  "house price":500, "Housescheck":5},
              { "name":"Euston Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1000, "base_rent":60, "mortgage_value":500, "unmortgage_value":550, "house1rent":300, "house2rent":900, "house3rent":2700, "house4rent":4000, "Hotelrent":5500, "colorset":120,  "house price":500, "Housescheck":5},
              { "name":"Pentonville Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1200, "base_rent":80, "mortgage_value":600, "unmortgage_value":660, "house1rent":400, "house2rent":1000, "house3rent":3000, "house4rent":4500, "Hotelrent":6000, "colorset":160, "house price":500, "Housescheck":5},
              { "name":"Pall Mall", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1400, "base_rent":100, "mortgage_value":700, "unmortgage_value":770, "house1rent":500, "house2rent":1500, "house3rent":4500, "house4rent":6250, "Hotelrent":7500, "colorset":200, "house price":1000, "Housescheck":5},
              { "name":"White Hall", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1400, "base_rent":100, "mortgage_value":700, "unmortgage_value":770, "house1rent":500, "house2rent":1500, "house3rent":4500, "house4rent":6250, "Hotelrent":7500, "colorset":200, "house price":1000, "Housescheck":5},
              { "name":"Northumberland Avenue", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1600, "base_rent":120, "mortgage_value":800, "unmortgage_value":880, "house1rent":600, "house2rent":1800, "house3rent":5000, "house4rent":7000, "Hotelrent":9000, "colorset":240, "house price":1000, "Housescheck":5},
              { "name":"Bow Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1800, "base_rent":140, "mortgage_value":900, "unmortgage_value":990, "house1rent":700, "house2rent":2000, "house3rent":5500, "house4rent":7500, "Hotelrent":9500, "colorset":280, "house price":1000, "Housescheck":5},
              { "name":"Marlborough Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1800, "base_rent":140, "mortgage_value":900, "unmortgage_value":990, "house1rent":700, "house2rent":2000, "house3rent":5500, "house4rent":7500, "Hotelrent":9500, "colorset":280, "house price":1000, "Housescheck":5},
              { "name":"Vine Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2000, "base_rent":160, "mortgage_value":1000, "unmortgage_value":1100, "house1rent":800, "house2rent":2200, "house3rent":6000, "house4rent":8000, "Hotelrent":10000, "colorset":320, "house price":1000, "Housescheck":5},
              { "name":"Strand", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2200, "base_rent":180, "mortgage_value":1100, "unmortgage_value":1210, "house1rent":900, "house2rent":2500, "house3rent":7000, "house4rent":8750, "Hotelrent":10500, "colorset":360, "house price":1500, "Housescheck":5},
              { "name":"Fleet Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2200, "base_rent":180, "mortgage_value":1100, "unmortgage_value":1210, "house1rent":900, "house2rent":2500, "house3rent":7000, "house4rent":8750, "Hotelrent":10500, "colorset":360, "house price":1500, "Housescheck":5},
              { "name":"Trafalgar Square", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2400, "base_rent":200, "mortgage_value":1200, "unmortgage_value":1320, "house1rent":1000, "house2rent":3000, "house3rent":7500, "house4rent":9250, "Hotelrent":11000, "colorset":400, "house price":1500, "Housescheck":5},
              { "name":"Leicester Square", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2600, "base_rent":220, "mortgage_value":1300, "unmortgage_value":1430, "house1rent":1100, "house2rent":3300, "house3rent":8000, "house4rent":9750, "Hotelrent":11500, "colorset":440, "house price":1500, "Housescheck":5},
              { "name":"Coventry Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2600, "base_rent":220, "mortgage_value":1300, "unmortgage_value":1430, "house1rent":1100, "house2rent":3300, "house3rent":8000, "house4rent":9750, "Hotelrent":11500, "colorset":440, "house price":1500, "Housescheck":5},
              { "name":"Piccadilly", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2800, "base_rent":240, "mortgage_value":1400, "unmortgage_value":1540, "house1rent":1200, "house2rent":3600, "house3rent":8500, "house4rent":10250, "Hotelrent":12000, "colorset":480, "house price":1500, "Housescheck":5},
              { "name":"Regent Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3000, "base_rent":260, "mortgage_value":1500, "unmortgage_value":1650, "house1rent":1300, "house2rent":3900, "house3rent":9000, "house4rent":11000, "Hotelrent":12750, "colorset":520, "house price":2000, "Housescheck":5},
              { "name":"Oxford Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3000, "base_rent":260, "mortgage_value":1500, "unmortgage_value":1650, "house1rent":1300, "house2rent":3900, "house3rent":9000, "house4rent":11000, "Hotelrent":12750, "colorset":520, "house price":2000, "Housescheck":5},
              { "name":"Bond Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3200, "base_rent":280, "mortgage_value":1600, "unmortgage_value":1760, "house1rent":1500, "house2rent":4500, "house3rent":10000, "house4rent":12000, "Hotelrent":14000, "colorset":560, "house price":2000, "Housescheck":5},
              { "name":"Park Lane", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3500, "base_rent":350, "mortgage_value":1750, "unmortgage_value":1930, "house1rent":1750, "house2rent":5000, "house3rent":11000, "house4rent":13000, "Hotelrent":15000, "colorset":700, "house price":2000, "Housescheck":5},
              { "name":"Mayfair", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":4000, "base_rent":500, "mortgage_value":2000, "unmortgage_value":2200, "house1rent":2000, "house2rent":6000, "house3rent":14000, "house4rent":17000, "Hotelrent":20000, "colorset":1000, "house price":2000, "Housescheck":5}
    ]

Properties = [{ "name":"Old Kent Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":600, "base_rent":20, "mortgage_value":300, "unmortgage_value":330, "house1rent":100, "house2rent":300, "house3rent":900, "house4rent":1600, "Hotelrent":2500, "colorset":40, "house price":500, "Housescheck":5},
              { "name":"Whitechapel Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":600, "base_rent":40, "mortgage_value":300, "unmortgage_value":330, "house1rent":200, "house2rent":600, "house3rent":1800, "house4rent":3200, "Hotelrent":4500, "colorset":80, "house price":500, "Housescheck":5},
              { "name":"The Angel Islington", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1000, "base_rent":60, "mortgage_value":500, "unmortgage_value":550, "house1rent":300, "house2rent":900, "house3rent":2700, "house4rent":4000, "Hotelrent":5500, "colorset":120,  "house price":500, "Housescheck":5},
              { "name":"Euston Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1000, "base_rent":60, "mortgage_value":500, "unmortgage_value":550, "house1rent":300, "house2rent":900, "house3rent":2700, "house4rent":4000, "Hotelrent":5500, "colorset":120,  "house price":500, "Housescheck":5},
              { "name":"Pentonville Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1200, "base_rent":80, "mortgage_value":600, "unmortgage_value":660, "house1rent":400, "house2rent":1000, "house3rent":3000, "house4rent":4500, "Hotelrent":6000, "colorset":160, "house price":500, "Housescheck":5},
              { "name":"Pall Mall", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1400, "base_rent":100, "mortgage_value":700, "unmortgage_value":770, "house1rent":500, "house2rent":1500, "house3rent":4500, "house4rent":6250, "Hotelrent":7500, "colorset":200, "house price":1000, "Housescheck":5},
              { "name":"White Hall", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1400, "base_rent":100, "mortgage_value":700, "unmortgage_value":770, "house1rent":500, "house2rent":1500, "house3rent":4500, "house4rent":6250, "Hotelrent":7500, "colorset":200, "house price":1000, "Housescheck":5},
              { "name":"Northumberland Avenue", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1600, "base_rent":120, "mortgage_value":800, "unmortgage_value":880, "house1rent":600, "house2rent":1800, "house3rent":5000, "house4rent":7000, "Hotelrent":9000, "colorset":240, "house price":1000, "Housescheck":5},
              { "name":"Bow Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1800, "base_rent":140, "mortgage_value":900, "unmortgage_value":990, "house1rent":700, "house2rent":2000, "house3rent":5500, "house4rent":7500, "Hotelrent":9500, "colorset":280, "house price":1000, "Housescheck":5},
              { "name":"Marlborough Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1800, "base_rent":140, "mortgage_value":900, "unmortgage_value":990, "house1rent":700, "house2rent":2000, "house3rent":5500, "house4rent":7500, "Hotelrent":9500, "colorset":280, "house price":1000, "Housescheck":5},
              { "name":"Vine Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2000, "base_rent":160, "mortgage_value":1000, "unmortgage_value":1100, "house1rent":800, "house2rent":2200, "house3rent":6000, "house4rent":8000, "Hotelrent":10000, "colorset":320, "house price":1000, "Housescheck":5},
              { "name":"Strand", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2200, "base_rent":180, "mortgage_value":1100, "unmortgage_value":1210, "house1rent":900, "house2rent":2500, "house3rent":7000, "house4rent":8750, "Hotelrent":10500, "colorset":360, "house price":1500, "Housescheck":5},
              { "name":"Fleet Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2200, "base_rent":180, "mortgage_value":1100, "unmortgage_value":1210, "house1rent":900, "house2rent":2500, "house3rent":7000, "house4rent":8750, "Hotelrent":10500, "colorset":360, "house price":1500, "Housescheck":5},
              { "name":"Trafalgar Square", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2400, "base_rent":200, "mortgage_value":1200, "unmortgage_value":1320, "house1rent":1000, "house2rent":3000, "house3rent":7500, "house4rent":9250, "Hotelrent":11000, "colorset":400, "house price":1500, "Housescheck":5},
              { "name":"Leicester Square", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2600, "base_rent":220, "mortgage_value":1300, "unmortgage_value":1430, "house1rent":1100, "house2rent":3300, "house3rent":8000, "house4rent":9750, "Hotelrent":11500, "colorset":440, "house price":1500, "Housescheck":5},
              { "name":"Coventry Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2600, "base_rent":220, "mortgage_value":1300, "unmortgage_value":1430, "house1rent":1100, "house2rent":3300, "house3rent":8000, "house4rent":9750, "Hotelrent":11500, "colorset":440, "house price":1500, "Housescheck":5},
              { "name":"Piccadilly", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2800, "base_rent":240, "mortgage_value":1400, "unmortgage_value":1540, "house1rent":1200, "house2rent":3600, "house3rent":8500, "house4rent":10250, "Hotelrent":12000, "colorset":480, "house price":1500, "Housescheck":5},
              { "name":"Regent Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3000, "base_rent":260, "mortgage_value":1500, "unmortgage_value":1650, "house1rent":1300, "house2rent":3900, "house3rent":9000, "house4rent":11000, "Hotelrent":12750, "colorset":520, "house price":2000, "Housescheck":5},
              { "name":"Oxford Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3000, "base_rent":260, "mortgage_value":1500, "unmortgage_value":1650, "house1rent":1300, "house2rent":3900, "house3rent":9000, "house4rent":11000, "Hotelrent":12750, "colorset":520, "house price":2000, "Housescheck":5},
              { "name":"Bond Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3200, "base_rent":280, "mortgage_value":1600, "unmortgage_value":1760, "house1rent":1500, "house2rent":4500, "house3rent":10000, "house4rent":12000, "Hotelrent":14000, "colorset":560, "house price":2000, "Housescheck":5},
              { "name":"Park Lane", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":3500, "base_rent":350, "mortgage_value":1750, "unmortgage_value":1930, "house1rent":1750, "house2rent":5000, "house3rent":11000, "house4rent":13000, "Hotelrent":15000, "colorset":700, "house price":2000, "Housescheck":5},
              { "name":"Mayfair", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":4000, "base_rent":500, "mortgage_value":2000, "unmortgage_value":2200, "house1rent":2000, "house2rent":6000, "house3rent":14000, "house4rent":17000, "Hotelrent":20000, "colorset":1000, "house price":2000, "Housescheck":5}
    ]

Utilities_backup=[{"name":"Electric Company", "Owner":"Nobody", "Purchase_price":1500, "Mortgage_value":750, "Unmortgage_value":830, "rent_multiplier":4, "Player_val":0, "mortgaged":False},
           {"name":"Water works", "Owner":"Nobody", "Purchase_price":1500, "Mortgage_value":750, "Unmortgage_value":830, "rent_multiplier":4, "Player_val":0, "mortgaged":False}
    ]

Utilities=[{"name":"Electric Company", "Owner":"Nobody", "Purchase_price":1500, "Mortgage_value":750, "Unmortgage_value":830, "rent_multiplier":4, "Player_val":0, "mortgaged":False},
           {"name":"Water works", "Owner":"Nobody", "Purchase_price":1500, "Mortgage_value":750, "Unmortgage_value":830, "rent_multiplier":4, "Player_val":0, "mortgaged":False}
    ]

Stations_backup=[{"name":"King Cross Station", "Owner":"Nobody", "Purchase_price":2000, "Mortgage_value":1000, "Unmortgage_value":1100, "Player_val":0, "rent":250, "mortgaged":False},
          {"name":"Marylebone Station", "Owner":"Nobody", "Purchase_price":2000, "Mortgage_value":1000, "Unmortgage_value":1100, "Player_val":0, "rent":250, "mortgaged":False},
          {"name":"Fenchurch Station", "Owner":"Nobody", "Purchase_price":2000, "Mortgage_value":1000, "Unmortgage_value":1100, "Player_val":0, "rent":250, "mortgaged":False},
          {"name":"Liverpool Station", "Owner":"Nobody", "Purchase_price":2000, "Mortgage_value":1000, "Unmortgage_value":1100, "Player_val":0, "rent":250, "mortgaged":False}
    ]

Stations=[{"name":"King Cross Station", "Owner":"Nobody", "Purchase_price":2000, "Mortgage_value":1000, "Unmortgage_value":1100, "Player_val":0, "rent":250, "mortgaged":False},
          {"name":"Marylebone Station", "Owner":"Nobody", "Purchase_price":2000, "Mortgage_value":1000, "Unmortgage_value":1100, "Player_val":0, "rent":250, "mortgaged":False},
          {"name":"Fenchurch Station", "Owner":"Nobody", "Purchase_price":2000, "Mortgage_value":1000, "Unmortgage_value":1100, "Player_val":0, "rent":250, "mortgaged":False},
          {"name":"Liverpool Station", "Owner":"Nobody", "Purchase_price":2000, "Mortgage_value":1000, "Unmortgage_value":1100, "Player_val":0, "rent":250, "mortgaged":False}
    ]

def color_rent(property_no):
    #add if property is part of colorset
    if  Properties[0]["name"] in Players[player_no]["items"] and Properties[1]["name"] in Players[player_no]["items"] and Properties[property_no]["Houses"]==0:
        Properties[property_no]["base_rent"]=Properties[property_no]["colorset"]
        
    if  Properties[2]["name"] in Players[player_no]["items"] and Properties[3]["name"] in Players[player_no]["items"] and Properties[4]["name"] in Players[player_no]["items"] and Properties[property_no]["Houses"]==0:
        Properties[property_no]["base_rent"]=Properties[property_no]["colorset"]

    if  Properties[5]["name"] in Players[player_no]["items"] and Properties[6]["name"] in Players[player_no]["items"] and Properties[7]["name"] in Players[player_no]["items"] and Properties[property_no]["Houses"]==0:
        Properties[property_no]["base_rent"]=Properties[property_no]["colorset"]

    if  Properties[8]["name"] in Players[player_no]["items"] and Properties[9]["name"] in Players[player_no]["items"] and Properties[10]["name"] in Players[player_no]["items"] and Properties[property_no]["Houses"]==0:
        Properties[property_no]["base_rent"]=Properties[property_no]["colorset"]

    if  Properties[11]["name"] in Players[player_no]["items"] and Properties[12]["name"] in Players[player_no]["items"] and Properties[13]["name"] in Players[player_no]["items"] and Properties[property_no]["Houses"]==0:
        Properties[property_no]["base_rent"]=Properties[property_no]["colorset"]

    if  Properties[14]["name"] in Players[player_no]["items"] and Properties[15]["name"] in Players[player_no]["items"] and Properties[16]["name"] in Players[player_no]["items"] and Properties[property_no]["Houses"]==0:
        Properties[property_no]["base_rent"]=Properties[property_no]["colorset"]

    if  Properties[17]["name"] in Players[player_no]["items"] and Properties[18]["name"] in Players[player_no]["items"] and Properties[19]["name"] in Players[player_no]["items"] and Properties[property_no]["Houses"]==0:
        Properties[property_no]["base_rent"]=Properties[property_no]["colorset"]

    if  Properties[20]["name"] in Players[player_no]["items"] and Properties[21]["name"] in Players[player_no]["items"] and Properties[property_no]["Houses"]==0:
        Properties[property_no]["base_rent"]=Properties[property_no]["colorset"]

def Sell():
    print("You are out of money... you have to sell something")
    print("Here are your Properties, Stations and Utilities. Your bank will buy your asset for 90% of the total price including houses and hotels")
    print("If mortgaged, the unmortgage value will be deducted from your newly earned money")
    items="|"
    item_no=0
    while item_count!=len(Players[player_no]["items"]):
        items="|"
        items+=str(Players[int(player_no)]["items"][item_no])
        item_no+=1
        if items!=len(Players[player_no]["items"]):
            items+="|"
        if items=="|":
            items="Nothing yet..."
        item_count+=1
        print(item_no+items)
    while True:
        try:
            sell_no = int(input("Type the number of your asset you wanna sell"))
            sell_no-=1
            while sell_no<=-1 or sell_no>=len(Players[player_no]["items"]):
                sell_no = int(input("Type the number of your asset you wanna sell"))
                sell_no-=1
            break
        except ValueError:
            print("Enter a number from 1 to "+len(Players[player_no]["items"])+"...")
            continue
    i=0
    while i!= len(Properties):
        if Players[player_no]["items"][sell_no]==Properties[i]["name"]:
            Sell_price=((Properties[i]["Purchase_price"]+(Properties[i]["house price"]*Properties[i]["Houses"]))/10)*9
            Players[player_no]["current_balance"]+=Sell_price
            Players[player_no]["items"].remove(Players[player_no]["items"][sell_no])
            Properties[i]=Properties_backup[i]
            if Properties[i]["mortgaged"]==True:
                Players[Player_no]["current_balance"]-=Properties[i]["unmortgage_value"]
        i+=1
    i=0
    while i!= len(Stations):
        if Players[player_no]["items"][sell_no]==Stations[i]["name"]:
            
            Sell_price=(Stations["Purchase_price"]/10)*9
            Players[player_no]["current_balance"]+=Sell_price
            Players[player_no]["items"].remove(Players[player_no]["items"][sell_no])
            Stations[i]=Stations_backup[i]
            
            if Stations[i]["mortgaged"]==True:
                Players[Player_no]["current_balance"]-=Stations[i]["unmortgage_value"]
        i+=1
    i=0
    while i!= len(Utilities):
        if Players[player_no]["items"][sell_no]==Utilities[i]["name"]:
            
            Sell_price=(Utilities[i]["Purchase_price"]/10)*9
            Players[player_no]["current_balance"]+=Sell_price
            Players[player_no]["items"].remove(Players[player_no]["items"][sell_no])
            Utilities[i]=Utilities_backup[i]
            
            if Utilities[i]["mortgaged"]==True:
                Players[Player_no]["current_balance"]-=Utilities[i]["unmortgage_value"]
        i+=1     
    
def Mortgage():
    print("You are out of money... you have to mortgage something")
    print("Here are your owned properties, stations and utilities")
    items="|"
    item_no=0
    while item_count!=len(Players[player_no]["items"]):
        items="|"
        items+=str(Players[int(player_no)]["items"][item_no])
        item_no+=1
        if items!=len(Players[player_no]["items"]):
            items+="|"
        if items=="|":
            items="Nothing yet..."
        item_count+=1
        print(item_no+items)
    while True:
        try:
            mortgage_no = int(input("Type the number of your asset you wanna mortgage"))
            mortgage_no-=1
            while mortgage_no<=-1 or mortgage_no>=len(Players[player_no]["items"]):
                mortgage_no = int(input("Type the number of your asset you wanna mortgage"))
                mortgage_no-=1
            break
        except ValueError:
            print("Enter a number from 1 to "+len(Players[player_no]["items"])+"...")
            continue
    i=0
    while i!= len(Properties):
        if Players[player_no]["items"][mortage_no]==Properties[i]["name"]:
            Properties[i]["mortgaged"]=True
            Players[Player_no]["current_balance"]+=Properties[i]["mortgage_value"]
        i+=1
    i=0
    while i!= len(Stations):
        if Players[player_no]["items"][mortage_no]==Stations[i]["name"]:
            Stations[i]["mortgaged"]=True
            Players[Player_no]["current_balance"]+=Stations[i]["mortgage_value"]
        i+=1
    i=0
    while i!= len(Utilities):
        if Players[player_no]["items"][mortage_no]==Utilities[i]["name"]:
            Utilities[i]["mortgaged"]=True
            Players[Player_no]["current_balance"]+=Utilities[i]["mortgage_value"]
        i+=1     
    
def Property():
    
    if Players[Player_no]["position"]==1:
        property_no=0
    if Players[Player_no]["position"]==3:
        property_no=1
    if Players[Player_no]["position"]==6:
        property_no=2
    if Players[Player_no]["position"]==8:
        property_no=3
    if Players[Player_no]["position"]==9:
        property_no=4
    if Players[Player_no]["position"]==11:
        property_no=5
    if Players[Player_no]["position"]==13:
        property_no=6
    if Players[Player_no]["position"]==14:
        property_no=7
    if Players[Player_no]["position"]==16:
        property_no=8
    if Players[Player_no]["position"]==18:
        property_no=9
    if Players[Player_no]["position"]==19:
        property_no=10
    if Players[Player_no]["position"]==21:
        property_no=11
    if Players[Player_no]["position"]==23:
        property_no=12
    if Players[Player_no]["position"]==24:
        property_no=13
    if Players[Player_no]["position"]==26:
        property_no=14
    if Players[Player_no]["position"]==27:
        property_no=15
    if Players[Player_no]["position"]==29:
        property_no=16
    if Players[Player_no]["position"]==31:
        property_no=17
    if Players[Player_no]["position"]==32:
        property_no=18
    if Players[Player_no]["position"]==34:
        property_no=19
    if Players[Player_no]["position"]==37:
        property_no=20
    if Players[Player_no]["position"]==39:
        property_no=21
    if Properties[property_no]["Owner"]=="Nobody":
        confirmation=0
        while True:
            try:
                confirmation=input("Do you wanna buy "+ Properties[property_no]["name"] + " for "+  str(Properties[property_no]["Purchase_price"]) +"?-1 for True | 2 for False: ")
                confirmation=int(confirmation)
                while confirmation<=0 or confirmation>=3:
                    confirmation=input("Do you wanna buy "+ Properties[property_no]["name"] + " for "+  str(Properties[property_no]["Purchase_price"]) +"?-1 for True | 2 for False: ")
                    confirmation=int(confirmation)
                break
            except ValueError:
                print("Try checking the digit you enetred...and type only 1 or 2...")
                continue
        if confirmation==1:
            if Players[Player_no]["current_balance"]-Properties[property_no]["Purchase_price"]<=-1:
                print("Mortgage time")
            else:
                Players[Player_no]["current_balance"]-=Properties[property_no]["Purchase_price"]
                Properties[property_no]["Owner"]=Players[Player_no]["name"]
                Properties[property_no]["Player_val"]=Player_no+1
                print(Players[Player_no]["name"] + ", Congrats!!! You bought "+ Properties[property_no]["name"]+"!!!")
                Players[Player_no]["items"].append(Properties[property_no]["name"])
    elif Properties[property_no]["Owner"]==Players[Player_no]["name"]:
        if Properties[property_no]["Housescheck"]!=0:
            while True:
                try:
                    confirmation=input("Do you wanna buy a house/hotel for "+  str(Properties[property_no]["house price"]) +"?-1 for True | 2 for False: ")
                    confirmation=int(confirmation)
                    while confirmation<=0 or confirmation>=3:
                        confirmation=input("Do you wanna buy a house/hotel for "+  str(Properties[property_no]["house price"]) +"?-1 for True | 2 for False: ")
                        confirmation=int(confirmation)
                    break
                except ValueError:
                    print("Try checking the digit you enetred...and type only 1 or 2...")
                    continue
            if confirmation==1:
                if Properties[property_no]["Housescheck"]!=0:
                    Properties[property_no]["Housescheck"]-=1
                    Properties[property_no]["Houses"]+=1
                    Players[Player_no]["current_balance"]-=Properties[property_no]["house price"]
                    if Properties[property_no]["Housescheck"]==4:
                        Properties[property_no]["base_rent"]=Properties[property_no]["house1rent"]
                    if Properties[property_no]["Housescheck"]==3:
                        Properties[property_no]["base_rent"]=Properties[property_no]["house2rent"]
                    if Properties[property_no]["Housescheck"]==2:
                        Properties[property_no]["base_rent"]=Properties[property_no]["house3rent"]
                    if Properties[property_no]["Housescheck"]==1:
                        Properties[property_no]["base_rent"]=Properties[property_no]["house4rent"]
                    if Properties[property_no]["Housescheck"]==0:
                        Properties[property_no]["base_rent"]=Properties[property_no]["Hotelrent"]
                        print("You have maxed out "+Properties[property_no]["name"]+" Gz")
                    else:
                        print("You just built another house at "+Properties[property_no]["name"]+"!")
            
    
    elif Properties[property_no]["Owner"]!=Players[Player_no]["name"] and Properties[property_no]["mortgaged"]==False:
        #if Properties[property_no]["Housescheck"]==5
        Players[Player_no]["current_balance"]-=Properties[property_no]["base_rent"]
        print("You payed "+Properties[property_no]["Owner"]+" "+str(Properties[property_no]["base_rent"])+"!")
        
        
def Utility():
    global Station_no
    if Players[Player_no]["position"]==12:
        Utility_no=0
        Other_Utility_no=1
    if Players[Player_no]["position"]==28:
        Utility_no=1
        Other_Utility_no=0
    if Utilities[Utility_no]["Owner"]=="Nobody":
        confirmation=0
        while True:
            try:
                confirmation=input("Do you wanna buy "+ Utilities[Utility_no]["name"] + " for "+  str(Utilities[Utility_no]["Purchase_price"]) +"?-1 for True | 2 for False: ")
                confirmation=int(confirmation)
                while confirmation<=0 or confirmation>=3:
                    confirmation=input("Do you wanna buy "+ Utilities[Utility_no]["name"] + " for "+  str(Utilities[Utility_no]["Purchase_price"]) +"?-1 for True | 2 for False: ")
                    confirmation=int(confirmation)
                break
            except ValueError:
                print("Try checking the digit you enetred...and type only 1 or 2...")
                continue
        if confirmation==1:
            if Players[Player_no]["current_balance"]-Utilities[Utility_no]["Purchase_price"]<=-1:
                print("Mortgage time")
            else:
                Players[Player_no]["current_balance"]-=Utilities[Utility_no]["Purchase_price"]
                Utilities[Utility_no]["Owner"]=Players[Player_no]["name"]
                Utilities[Utility_no]["Player_val"]=Player_no+1
                print(Players[Player_no]["name"] + ", Congrats!!! You bought "+ Utilities[Utility_no]["name"]+"!!!")
                Players[Player_no]["items"].append(Utilities[Utility_no]["name"])
                    
    elif Utilities[Utility_no]["Owner"]!=Players[Player_no]["name"] and Utilities[Utility_no]["mortgaged"]==False:
        if Utilities[Utility_no]["Owner"]==Utilities[Other_Utility_no]["Owner"]:
            Utilities[Utility_no]["rent_multiplier"]=10
        
        Players[Player_no]["current_balance"]-=(dice_roll*10*Utilities[Utility_no]["rent_multiplier"])
        Players[Utilities[Utility_no]["Player_val"]-1]["current_balance"]+=(dice_roll*10*Utilities[Utility_no]["rent_multiplier"])
        rent_amount=(dice_roll*10*Utilities[Utility_no]["rent_multiplier"])
        if not Utilities[Utility_no]["Owner"]==Utilities[Other_Utility_no]["Owner"]:
            Utilities[Utility_no]["rent_multiplier"]=4
        print("You payed "+ str(Utilities[Utility_no]["Owner"]) + " " + str(rent_amount) + "!!!")

def Station():
    Stations[0]["rent"]=250
    Stations[1]["rent"]=250
    Stations[2]["rent"]=250
    Stations[3]["rent"]=250
    if Players[Player_no]["position"]==5:
        Station_no=0
    if Players[Player_no]["position"]==15:
        Station_no=1
    if Players[Player_no]["position"]==25:
        Station_no=2
    if Players[Player_no]["position"]==35:
        Station_no=3
    if Stations[Station_no]["Owner"]=="Nobody":
        confirmation=0
        while True:
            try:
                confirmation=input("Do you wanna buy "+ str(Stations[Station_no]["name"]) +" for "+str(Stations[Station_no]["Purchase_price"])+"?-1 for True | 2 for False: ")
                confirmation=int(confirmation)
                while confirmation<=0 or confirmation>=3:
                    confirmation=input("Do you wanna buy "+ Stations[Station_no]["name"] +" for "+str(Stations[Station_no]["Purchase_price"])+"?-1 for True | 2 for False: ")
                    confirmation=int(confirmation)
                break
            except ValueError:
                print("Try checking the digit you enetred...and type only 1 or 2...")
                continue
        if confirmation==1:
            Players[Player_no]["current_balance"]-Stations[Station_no]["Purchase_price"]
            Stations[Station_no]["Owner"]=Players[Player_no]["name"]
            Stations[Station_no]["Player_val"]=Player_no+1
            print(Players[Player_no]["name"] + ", Congrats!!! You bought "+ Stations[Station_no]["name"]+"!!!")
            Players[Player_no]["items"].append(Stations[Station_no]["name"])
            
    elif Stations[Station_no]["Owner"]!=Players[Player_no]["name"] and Stations[Station_no]["mortgaged"]==False:
        if Stations[Station_no]["Owner"]==Stations[0]["Owner"]:
            Stations[Station_no]["rent"]*=2
        if Stations[Station_no]["Owner"]==Stations[1]["Owner"]:
            Stations[Station_no]["rent"]*=2
        if Stations[Station_no]["Owner"]==Stations[2]["Owner"]:
            Stations[Station_no]["rent"]*=2
        if Stations[Station_no]["Owner"]==Stations[3]["Owner"]:
            Stations[Station_no]["rent"]*=2
        Stations[Station_no]["rent"]/=2
        if Players[Player_no]["tmp_chance_multiplier"]==True:
            Stations[Station_no]["rent"]*=2
            Players[Player_no]["tmp_chance_multiplier"]==False
        Players[Player_no]["current_balance"]-=Stations[Station_no]["rent"]
        Players[Stations[Station_no]["Player_val"]-1]["current_balance"]+=Stations[Station_no]["rent"]
        rent_amount=Stations[Station_no]["rent"]
        print("You payed "+ str(Stations[Station_no]["Owner"]) + " " + str(rent_amount) + "!!!")

def Position_check():
    
    
        
    if Players[Player_no]["jail"]==False:
        if Players[Player_no]["position"]>=0 and Players[Player_no]["round"]!=Players[Player_no]["go_collections"]:
            Players[Player_no]["current_balance"]  +=2000
            Players[Player_no]["go_collections"]+=1
            
        if Players[Player_no]["position"]==7 or Players[Player_no]["position"]==22 or Players[Player_no]["position"]==36:
            Chance()
            
        elif Players[Player_no]["position"]==2 or Players[Player_no]["position"]==17 or Players[Player_no]["position"]==33:
            Community_Chest()           
            
        elif Players[Player_no]["position"]==4:
            Players[Player_no]["current_balance"]-=2000
            
        elif Players[Player_no]["position"]==38:
            Players[Player_no]["current_balance"]-=1000
            
        elif Players[Player_no]["position"]==30:
            Players[Player_no]["jail"]=True 
        
        elif Players[Player_no]["position"]==12 or Players[Player_no]["position"]==28:
            Utility()
                    
        elif Players[Player_no]["position"]==5 or Players[Player_no]["position"]==15 or Players[Player_no]["position"]==25 or Players[Player_no]["position"]==35:
            Station()
            
        elif Players[Player_no]["position"]==1 or Players[Player_no]["position"]==3 or Players[Player_no]["position"]==6 or Players[Player_no]["position"]==8 or Players[Player_no]["position"]==9 or Players[Player_no]["position"]==11 or Players[Player_no]["position"]==13 or Players[Player_no]["position"]==14 or Players[Player_no]["position"]==16 or Players[Player_no]["position"]==18 or Players[Player_no]["position"]==19 or Players[Player_no]["position"]==21 or Players[Player_no]["position"]==23 or Players[Player_no]["position"]==24 or Players[Player_no]["position"]==26 or Players[Player_no]["position"]==27 or Players[Player_no]["position"]==29 or Players[Player_no]["position"]==31 or Players[Player_no]["position"]==32 or Players[Player_no]["position"]==34 or Players[Player_no]["position"]==37 or Players[Player_no]["position"]==39:
            Property()
        print(str(Players[Player_no]["name"])+" is on "+str(Players[Player_no]["position"]))
    
def Jail():
    
    global dice_roll_1
    global dice_roll_2
    global same_roll_count
    global Player_no
    print("You are in jail, lol XD")
    Players[Player_no]["jail_count"]+=1
    if Players[Player_no]["jail_count"]==3 and Players[Player_no]["jail"]==True:
        same_roll_count-=1
        Players[Player_no]["jail"]=False
        Players[Player_no]["dice_roll"]=dice_roll_1+dice_roll_2
    
    
    if Players[Player_no]["jail_card"]==True and Players[Player_no]["jail"]==True:
        while True:
            try:
                confirmation=int(input("Do you wanna use the get out of jail card?-1 for True | 2 for False: "))
                while confirmation<=0 or confirmation>=3:
                    confirmation=int(input("Do you wanna use the get out of jail card?-1 for True | 2 for False: "))
                break
            except ValueError:
                print("Try checking the digit you enetred...and type only 1 or 2...")
                continue
        if confirmation==True:
            Players[Player_no]["jail"]=False
            Player_no-=1
            same_roll_count-=1
            Players[Player_no]["jail_card"]=False
            Players[Player_no]["dice_roll"]=dice_roll_1+dice_roll_2
            
    if dice_roll_1==dice_roll_2 and same_roll_count!=4 and Players[Player_no]["jail"]==True:
        same_roll_count-=1
        Players[Player_no]["jail"]=False
        Players[Player_no]["dice_roll"]=dice_roll_1+dice_roll_2
    if Players[Player_no]["jail"]==False:
        Players[Player_no]["jail_count"]=0
        
    if Players[Player_no]["jail"]==True:
        while True:
            try:
                confirmation=int(input("Do you wanna pay 500 for getting out of jail?-1 for True | 2 for False: "))
                while confirmation<=0 or confirmation>=3:
                    confirmation=int(input("Do you wanna pay 500 for getting out of jail?-1 for True | 2 for False: "))
                break
            except ValueError:
                print("Try checking the digit you enetred...and type only 1 or 2...")
                continue
        if confirmation==True:
            Players[Player_no]["jail"]=False
            Player_no-=1
            same_roll_count-=1
            Players[Player_no]["current_balance"]-=500
            Players[Player_no]["dice_roll"]=dice_roll_1+dice_roll_2
            

      
    
    
Run = True
same_roll_count=0
Player_no =-1
Playername = Players[Player_no]["name"]
dice_roll_1=0
dice_roll_2=0
while Run:
    Player_no+=1
        
        
    if Player_no==int(players_playing):
        Player_no=0
    

# =============================================================================
#     Players[Player_no]["jail"]=False
# =============================================================================
    
    dice_roll_1=0
    dice_roll_2=0
    same_roll_count=0
    while dice_roll_1==dice_roll_2:
        dice_roll_1=random.randrange(1,7)
        dice_roll_2=random.randrange(1,7)
        Players[Player_no]["dice_roll"]=0
            
        Playername=Players[Player_no]["name"]   
        dice_roll = dice_roll_1 + dice_roll_2
        print(Playername + " got " + str(dice_roll_1)+" and "+ str(dice_roll_2)+ " which is "+str(dice_roll)) 
        print("jail for " + Playername + " is "+ str(Players[Player_no]["jail"]))
        print(Player_no)
        if Players[Player_no]["jail"]==False:
            Players[Player_no]["position"]+=dice_roll
            if Players[Player_no]["position"]>=40:
                Players[Player_no]["position"]-=40
            if Players[Player_no]["position"]==30:
                Players[Player_no]["jail"]=True
    
        if Players[Player_no]["jail"]==True:
            Players[Player_no]["position"]=10
            
    
    
            print(str(Players[Player_no]["name"])+" is on "+str(Players[Player_no]["position"]))
        same_roll_count+=1
        if same_roll_count==4:
            Players[Player_no]["jail"]=True
        if Players[Player_no]["position"]==30:
            Players[Player_no]["jail"]=True
            
            
        int(Players[Player_no]["position"])

        Position_check()
        if Players[Player_no]["jail"]==True:
            Players[Player_no]["position"]=10
            Jail()
        
            
        print(Players[Player_no]["current_balance"]) 
        
        x=input(print("Continue???"))
        if x == "no":
            print(":(")
            player_no=0
            while player_no!=int(players_playing):
                item_count=0
                items="|"
                item_no=0
                while item_count!=len(Players[player_no]["items"]):
                    items+=str(Players[int(player_no)]["items"][item_no])
                    items+="|"
                    item_count+=1
                    item_no+=1
                if items=="|":
                    items="|Nothing...gl next time...|"
                print(Players[int(player_no)]["name"]+" has "+str(Players[int(player_no)]["current_balance"])+" money and owns "+items)
                player_no+=1
            sys.exit()
