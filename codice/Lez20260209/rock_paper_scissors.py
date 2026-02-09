
import random

simboli = ['rock', 'paper', 'scissors']

macchina = random.choice(simboli)

umano = input(f"Umano! Scegli tra {simboli} ")

print(f"La macchina ha scelto {macchina}")
print(f"L'umano ha scelto {umano}")

