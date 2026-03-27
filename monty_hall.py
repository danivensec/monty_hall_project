import random as rand 

def monty_game_switch (games, switch_strategy): 
    global goatCount
    global carCount
    
    carCount = 0 
    goatCount = 0 
   

    for i in range (games): 
        doors = [0,0,0] # the zero represents the goats, at the start, all the doors have a goat behind them 

        #randomly replace a goat with a car
        car = rand.randint(0,2)
        doors[car] = 1

        first_choice = rand.randint(0,2)

        monty_open = [x for x in range(3) if x!= first_choice and doors[x]==0]

        second_choice = rand.choice(monty_open)



        if switch_strategy == True:
            third_choice = next(x for x in range(3) if x != first_choice and x!= second_choice)

            if doors[third_choice] == 1:
                carCount += 1
                
            else: 
                goatCount += 1

            

    
    switch_win_percent = (carCount/games)*100
   

    return switch_win_percent
def monty_game_stay (games, stay_strategy): 
    global goatCount
    global carCount_stay
    
    carCount_stay = 0 
    goatCount_stay = 0 
   

    for i in range (games): 
        doors = [0,0,0] # the zero represents the goats, at the start, all the doors have a goat behind them 

        #randomly replace a goat with a car
        car = rand.randint(0,2)
        doors[car] = 1

        first_choice = rand.randint(0,2)

        monty_open = [x for x in range(3) if x!= first_choice and doors[x]==0]

        second_choice = rand.choice(monty_open)



        if stay_strategy == True:

            if doors[first_choice] == 1:
                carCount_stay += 1
                
            else: 
                goatCount_stay += 1

            

    
    stay_win_percent = (carCount_stay/games)*100
   

    return stay_win_percent
    
    
    


games = 10000
switch_strategy = True
win_percent_switch = monty_game_switch(games, switch_strategy )
win_percent_stay = monty_game_stay(games, stay_strategy = True)
    
print( "won", carCount, "times")

print ( "The probability that a contestant switches the door and wins in a simulation that loops 10000 time is: ", win_percent_switch, "%")

print( "won", carCount_stay, "times")

print ( "The probability that a contestant stays with the same door and wins in a simulation that loops 10000 time is: ", win_percent_stay, "%")









