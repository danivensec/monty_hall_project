import random as rand 

def monty_game_switch (games, switch, stay): 
    global goatCount
    global carCount
    global goatCount_stay
    global carCount_stay
    
   
    carCount_stay = 0 
    goatCount_stay = 0 
    carCount = 0 
    goatCount = 0 
   
    


    for i in range (games): 
        doors = [0,0,0] # the zero represents the goats, at the start, all the doors have a goat behind them 

        #randomly replace a goat with a car
        car = rand.randint(0,2)
        doors[car] = 1

        

        first_choice = rand.randint(0,2)

        monty_open = [x for x in range(3) if x!= first_choice and doors[x]==0]

        monty_choice = rand.choice(monty_open)

        switch = rand.choice([True,False])
        if switch == True: 
            stay = False
        else: 
            stay = True

        if switch == True:
            third_choice = next(x for x in range(3) if x != first_choice and x!= monty_choice)

            if doors[third_choice] == 1:
                carCount += 1
                
            else: 
                goatCount += 1
        if stay == True: 
                if doors[first_choice] == 1:
                     carCount_stay += 1
                
                else: 
                     goatCount_stay += 1
    
    switch_win_probability = (carCount/games)*100
    stay_win_probability = (carCount_stay/games)*100

    print( "won", carCount, "times")

    print ( "The probability that a contestant switches the door and wins in a simulation that loops 10000 time is: ", switch_win_probability, "%")

    print( "won", carCount_stay, "times")

    print ( "The probability that a contestant stays with the same door and wins in a simulation that loops 10000 time is: ", stay_win_probability, "%")


games= 10000

monty_game_switch(games,None, None)
