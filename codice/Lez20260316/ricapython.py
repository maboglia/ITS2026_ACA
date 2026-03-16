

# frutta = ['mele', 'pere', 'banane']
# frutti_piccoli = ['mirtilli', 'fragole', 'ribes']

# # frutta.extend(frutti_piccoli)

# tutti_frutti = frutta + frutti_piccoli

# tupla_frutti = tuple(tutti_frutti)

# lista_frutti = list(tupla_frutti)

# print(tutti_frutti)

# print("#############TIPO##############")
# print(type(frutta))


# print("#############HELP##############")
# print(help(frutta))



#            0       1       2
frutti = ['mele', 'pere', 'banane']
verdure = ['spinaci', 'costine', 'broccoli']
dolci = ['cassatina', 'cannolo', 'meringata']

alimenti = frutti + verdure +  dolci

print (alimenti)

# for frutto in frutti:
#     print(frutto)

zippati =  zip(frutti, verdure, dolci)
# unpacking
for frutto, verdura, dolce in zippati:
    print(frutto, verdura, dolce)


# list comprehension

scatola = [alimento  for alimento in alimenti if alimento.startswith('c') ]

# for alimento in alimenti:
#     if alimento.startswith('c'):
#         scatola.append(alimento)


print(scatola)








