#GivingPlayersValue
#TypesOfFakePeople@Jordindian
#XD
Player1name = input(print("Enter name of Player 1"))
Player2name = input(print("Enter name of Player 2"))
Player3name = input(print("Enter name of Player 3"))
Player4name = input(print("Enter name of Player 4"))

Players = [{ "name":Player1name, "current_balance":15000, "position":0}, 
           { "name":Player2name, "current_balance":15000, "position":0},
           { "name":Player3name, "current_balance":15000, "position":0},
           { "name":Player4name, "current_balance":15000, "position":0}]
Player1 = Players[0]
Player2 = Players[1]
Player3 = Players[2]
Player4 = Players[3]
print(Player2["name"])

Properties = [{ "name":"Old Kent Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":600, "base_rent":20, "mortgage_value":300, "unmortgage_value":330, "house1rent":100, "house2rent":300, "house3rent":900, "house4rent":1600, "Hotelrent":2500, "colorset":40, "house price":500},
              { "name":"Whitechapel Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":600, "base_rent":40, "mortgage_value":300, "unmortgage_value":330, "house1rent":200, "house2rent":600, "house3rent":1800, "house4rent":3200, "Hotelrent":4500, "colorset":80, "house price":500},
              { "name":"The Angel Islington", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1000, "base_rent":60, "mortgage_value":500, "unmortgage_value":550, "house1rent":300, "house2rent":900, "house3rent":2700, "house4rent":4000, "Hotelrent":5500, "colorset":120,  "house price":500},
              { "name":"Euston Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1000, "base_rent":60, "mortgage_value":500, "unmortgage_value":550, "house1rent":300, "house2rent":900, "house3rent":2700, "house4rent":4000, "Hotelrent":5500, "colorset":120,  "house price":500},
              { "name":"Pentonville Road", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1200, "base_rent":80, "mortgage_value":600, "unmortgage_value":660, "house1rent":400, "house2rent":1000, "house3rent":3000, "house4rent":4500, "Hotelrent":6000, "colorset":160, "house price":500},
              { "name":"Pall Mall", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1400, "base_rent":100, "mortgage_value":700, "unmortgage_value":770, "house1rent":500, "house2rent":1500, "house3rent":4500, "house4rent":6250, "Hotelrent":7500, "colorset":200, "house price":1000},
              { "name":"White Hall", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1400, "base_rent":100, "mortgage_value":700, "unmortgage_value":770, "house1rent":500, "house2rent":1500, "house3rent":4500, "house4rent":6250, "Hotelrent":7500, "colorset":200, "house price":1000},
              { "name":"Northumberland Avenue", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1600, "base_rent":120, "mortgage_value":800, "unmortgage_value":880, "house1rent":600, "house2rent":1800, "house3rent":5000, "house4rent":7000, "Hotelrent":9000, "colorset":240, "house price":1000}
              { "name":"Bow Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1800, "base_rent":140, "mortgage_value":900, "unmortgage_value":990, "house1rent":700, "house2rent":2000, "house3rent":5500, "house4rent":7500, "Hotelrent":9500, "colorset":280, "house price":1000}
              { "name":"Marlborough Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":1800, "base_rent":140, "mortgage_value":900, "unmortgage_value":990, "house1rent":700, "house2rent":2000, "house3rent":5500, "house4rent":7500, "Hotelrent":9500, "colorset":280, "house price":1000}
              { "name":"Vine Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2000, "base_rent":160, "mortgage_value":1000, "unmortgage_value":1100, "house1rent":800, "house2rent":2200, "house3rent":6000, "house4rent":8000, "Hotelrent":10000, "colorset":320, "house price":1000}
              { "name":"Strand", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2200, "base_rent":180, "mortgage_value":1100, "unmortgage_value":1210, "house1rent":900, "house2rent":2500, "house3rent":7000, "house4rent":8750, "Hotelrent":10500, "colorset":360, "house price":1500}
              { "name":"Fleet Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2200, "base_rent":180, "mortgage_value":1100, "unmortgage_value":1210, "house1rent":900, "house2rent":2500, "house3rent":7000, "house4rent":8750, "Hotelrent":10500, "colorset":360, "house price":1500}
              { "name":"Trafalgar Square", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2400, "base_rent":200, "mortgage_value":1200, "unmortgage_value":1320, "house1rent":1000, "house2rent":3000, "house3rent":7500, "house4rent":9250, "Hotelrent":11000, "colorset":400, "house price":1500}
              { "name":"Leicester Square", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2600, "base_rent":220, "mortgage_value":1300, "unmortgage_value":1430, "house1rent":1100, "house2rent":3300, "house3rent":8000, "house4rent":9750, "Hotelrent":11500, "colorset":440, "house price":1500}
              { "name":"Coventry Street", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2600, "base_rent":220, "mortgage_value":1300, "unmortgage_value":1430, "house1rent":1100, "house2rent":3300, "house3rent":8000, "house4rent":9750, "Hotelrent":11500, "colorset":440, "house price":1500}
              { "name":"Piccaadlly", "Houses":0, "mortgaged":False, "Owner":"Nobody", "Purchase_price":2800, "base_rent":240, "mortgage_value":1400, "unmortgage_value":1540, "house1rent":1200, "house2rent":3600, "house3rent":8500, "house4rent":10250, "Hotelrent":12000, "colorset":480, "house price":1500}
                            
    ]

print(Properties[0]["name"])    
