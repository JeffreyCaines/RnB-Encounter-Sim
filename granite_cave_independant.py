#Encounter insert handling is out of date and hardcoded
#Route 110 Calcs
    def calc_110():
        while True:
            encounter_110 = random.choices(route_110, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1)
            if encounter_110[0] in encounters:
                print(colored(f"\nRoute 110 is a dupe of {encounter_110[0]}, rerolling.", 'red'))
            else:
                encounters.insert(7, encounter_110[0])
                break
        print(f"Route 110 Encounter:\t   {encounter_110[0]}")
        route110Label['text'] = f"\nRoute 110 Encounter: {encounter_110[0]}"


    #Granite Cave Independancy Test
    def granite_test():
        if encounter_110 == []:
            print("No route 110 encounter detected")
            encounter_granite = random.choices(granite_cave1F, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1)
            encounters.insert(8, encounter_granite[0])
            print(f"Granite Cave Encounter:    {encounter_granite[0]}")
            graniteLabel['text'] = f"\nGranite Cave Encounter: {encounter_granite[0]}"

        elif encounter_110[0] == static_mons[0] or encounter_110[0] == static[1]: #Mareep or Electrike
            print("Simulating Static")
            staticChance = random.choices(["Success", "Failure"])                    #50/50 Static table
            staticLabel['text'] = f"Static encounter status: {staticChance[0]}"
            print(f"Static encounter status:   {staticChance[0]}")
            if staticChance[0] == "Success":
                encounters.insert(8, togedemaru_cave[0])
                print (f"Granite Cave Encounter:    {togedemaru_cave[0]}")
                graniteLabel['text'] = f"\nGranite Cave Encounter: {togedemaru_cave[0]}"
            else:
                print("Static failed, using normal table")
                encounter_granite = random.choices(granite_cave1F, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1)
                encounters.insert(8, encounter_granite[0])
                print(f"Granite Cave Encounter:    {encounter_granite[0]}")
                graniteLabel['text'] = f"\nGranite Cave Encounter: {encounter_granite[0]}"


    #Granite Cave Calcs
    def calc_granite():
        if encounter_110[0] == "":
            if encounter_110[0] == static_mons[0] or encounter_110[0] == static[1]: #Mareep or Electrike
                staticChance = random.choices(["Success", "Failure"])                    #50/50 Static table
                staticLabel['text'] = f"Static encounter status: {staticChance[0]}"
                print(f"Static encounter status:   {staticChance[0]}")
                if staticChance[0] == "Success":
                    encounters.insert(8, togedemaru_cave[0])
                    print (f"Granite Cave Encounter:    {togedemaru_cave[0]}")
                    graniteLabel['text'] = f"\nGranite Cave Encounter: {togedemaru_cave[0]}"
                else:
                    encounter_granite = random.choices(granite_cave1F, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1)
                    encounters.insert(8, encounter_granite[0])
                    print(f"Granite Cave Encounter:    {encounter_granite[0]}")
                    graniteLabel['text'] = f"\nGranite Cave Encounter: {encounter_granite[0]}"  
        else:
            encounter_granite = random.choices(granite_cave1F, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1)
            encounters.insert(8, encounter_granite[0])
            print(f"Granite Cave Encounter:    {encounter_granite[0]}")
            graniteLabel['text'] = f"\nGranite Cave Encounter: {encounter_granite[0]}"