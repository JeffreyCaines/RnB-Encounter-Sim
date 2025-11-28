from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import random
from termcolor import colored
import requests
from io import BytesIO


#define route urls here and modify them within the on_calc_clicked method



base_url = "https://img.pokemondb.net/sprites/home/normal/"
url_102 = ""
url_dbg = "https://img.pokemondb.net/sprites/home/normal/bounsweet.png"
Encounters = []
index_102 = [0]




window = Tk() #Initialize a window
window.geometry("480x435")
window.title("Run and Bun Encounter Simulator")
icon = PhotoImage(file='pokeball-icon.png')
window.iconphoto(True,icon)
window.config(background="#242429")
'''
response = requests.get(url_dbg)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = tk.Label(window, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
'''

Route_102 = (["starly", "starly", "pidgey", "pidgey", "rookidee", "rookidee",
            "fletchling", "fletchling", "natu", "natu", "abra", "ralts"])

def on_calc_clicked ():
    #Route 102
    while True:
        Random_102 = random.choices(Route_102, weights=(20, 10, 10, 10, 10, 10, 10, 5, 5, 5, 4, 1), k=1)
        if Random_102 in Encounters:
            Output_102 = f"\nRoute 102 is a dupe of {Random_102}, rerolling."
            print(colored(Output_102, 'red'))
        else:
            Encounters.insert(0, Random_102)
            break

    Result_102 = f"Route 102 Encounter: {Random_102}"
    print(Result_102)
    route102Label['text'] = f"Route 102 Encounter: {Random_102}"




    def get_pokemon_sprite():
        url = f"{base_url}{"".join(Random_102)}.png" #converts from list entry to string with no formatting?      
        url_102 = url
        print(url_102)
        pokemon_name = [Encounters[i] for i in index_102]
        pokemon_info = get_pokemon_sprite(Random_102)
 


    response = requests.get(url_102)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    panel = tk.Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")


Encounters.clear()










#Calc Encounters Button GUI Config
button = Button(window, text='Calc Encounters')
button.config(command=on_calc_clicked)
button.config(font=('Arial', 40, 'bold'), width = 15, height = 1)
button.config(bg='#008f99')
button.config(fg='#fffb1f')
button.config(activebackground='#00474d')
button.config(activeforeground='#800835')
button.pack()

#Route 102 GUI Output Config
route102Label = Label(text='')
route102Label.config(font=('Arial', 15, 'bold'), width = 40, height = 2, anchor = "w")
route102Label.pack()






window.mainloop()