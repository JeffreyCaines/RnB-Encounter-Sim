import requests
import tkinter as tk
from termcolor import colored
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image

sprite_url = "https://img.pokemondb.net/sprites/home/normal/volcarona.png"

def on_calc_clicked ():
    #Display image from url
    response = requests.get(sprite_url)
    print(response.content)
    
    #processed_sprite = Image.open(BytesIO(response.content))
    #sprite_102 = ImageTk.PhotoImage(processed_sprite)
    #panel = tk.Label(window, image = sprite_102)

    sprite_data = response.content
    sprite_volc = ImageTk.PhotoImage(Image.open(BytesIO(sprite_data)))
    panel = tk.Label(window, image = sprite_volc)
    
    panel.pack()

#URL Handling
def process_pokemon_url():
    response = requests.get(sprite_url)
    sprite_data = Image.open(response.content)
    sprite_data.show()

    if response.status_code == 200:
        print(colored(f"Retrieved data {response.status_code}", 'green'))
    else:
        print(colored(f"Failed to retrieve data {response.status_code}", 'red'))
    sprite_volc = ImageTk.PhotoImage(Image.open(BytesIO(sprite_data)))
    panel = tk.Label(window, image = sprite_volc)
    
    panel.pack()


window = Tk() #Initialize a window
window.geometry("480x435")
window.title("Run and Bun Encounter Simulator")
icon = PhotoImage(file='pokeball-icon.png')
window.iconphoto(True,icon)
window.config(background="#242429")

#Calc encounters Button GUI Config
button = Button(window, text='Test')
#button.config(command=on_calc_clicked)
button.config(command=process_pokemon_url)
button.config(font=('Arial', 40, 'bold'), width = 15, height = 1)
button.config(bg='#008f99')
button.config(fg='#fffb1f')
button.config(activebackground='#00474d')
button.config(activeforeground='#800835')
button.pack()

window.mainloop()