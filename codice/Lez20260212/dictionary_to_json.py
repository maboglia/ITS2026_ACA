""" Dictionary to JSON"""

import json

menu = {
    "pizza" : 2.5,
    "panino": 4.0,
    "bibita": 2.5,
    "acqua" : 1.0,
    "caffé" : 1.3
}

with open("scontrino.json", "w", encoding='utf8') as f:
    json.dump(menu, f,  indent=4, ensure_ascii=False  )
