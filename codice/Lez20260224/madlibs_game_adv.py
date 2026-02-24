""" Madlibs Game - Storia divertente """

import random as rnd

print("🎭 BENVENUTO AL GIOCO MADLIBS! 🎭")
print("Inserisci le parole richieste per creare una storia divertente!\n")

# Raccolta input
nome = ["francesca", "giovanni", "brad pitt"]
aggettivo1 = ["bella", "utile", "TOP"]
animale = ["cane", "cinghiale", "orso"]
cibo = ["pizza", "banane", "lamponi"]
numero = ["12", "3", "4"]
colore = ["verde", "giallo", "blu"]
verbo = ["correre", "camminare", "giocare"]

# Creazione della storia

with open("stories.txt", "w", encoding="utf8") as f:

    for x in range(10):

        f.write(f"------------------------Storia nr {x+1}----------------------")
        storia = f"""
        🌟 LA STORIA DI {rnd.choice(nome).upper()} 🌟

        C'era una volta {rnd.choice(nome)}, una persona molto {rnd.choice(aggettivo1)}.
        Un giorno, mentre camminava nel bosco, incontrò un {rnd.choice(animale)} {rnd.choice(colore)}.
        L'animale aveva {rnd.choice(numero)} pezzi di {rnd.choice(cibo)} e voleva {rnd.choice(verbo)}.
        {rnd.choice(nome)} decise di aiutarlo e insieme vissero felici e contenti!
        """
        
        f.write(storia)

        f.write("------------------------------------------------------")

print("Le tue storie sono pronte!")