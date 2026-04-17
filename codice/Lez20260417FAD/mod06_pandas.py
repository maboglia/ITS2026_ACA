# per usare pandas devo installare pip install pandas

import pandas as pd
import matplotlib

df_auto = pd.read_csv("auto.csv")
df = pd.read_json("moto.json")

# print(df.tail(3))

# print(df[["Marca","Modello"]])  

# print(df.iloc[0:2, 0:2])


moto_sopra_10k = df[df["Prezzo (€)"] > 10000][["Marca", "Modello", "Prezzo (€)"]]
moto_sopra_10k.sort_values(by="Prezzo (€)", ascending=False, inplace=True)
moto_sopra_10k["IVA"] = 0.22
moto_sopra_10k["Valore_IVA"] = moto_sopra_10k["Prezzo (€)"] * moto_sopra_10k["IVA"] 
print(moto_sopra_10k)

#veicoli = pd.concat([df_auto, df])


# veicoli.to_csv('veicoli.csv', index=False)
# veicoli.to_json('veicoli.json', indent=4)
# veicoli.to_html('veicoli.html')
# veicoli.to_excel("veicoli.xlsx")

moto_sopra_10k.plot()

