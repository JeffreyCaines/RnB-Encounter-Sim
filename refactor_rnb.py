import random
from termcolor import colored
from pokedex import *

def route_calc(current_route, route_string, encounter_weights, encounters, i):
    while True:
        current_encounter = random.choices(current_route, weights=encounter_weights, k=1)
        if current_encounter[0] in encounters:
            print(colored(f"\n{route_string} is a dupe of {current_encounter[0][0]}, rerolling.", 'red'))
        else:
            encounters.append(current_encounter[0])         
            print(f"{route_string:<17} {current_encounter[0][0]}")
            i += 1
            return encounters, i

def cli_output(encounters):
    print ("\n===========")
    for i in range(0, len(encounters)):
        print (encounters[i][0])
    print ("===========\n")

def main():
    route_102 = (Starly, Starly, Pidgey, Pidgey, Rookidee, Rookidee, Fletchling, Fletchling, Natu, Natu, Abra, Ralts)
    route_103 = (Gossifleur, Bounsweet, Bounsweet, Exeggcute, Budew, Seedot, Lotad, Exeggcute, Budew, Seedot, Deerling_Spring, Deerling_Summer)
    oldale_town = (Ponyta, Ponyta, Growlithe, Growlithe, Houndour, Fletchling, Sizzlipede, Houndour, Sizzlipede, Salandit, Litleo, Litleo)
    route_101 = (Lillipup, Bunnelby, Bunnelby, Buneary, Skitty, Zigzagoon_Galar, Poochyena, Starly, Pidgey, Litleo, Deerling_Spring, Deerling_Autumn)
    littleroot_town = (Surskit, Surskit, Lotad, Lotad, Finneon, Finneon, Tympole, Tympole, Tympole, Tympole)
    route_104 = (Paras, Weedle, Scatterbug, Blipbug, Sizzlipede, Ekans, Salandit, Venipede, Combee, Yanma, Ledyba, Ledyba)
    route_110 = (Shinx,Shinx,Mareep,Mareep,Mareep,Tynamo,Tynamo,Yamper,Yamper,Electrike,Electrike,Electrike)
    granite_cave1F =(Phanpy,Phanpy,Cufant,Cufant,Rhyhorn,Rhyhorn,Onix,Aron,Aron,Togedemaru,Sandile,Sandile)

    land_weights = 20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1
    fishing_weights = 20, 20, 10, 10, 10, 10, 10, 5, 4, 1

    encounters = []
    current_encounter = []
    current_route = []
    route_string = ""

    i = 0
    print ("\n=================================")
    encounters, i = route_calc(route_102, "Route 102", land_weights, encounters, i)
    encounters, i = route_calc(route_103, "Route 103", land_weights, encounters, i)
    encounters, i = route_calc(oldale_town, "Oldale Town", land_weights, encounters, i)
    encounters, i = route_calc(route_101, "Route 101", land_weights, encounters, i)
    encounters, i = route_calc(littleroot_town, "Littleroot Town", fishing_weights, encounters, i)
    encounters, i = route_calc(route_104, "Route 104", land_weights, encounters, i)
    encounters, i = route_calc(route_110, "Route 110", land_weights, encounters, i)
    encounters, i = route_calc(granite_cave1F, "Granite Cave", land_weights, encounters, i)
    print ("=================================\n")

    # cli_output(encounters)



if __name__ == "__main__":
    main()