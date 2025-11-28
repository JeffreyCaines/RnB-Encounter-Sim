import random
from termcolor import colored
i = 0

def land_route_calc():
    global i
    while True:
        current_encounter = random.choices(current_route, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1) #12 Weights
        if current_encounter[0] in encounters:
            print(colored(f"\n{current_route_string} is a dupe of {current_encounter[0]}, rerolling.", 'red'))
        else:
            encounters.insert(i, current_encounter[0])
            routes_used.insert(i, current_route[0])
            break                   
    print(f"{current_route_string} Encounter:\t   {current_encounter[0]}")

def fishing_route_calc():
    global i
    while True:
        current_encounter = random.choices(current_route, weights=(20, 20, 10, 10, 10, 10, 10, 5, 4, 1), k=1) #10 Weights
        if current_encounter[0] in encounters:
            print(colored(f"\n{current_route_string} is a dupe of {current_encounter[0]}, rerolling.", 'red'))
        else:
            encounters.insert(i, current_encounter[0])
            routes_used.insert(i, current_route[0])
            break
    print(f"{current_route_string} Encounter: {current_encounter[0]}")