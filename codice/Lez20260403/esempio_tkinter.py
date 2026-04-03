import tkinter as tk
from prodotti import lista_prodotti
from PIL import ImageTk, Image
import os


counter = 0

root = tk.Tk()

root.title("Magazzino prodotti")

root.geometry("540x640")

label = tk.Label(root, text="Magazzino prodotti",  font=("Helvetica", 40))
label_prodotto = tk.Label(root, text="Magazzino prodotti",  font=("Helvetica", 22))
label_info_prodotto = tk.Label(root, text="",  font=("Helvetica", 14))

def find_next_product(): 
    global counter
    if counter == len(lista_prodotti): counter = 0
    prodotto = lista_prodotti[counter] 
    label_prodotto.config(text=f"{prodotto.nome}") 
    label_info_prodotto.config(text=f"Prezzo €{prodotto.prezzo} - ({prodotto.giacenza} pezzi)") 
    counter += 1

button = tk.Button(root, text="Scorri prodotti", font=("Helvetica", 16), command=find_next_product)

img = ImageTk.PhotoImage(Image.open("truck.jpg"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

label.pack(pady=10) 
label_prodotto.pack(pady=10) 
label_info_prodotto.pack(pady=10) 
button.pack(pady=10)

root.mainloop()