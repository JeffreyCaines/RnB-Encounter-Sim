import random
import requests
import tkinter as tk
from tkinter import *
from io import BytesIO
from termcolor import colored
from PIL import ImageTk, Image
from pokedex import *
#from route_calcs import *

#Initialize variables, tuples, & lists
base_url = "https://img.pokemondb.net/sprites/home/normal/"
static = (Mareep, Electrike)
togedemaru_cave = (Togedemaru)
route_102 = (Starly, Starly, Pidgey, Pidgey, Rookidee, Rookidee, Fletchling, Fletchling, Natu, Natu, Abra, Ralts)
route_103 = (Gossifleur, Bounsweet, Bounsweet, Exeggcute, Budew, Seedot, Lotad, Exeggcute, Budew, Seedot, Deerling_Spring, Deerling_Summer)
oldale_town = (Ponyta, Ponyta, Growlithe, Growlithe, Houndour, Fletchling, Sizzlipede, Houndour, Sizzlipede, Salandit, Litleo, Litleo)
route_101 = (Lillipup, Bunnelby, Bunnelby, Buneary, Skitty, Zigzagoon_Galar, Poochyena, Starly, Pidgey, Litleo, Deerling_Spring, Deerling_Autumn)
littleroot_town = (Surskit, Surskit, Lotad, Lotad, Finneon, Finneon, Tympole, Tympole, Tympole, Tympole)
route_104 = (Paras, Weedle, Scatterbug, Blipbug, Sizzlipede, Ekans, Salandit, Venipede, Combee, Yanma, Ledyba, Ledyba)
route_110 = (Shinx,Shinx,Mareep,Mareep,Mareep,Tynamo,Tynamo,Yamper,Yamper,Electrike,Electrike,Electrike)
granite_cave1F =(Phanpy,Phanpy,Cufant,Cufant,Rhyhorn,Rhyhorn,Onix,Aron,Aron,Togedemaru,Sandile,Sandile)

static_table = []
magnet_pull_table = []

land_weights = 20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1 # 12 Weights
fishing_weights = 20, 20, 10, 10, 10, 10, 10, 5, 4, 1    # 10 Weights

encounters = []
current_encounter = []
encounter_110 = []
current_route = []
current_route_string = ""
i = 0

#Ask the user for their attempt count
attempts = int(input(" __| |_______________________________| |__\n(__   _______________________________   __)\n   | |                               | |\n   | |  What is your attempt count?  | |\n __| |_______________________________| |__\n(__   _______________________________   __)\n   | |                               | |\n                  "))
print()

def route_calc(current_route, current_route_string, encounter_weights):
    while True:
        current_encounter = random.choices(current_route, weights=encounter_weights, k=1)
        if current_encounter[0] in encounters:
            print(colored(f"\n{current_route_string} is a dupe of {current_encounter[0][0]}, rerolling.", 'red'))
        else:
            encounters.append(current_encounter[0])
            # routes_used.append(current_route[0])
            if current_route == littleroot_town:
                print(f"{current_route_string} Encounter: {current_encounter[0][0]}")
                break
            else:                
                print(f"{current_route_string} Encounter:\t   {current_encounter[0][0]}")
                break

def calc_103(i):
    route_calc(route_103, "Route 103", land_weights)
    route_103_Label['text'] = f"\nRoute 103 Encounter:             {encounters[i][0]}"
    clear_special_tables()
    i += 1
    return i

def calc_102(i):
    route_calc(route_102, "Route 102", land_weights)
    route_102_Label['text'] = f"\nRoute 102 Encounter:             {encounters[i][0]}"
    clear_special_tables()
    i += 1
    return i

def calc_oldale(i):
    route_calc(oldale_town, "Oldale Town", land_weights)
    oldale_town_Label['text'] = f"\nOldale Town Encounter:         {encounters[i][0]}"
    clear_special_tables()
    i += 1
    return i

def calc_101(i):
    route_calc(route_101, "Route 101", land_weights)
    route_101_Label['text'] = f"\nRoute 101 Encounter:             {encounters[i][0]}"
    clear_special_tables()
    i += 1
    return i

def calc_littleroot(i):
    route_calc(littleroot_town, "Littleroot Town", fishing_weights)
    littleroot_town_Label['text'] = f"\nLittleroot Town Encounter:     {encounters[i][0]}"
    clear_special_tables()
    i += 1
    return i

def calc_104(i):
    route_calc(route_104, "Route 104", land_weights)
    route_104_Label['text'] = f"\nRoute 104 Encounter:             {encounters[i][0]}"
    clear_special_tables()
    i += 1
    return i

#Only route semi reworked for static and magnet pull
def calc_110(i):
    if static_chance == True:
        safe_get(encounters, "Electric")
        route_calc(static_table, "Route 110", dynamic_weights)
    if magnet_pull_chance == True:
        safe_get(encounters, "Electric")
        route_calc(static_table, "Route 110", dynamic_weights)
    route_calc(route_110, "Route 110", land_weights)
    route_110_Label['text'] = f"\nRoute 110 Encounter:             {encounters[i][0]}"
    clear_special_tables()
    i += 1
    return i

def is_static_present():
    if static[0] in encounters or static[1] in encounters:
        return True
    else:
        return False

def calc_static():
    use_static_table = random.choices([True, False])   #50/50 Static table
    print(f"Static encounter status:   {use_static_table[0]}")
    static_Label['text'] = f"\nStatic encounter status:         {use_static_table[0]}"
    return use_static_table

def calc_granite(i, static_presence):
    if len(encounter_110) == 0: #If no route 110 encounter roll normal table
            route_calc(granite_cave1F, "Granite Cave", land_weights)
            print(f"Static encounter status:   N/A")
            print(f"Granite Cave Encounter:    {encounters[i][0]}")
            static_Label['text'] = f"\nStatic encounter status:         N/A"   
            # granite_cave1F_Label['text'] = f"\nGranite Cave Encounter:       {encounter_granite[0]}"
            i += 1
            return i

    elif static_presence == True: #If Shinx or Mareep is encountered on 110 roll 50/50 for static vs normal table
        use_static_table = random.choices(["Success", "Failure"])                    #50/50 Static table
        print(f"Static encounter status:   {use_static_table[0]}")
        static_Label['text'] = f"\nStatic encounter status:         {use_static_table[0]}"
        if use_static_table == "Success":
            encounters.append(togedemaru_cave[0])
            print (f"Granite Cave Encounter:    {togedemaru_cave[0]}")
            static_Label['text'] = f"\nStatic encounter status:         {use_static_table[0]}"
            granite_cave1F_Label['text'] = f"\nGranite Cave Encounter:        {togedemaru_cave[0]}"
            i += 1
            return i
        else:
            route_calc(granite_cave1F, "Granite Cave", land_weights)
            print(f"Granite Cave Encounter:    {encounters[i][0]}")
            static_Label['text'] = f"\nStatic encounter status:         {use_static_table[0]}"   
            granite_cave1F_Label['text'] = f"\nGranite Cave Encounter:        {encounters[i][0]}"
            i += 1
            return i 
    else:
        route_calc(granite_cave1F, "Granite Cave", land_weights)
        print(f"Static encounter status:   N/A")
        print(f"Granite Cave Encounter:    {encounters[i][0]}")
        static_Label['text'] = f"\nStatic encounter status:         N/A"   
        granite_cave1F_Label['text'] = f"\nGranite Cave Encounter:        {encounters[i][0]}"
        i += 1
        return i 



    #route_calc(current_route, current_route_string, encounter_weights)
    #granite_cave1F_Label['text'] = f"\nGranite Cave Encounter:             {encounters[i][0]}"
    #i += 1
    #return i

def safe_get(encounters, affected_type, default=None):
    try:
        for encounter in encounters:
            if encounter[1] == affected_type or encounter[2] == affected_type:
                print(f"{affected_type} mon present")
                if affected_type == "Electric":
                    static_table.append(encounter)
                elif affected_type == "Steel":
                    magnet_pull_table.append(encounter)
        return affected_type
    except IndexError:
        return default

def overworld_ability_coinflip(overworld_ability):
    overworld_ability_chance = bool(getrandbits(1))
    print(f"{overworld_ability} active: {overworld_ability_chance}")
    return overworld_ability_chance

def process_pokemon_url():
    print("\nURL processing ran")
    for i in range(0, len(encounters)):
        url = f"{base_url}{encounters[i][0]}.png".lower()
        print(url)
        response = requests.get(url)
        sprite_data = response.content
        sprite = ImageTk.PhotoImage(Image.open(BytesIO(sprite_data)))
        #root = tk.Tk()
        #Panel = tk.Label(root, image=sprite)
        #Panel.pack(side="bottom", fill="both", expand="yes")
        #root.mainloop()

        if response.status_code == 200:
            print(colored(f"Retrieved data {response.status_code}", 'green'))
        else:
            print(colored(f"Failed to retrieve data {response.status_code}", 'red'))

def cli_output():
    print ("\n===========")
    for i in range(0, len(encounters)):
        print (encounters[i][0])
    print ("===========\n")

def clear_special_tables():
    static_table.clear()
    magnet_pull_table.clear()

def clear_encounters():
    encounters.clear()
    encounter_110.clear()

#Ran upon UI button press
def on_calc_clicked():
    global attempts
    attempts += 1
    i = 0
    print(f"Attempt: {attempts}\n______________________________________")


    ##################################################
    #Select routes to simulate
    #Feature creep: 
    #Toggle routes from within the UI
    #Store attempt count in a file and pull it's value
    ##################################################
    clear_encounters()
    i = calc_103(i)
    i = calc_102(i)
    i = calc_oldale(i)
    i = calc_101(i)
    i = calc_littleroot(i)
    i = calc_104(i)
    #i = calc_110(i)
    static_presence = is_static_present()
    i = calc_granite(i, static_presence)
    ##################################################
    #overworld_ability_coinflip()
    #static_chance = overworld_ability_coinflip("Static")
    #magnet_pull_chance = overworld_ability_coinflip("Magnet Pull")
    safe_get(current_route, "Electric")
    safe_get(current_route, "Steel")

    #process_pokemon_url()
    cli_output()
    #gui_output()
    ##################################################


window = Tk() #Initialize a window
window.geometry("480x600")
window.title("Run and Bun Encounter Simulator")
icon = PhotoImage(file='pokeball-icon.png')
window.iconphoto(True,icon)
#window.config(bg=PhotoImage(file='Box_Forest_E.png'))

#Calc encounters Button GUI Config
button = Button(window, text='Calc encounters')
button.config(command=on_calc_clicked)
button.config(font=('Arial', 40, 'bold'), width = 15, height = 1)
button.config(bg='#008f99')
button.config(fg='#fffb1f')
button.config(activebackground='#00474d')
button.config(activeforeground='#800835')
button.pack()

#Route 103 GUI Output Config
route_103_Label = Label(text='')
route_103_Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w", bg="#242429", fg='#ff0b1f')
route_103_Label.pack()

#Route 102 GUI Output Config
route_102_Label = Label(text='')
route_102_Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w", bg="#242429", fg='#ff0b1f')
route_102_Label.pack()

#Oldale Town GUI Output Config
oldale_town_Label = Label(text='')
oldale_town_Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w", bg="#242429", fg='#ff0b1f')
oldale_town_Label.pack()

#Route 101 GUI Output Config
route_101_Label = Label(text='')
route_101_Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w", bg="#242429", fg='#ff0b1f')
route_101_Label.pack()

#Littleroot Town GUI Output Config
littleroot_town_Label = Label(text='')
littleroot_town_Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w", bg="#242429", fg='#ff0b1f')
littleroot_town_Label.pack()
#img = PhotoImage(pokemon_sprite)
#littlerootLabel.pack()

#Route 104 GUI Output Config
route_104_Label = Label(text='')
route_104_Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w", bg="#242429", fg='#ff0b1f')
route_104_Label.pack()

#Route 110 GUI Output Config
route_110_Label = Label(text='')
route_110_Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w", bg="#242429", fg='#ff0b1f')
route_110_Label.pack()

#Static Chance GUI Output Config
static_Label = Label(text='')
static_Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w", bg="#242429", fg='#ff0b1f')
static_Label.pack()

#Granite Cave GUI Output Config
granite_cave1F_Label = Label(text='')
granite_cave1F_Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w", bg="#242429", fg='#ff0b1f')
granite_cave1F_Label.pack()

window.mainloop()