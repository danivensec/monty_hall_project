import random as rand 

# Part 1: Simulating the game
def monty_game_PART_ONE (games, switch, stay): 
    
    carCount_stay = 0  #keep stack of the times it wins when it stays with the door
    carCount_switch = 0 # will keep track of when it wins when it switches
    stay_games = 0 # will keep track everytime it stays with the first choice
    switch_games =0 # will keep track of when it switches choices
   
    

    for i in range (games): 
        doors = [0,0,0] # the zero represents the goats, at the start, all the doors have a goat behind them 

        #randomly replace a goat with a car
        car = rand.randint(0,2)
        doors[car] = 1 #1 is for car 

        

        first_choice = rand.randint(0,2) # randomly choose a door
        
        #the host will open one door that is not the players first choice and does not have the car behind it
        monty_open = [x for x in range(3) if x!= first_choice and doors[x]==0] 
        monty_choice = rand.choice(monty_open)
        
        #randomly chooses if it is going to stay or switch
        switch = rand.choice([True,False])
        if switch == True: 
            stay = False
        else: 
            stay = True

        
        #operations of staying with the first door or switching
        if switch == True: #switch operation
            switch_games +=1 
            #will choose the next door, the one that was not open and the one that was not their inital choice
            switch_choice = next(x for x in range(3) if x != first_choice and x!= monty_choice)
            
            #checks if the door has the car or not
            if doors[switch_choice] == 1:
                carCount_switch += 1
            
        if stay == True: #stay operation
                stay_games+=1
                #if inital choice has the car, the car count for stay is incremented
                if doors[first_choice] == 1:
                     carCount_stay += 1  


    #probability calculations
    switch_win_probability = (carCount_switch/switch_games)*100
    stay_win_probability = (carCount_stay/stay_games)*100


    print("The results of a 10000 simulation with 3 doors (traditional Monty Hall simulation):")
    print("The probabilty of switching is ", switch_win_probability, "%")
    print("The probabilty of staying is ", stay_win_probability, "%\n")



#Part 2: Increasing the Number of doors
def monty_game_PART_TWO(games, switch, stay): 
    carCount_stay = 0  
    carCount_switch = 0 
    stay_games = 0
    switch_games =0
   
    

    for i in range (games): 
        doors = [0,0,0,0,0,0,0,0,0,0] # the zero represents the goats, at the start, all the doors have a goat behind them 

        #randomly replace a goat with a car
        car = rand.randint(0,9)
        doors[car] = 1

        

        first_choice = rand.randint(0,9)

        #will open 8 doors with goats behind them
        monty_available = [x for x in range(10) if x!= first_choice and doors[x]==0 ]
        monty_choices = rand.sample(monty_available,8)

        #track the remaining door
        remaining_door = [x for x in range (10) if x!= first_choice and x not in monty_choices]

        switch = rand.choice([True,False])
        if switch == True: 
            stay = False
        else: 
            stay = True

        if switch == True: # when the player does decide to switch to the remaing door
            switch_games+=1
            switch_choice = remaining_door[0]

            if doors[switch_choice] == 1:
                carCount_switch += 1

        if stay == True: 
                stay_games+=1
                if doors[first_choice] == 1:
                     carCount_stay += 1

    switch_win_probability = (carCount_switch/switch_games)*100
    stay_win_probability = (carCount_stay/stay_games)*100


    print("The results of a 10000 simulation with 10 doors and the host open 8 doors:")
    print("The probabilty of switching is ",switch_win_probability,"%")
    print("The probabilty of staying is ",stay_win_probability, "%\n")


#Part 3: Increasing number of door chocies
def monty_game_PART_THREE(games, switch, stay): 
    
    carCount_stay = 0 
    carCount_switch = 0
    switch_games = 0
    stay_games = 0 
    
   
    

    for i in range (games): 
        doors = [0,0,0,0,0,0,0,0,0,0] # the zero represents the goats, at the start, all the doors have a goat behind them 

        #randomly replace a goat with a car
        car = rand.randint(0,9)
        doors[car] = 1

        

        first_choice = rand.randint(0,9)

        #only one door is open
        monty_open = [x for x in range(10) if x!= first_choice and doors[x]==0]
        monty_choice = rand.choice(monty_open)

        #a list of the remaining doors is created
        remaining_doors = ([x for x in range (10) if x!= first_choice and x != monty_choice])
        

        switch = rand.choice([True,False])
        if switch == True: 
            stay = False
        else: 
            stay = True

        if switch == True:
            switch_games += 1
            switch_choice_of_door = rand.choice(remaining_doors) # will randomly choose a new door from the remaing list

            if doors[switch_choice_of_door] == 1:
                carCount_switch += 1
            
        if stay == True: 
                stay_games +=1
                if doors[first_choice] == 1:
                     carCount_stay += 1

    switch_win_probability = (carCount_switch/switch_games)*100
    stay_win_probability = (carCount_stay/stay_games)*100

    

    print("The results of a 10000 simulation with 10 doors but the host only opens one door:")
    print("The probabilty of switching is ",switch_win_probability,"%")
    print("The probabilty of staying is ",stay_win_probability,"%\n")



   
# Part 4: Imperfect Host #temp

#def monty_game_PART_FOUR(games, switch, stay):
def monty_game_PART_FOUR(games):
    carCount_stay = 0
    carCount_switch = 0
    #stay_games = 0
    #switch_games = 0

    for i in range(games):
        doors = [0, 0, 0]

        # randomly place the car
        car = rand.randint(0, 2)
        doors[car] = 1

        # player's first choice
        first_choice = rand.randint(0, 2)

        # determine if host is imperfect 
        host_imperfect = rand.random() < 0.2

        if host_imperfect:
            possible_open = [x for x in range(3) if x != first_choice]
            monty_choice = rand.choice(possible_open)

            # if the host reveals the car, that round is spoiled
            # we skip it because the normal stay/switch decision no longer happens
            #if doors[monty_choice] == 1:
              #  continue

        
        else:
            # normal Monty behavior (open always goat door)
            
            monty_open = [x for x in range(3) if x != first_choice and doors[x] == 0]
            monty_choice = rand.choice(monty_open)

        if doors[first_choice] == 1:  # stay
            carCount_stay += 1

        if doors[monty_choice] == 1: #switch 
            continue

        switch_choice = next(x for x in range(3) if x != first_choice and x != monty_choice)

        # switch strategy
        #if switch == True:
        #    switch_games += 1

        if doors[switch_choice] == 1:
             carCount_switch += 1

        # stay strategy
       # if stay == True:
        #    stay_games += 1
        #    if doors[first_choice] == 1:
        #        carCount_stay += 1


    
    switch_win_probability = (carCount_switch / games) * 100
    stay_win_probability = (carCount_stay / games) * 100


    
    print("The results of a", games, "simulation with an imperfect host:")
   # print("The probabilty of switching is ", switch_win_probability, "%")
   # print("The probabilty of staying is ", stay_win_probability, "%\n")

    print("Win rate when switching is", switch_win_probability, "%")
    print("Win rate when staying is", stay_win_probability, "%\n")



games= 10000
default_bool = None
monty_game_PART_ONE(games,default_bool, default_bool)

monty_game_PART_TWO(games,default_bool, default_bool)

monty_game_PART_THREE(games,default_bool, default_bool)

monty_game_PART_FOUR(games)


