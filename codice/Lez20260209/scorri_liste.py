"""liste"""

frutti = ['mele', 'pere', 'banane', 'mandarini']

# for frutto in frutti:
#     print(f"Il frutto corrente è: {frutto} ed è di tipo {type(frutto)}")

# for i in range(len(frutti)):
#     print(f"Il {i+1}° frutto è: {frutti[i]} ed è di tipo {type(frutti[i])}")

# for i, frutto in enumerate(frutti):
#     print(f"Il {i+1}° frutto è: {frutto} ed è di tipo {type(frutto)}")

for x in enumerate(frutti):
    print(f"Il valore di x è{x} ed è di tipo {type(x)}")
