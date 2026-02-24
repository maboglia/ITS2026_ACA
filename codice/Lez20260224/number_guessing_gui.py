import tkinter as tk
from tkinter import messagebox
import random

# Variabili globali
numero_segreto = random.randint(1, 100)
tentativi = 0

# Funzione controllo
def controlla():
    global tentativi

    try:
        guess = int(entry.get())
        tentativi += 1
        label_tentativi.config(text=f"Tentativi: {tentativi}")

        if guess < numero_segreto:
            label_feedback.config(text="Troppo basso!")
        elif guess > numero_segreto:
            label_feedback.config(text="Troppo alto!")
        else:
            messagebox.showinfo("Bravo!", f"Hai indovinato in {tentativi} tentativi!")
            nuova_partita()

    except ValueError:
        messagebox.showerror("Errore", "Inserisci un numero valido")

# Reset partita
def nuova_partita():
    global numero_segreto, tentativi
    numero_segreto = random.randint(1, 100)
    tentativi = 0
    label_feedback.config(text="")
    label_tentativi.config(text="Tentativi: 0")
    entry.delete(0, tk.END)

# GUI
root = tk.Tk() # creo un oggetto di tipo GUI
root.title("Guessing Game base") # titolo
root.geometry("300x200") # dimensioni width x height in pixel

label_title = tk.Label(root, text="Indovina il numero (1-100)") # creo nuova Label
label_title.pack(pady=10) # aggiungo la label alla GUI

entry = tk.Entry(root) # testo editabile
entry.pack() # aggiungo alla GUI

btn = tk.Button(root, text="Indovina", command=controlla) # creo un button con testo e azione
btn.pack(pady=5) # aggiungo alla GUI

label_feedback = tk.Label(root, text="") # creo nuova Label
label_feedback.pack() # aggiungo alla GUI

label_tentativi = tk.Label(root, text="Tentativi: 0") # creo nuova Label
label_tentativi.pack() # aggiungo alla GUI

btn_reset = tk.Button(root, text="Nuova partita", command=nuova_partita) # creo un button con testo e azione
btn_reset.pack(pady=5) # aggiungo alla GUI

root.mainloop() # faccio partire il loop