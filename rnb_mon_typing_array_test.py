#main file to fix
#Figure out logic for determining if there is a mon with static/manget pull and the logic for if the mon is affected by the ability

from random import choices, getrandbits
from termcolor import colored
from pokedex import *
from pokedex import *
from pokedex import *

granite_cave1F =(Phanpy,Phanpy,Cufant,Cufant,Rhyhorn,Rhyhorn,Onix,Aron,Aron,Togedemaru,Sandile,Sandile)

land_weights = 20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1

encounters = []
current_encounter = []
encounter_110 = []
current_route = []
current_route_string = ""

def overworld_ability_coinflip(overworld_ability):
    overworld_ability_chance = bool(getrandbits(1))
    print(f"{overworld_ability} active: {overworld_ability_chance}")
    return overworld_ability_chance

def calc_granite(static_chance, magnet_pull_chance):
    if static_chance == True:
        print("Static worked")
        route_calc(granite_cave1F, "Granite Cave", land_weights)
    if magnet_pull_chance == True:
        print("Magnet Pull worked")
        route_calc(granite_cave1F, "Granite Cave", land_weights)
    else:
        route_calc(granite_cave1F, "Granite Cave", land_weights)

def route_calc(current_route, current_route_string, encounter_weights):
    while True:
        current_encounter = choices(current_route, weights=encounter_weights, k=1)
        if current_encounter[0] in encounters:
            print(colored(f"\n{current_route_string} is a dupe of {current_encounter[0][0]}, rerolling.", 'red'))
        else:
            encounters.append(current_encounter[0])                  
            print(f"{current_route_string} Encounter:\t   {current_encounter[0][0]}")
            break

def safe_get(encounters, affected_type, default=None):
    try:
        for encounter in encounters:
            if encounter[1] == affected_type or encounter[2] == affected_type:
                print(f"{affected_type} mon present")
                return True
    except IndexError:
        return default

def main():
    static_chance = overworld_ability_coinflip("Static")
    magnet_pull_chance = overworld_ability_coinflip("Magnet Pull")
    calc_granite(static_chance, magnet_pull_chance)

    safe_get(current_route, "Electric")
    safe_get(current_route, "Steel")
    # 
    calc_granite(static_chance, magnet_pull_chance)

if __name__ == "__main__":
    main()