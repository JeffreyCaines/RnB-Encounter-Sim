import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO

def lotad(): 
    root = tk.Tk()
    root.geometry("600x600")
    url = "https://img.pokemondb.net/sprites/home/normal/lotad.png"
    response = requests.get(url)
    sprite_data = response.content
    sprite = ImageTk.PhotoImage(Image.open(BytesIO(sprite_data)))
    panel = tk.Label(root, image=sprite)
    panel.pack(side="bottom", fill="both", expand="yes")

    url2 = "https://img.pokemondb.net/sprites/home/normal/lombre.png"
    response2 = requests.get(url2)
    sprite_data2 = response2.content
    sprite2 = ImageTk.PhotoImage(Image.open(BytesIO(sprite_data2)))
    lombrePanel = tk.Label(root, image=sprite2)
    lombrePanel.pack(side="bottom", fill="both", expand="yes")

    root.mainloop()

def pc_box():
    im = Image.open("Box_Forest_E.png")
    root = tk.Tk()
    root.geometry("156x141")
    newsize = (468, 423)
    resized_im = im.resize(newsize)
    label1 = tk.Label(root, image = resized_im)
    label1.place(x = 0, y = 0)
    root.mainloop()

########
#lotad()
pc_box()
########