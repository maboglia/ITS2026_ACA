""" number guessing game """

import random

def number_guessing_game():
    print("🔢 GIOCO INDOVINA IL NUMERO 🔢")

    # 1. Genera il numero segreto
    limite_inferiore = 1
    limite_superiore = 100
    numero_segreto = random.randint(limite_inferiore, limite_superiore)

    tentativi = 0
    indovinato = False

    print(f"Ho pensato a un numero tra {limite_inferiore} e {limite_superiore}.")

    # 2. Ciclo principale del gioco
    while not indovinato:
        try:
            tentativo_utente = int(input("Indovina il numero: "))
            tentativi += 1

            if tentativo_utente < limite_inferiore or tentativo_utente > limite_superiore:
                print(f"Per favore, inserisci un numero tra {limite_inferiore} e {limite_superiore}.")
                continue

            # 3. Controllo del numero e suggerimenti
            if tentativo_utente < numero_segreto:
                print("⬆️ Troppo basso! Riprova.")
            elif tentativo_utente > numero_segreto:
                print("⬇️ Troppo alto! Riprova.")
            else:
                indovinato = True
                print("\n" + "="*40)
                print(f"🎉 COMPLIMENTI! Hai indovinato il numero {numero_segreto}!")
                print(f"Hai impiegato {tentativi} tentativi.")
                print("="*40)

        except ValueError:
            print("❌ Devi inserire un numero intero valido.")

number_guessing_game()