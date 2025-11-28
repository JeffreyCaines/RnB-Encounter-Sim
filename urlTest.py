import requests
import tkinter as tk
from termcolor import colored
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image

base_url = "https://img.pokemondb.net/sprites/home/normal/"
encounters = ["Fletchling"]#, "Natu"]

#URL Handling
def process_pokemon_url():
    for i in range(0, len(encounters)):
        url = f"{base_url}{encounters[i]}.png".lower()
        print(url)
        response = requests.get(url)
        print(response.)
        if response.status_code == 200:
            print(colored(f"Retrieved data {response.status_code}", 'green'))
        else:
            print(colored(f"Failed to retrieve data {response.status_code}", 'red'))

process_pokemon_url()

window = Tk() #Initialize a window
window.geometry("480x600")
window.title("Run and Bun Encounter Sprite Test")
icon = PhotoImage(file='pokeball-icon.png')
window.iconphoto(True,icon)
window.config(background="#242429")

label = Label(window, image = pokemon_sprite)
pokemon_sprite = ImageTk.PhotoImage(processed_sprite)
label.pack()

window.mainloop()