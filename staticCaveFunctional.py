import random
from termcolor import colored
print("\n-----------")

Encounters = []


Static_Mons = ["Mareep","Shinx"]
Togedemaru_Cave = ["Togedemaru"]

Route_110 = ["Shinx","Shinx","Mareep","Mareep","Mareep","Tynamo","Tynamo","Yamper","Yamper","Electrike","Electrike","Electrike"]
Granite_Cave1F =["Phanpy","Phanpy","Cufant","Cufant","Ryhorn","Ryhorn","Onix","Aron","Aron","Togedemaru","Sandile","Sandile"]

#Route 110 Calcs
while True:
    Encounter_110 = random.choices(Route_110, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1)
    if Encounter_110 in Encounters:
        Output_110 = f"\nRoute 110 is a dupe of {Encounter_110[0]}, rerolling."   
        print(colored(Output_110, 'red'))
    else:
        Encounters.insert(0, Encounter_110)
        break
print(f"Route 110 Encounter: {Encounter_110[0]}")


#Granite Cave Calcs
if Encounter_110[0] == Static_Mons[0] or Encounter_110[0] == Static_Mons[1]: #If Shinx or Mareep
    staticChance = random.choices(["Success", "Failure"])              #50/50 Static table
    print(f"Static encounter status: {staticChance[0]}")
    if staticChance[0] == "Success":                                   #If 50/50 win print Toge
        print (f"Granite Cave Encounter: {Togedemaru_Cave[0]}")
    else:
        Encounter_Granite = random.choices(Granite_Cave1F, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1)
        Encounters.insert(0, Encounter_Granite)
        print(f"Granite Cave Encounter: {Encounter_Granite[0]}")  
else:
    Encounter_Granite = random.choices(Granite_Cave1F, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1)
    Encounters.insert(0, Encounter_Granite)
    print(f"Granite Cave Encounter: {Encounter_Granite[0]}")
print("-----------\n")