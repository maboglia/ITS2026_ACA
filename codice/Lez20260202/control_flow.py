
# numero = 9
# risultato = numero > 0 and numero % 2 == 1

# print(risultato)

# if risultato:
#     print("Tutto giusto")
# else:
#     print("Tutto sbagliato")

# -----------------------------------------------------

# eta = 65

# if eta < 18:
#     print("Ingresso ridotto del 30%")
# elif eta>=65:
#     print("Ingresso ridotto del 20%")
# else:
#     print("Paghi intero!")

# -----------------------------------------------------

# numero = 70

# tipo = "Pari" if numero % 2 == 0 else "Dispari"
# print(tipo)

# if numero % 2 == 0:
#     tipo = "Pari"
# else:
#     tipo = "Dispari"
# print(tipo)

# -----------------------------------------------------

# scelta = int(input("Scegli (1-3): "))

# match scelta:
#     case 1:
#         print("Inserisci")
#     case 2:
#         print("Modifica")
#     case 3:
#         print("Elimina")
#     case _:
#         print("Scelta non valida")

import time

secret = 94


start = time.time()

for i in range(50001):
    print("Tentativo ", i)
    time.sleep(0.1)
    if i == secret:
        print(i)
        print(f"Il numero segreto è {i}")
        break

stop = time.time()
durata = stop - start

print(f"Programma terminato, l'elaborazione è durata {durata}")
