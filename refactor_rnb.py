import random
from termcolor import colored
from pokedex import *

class Route:
    def __init__(self, encounters, name, weights):
        self.encounters = encounters
        self.name = name
        self.weights = weights

        # @property
        # def encounters(self):
        #     return self.__encounters

        # @property
        # def name(self):
        #     return self.__name

        # @property
        # def weights(self):
        #     return self.__weights

class Box:
    def __init__(self, name):
        self.__captures = []
        self.name = name

    @property
    def length(self):
        return len(self.__captures)

    def append(self, pokemon):
        self.__captures.append(pokemon)

    def __iter__(self):
        for pokemon in self.__captures:
            yield pokemon

    def __str__(self):
        output = f"========================= {self.name} =========================\n\n"
        for pokemon in self.__captures:
            output += f"{pokemon.name:<16}{pokemon.primary_type:<10}{pokemon.secondary_type:<10}Met: {pokemon.met_location}\n"   
        output += f"\n========================================================="
        return output


def route_calc(route, box):
    while True:
        current_encounter = random.choices(route.encounters, weights=route.weights, k=1)
        current_encounter = current_encounter[0]
        if current_encounter in box:
            print(colored(f"\n{route.name} is a dupe of {current_encounter.name}, rerolling.\n", 'red'))
        else:
            current_encounter.met_location = route.name
            box.append(current_encounter)         
            return box


def cli_output(box):
    print ("\n=========== Encounters ===========\n")
    for pokemon in box:
        print(f"{pokemon.met_location:<17} {pokemon.name}")
    print ("\n==================================\n")


def main():
    land_weights = 20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1
    fishing_weights = 20, 20, 10, 10, 10, 10, 10, 5, 4, 1
    box1 = Box("Box 1")
    route_102 = Route((Starly, Starly, Pidgey, Pidgey, Rookidee, Rookidee, Fletchling, Fletchling, Natu, Natu, Abra, Ralts),"Route 102", land_weights)
    route_103 = Route((Gossifleur, Bounsweet, Bounsweet, Exeggcute, Budew, Seedot, Lotad, Exeggcute, Budew, Seedot, Deerling_Spring, Deerling_Summer), "Route 103", land_weights)
    oldale_town = Route((Ponyta, Ponyta, Growlithe, Growlithe, Houndour, Fletchling, Sizzlipede, Houndour, Sizzlipede, Salandit, Litleo, Litleo), "Oldale Town", land_weights)
    route_101 = Route((Lillipup, Bunnelby, Bunnelby, Buneary, Skitty, Zigzagoon_Galar, Poochyena, Starly, Pidgey, Litleo, Deerling_Spring, Deerling_Autumn), "Route 101", land_weights)
    littleroot_town = Route((Surskit, Surskit, Lotad, Lotad, Finneon, Finneon, Tympole, Tympole, Tympole, Tympole), "Littleroot Town", fishing_weights)
    route_104 = Route((Paras, Weedle, Scatterbug, Blipbug, Sizzlipede, Ekans, Salandit, Venipede, Combee, Yanma, Ledyba, Ledyba), "Route 104", land_weights)
    route_110 = Route((Shinx,Shinx,Mareep,Mareep,Mareep,Tynamo,Tynamo,Yamper,Yamper,Electrike,Electrike,Electrike), "Route 110", land_weights)
    granite_cave1F = Route((Phanpy,Phanpy,Cufant,Cufant,Rhyhorn,Rhyhorn,Onix,Aron,Aron,Togedemaru,Sandile,Sandile), "Granite Cave 1F", land_weights)

    route_calc(route_102, box1)
    route_calc(route_103, box1)
    route_calc(oldale_town, box1)
    route_calc(route_101, box1)
    route_calc(littleroot_town, box1)
    route_calc(route_104, box1)
    route_calc(route_110, box1)
    route_calc(granite_cave1F, box1)

    cli_output(box1)
    print(box1)


if __name__ == "__main__":
    main()
