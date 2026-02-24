def calcola_media(voti):
    totale = 0
    for voto in voti:
        totale += voto
    
    media = totale / len(voti)
    return media

media_voti = calcola_media(25, 28, 30, 19)

print(f"La media artimetica dei tuoi voti è media:{media_voti:.2f}")