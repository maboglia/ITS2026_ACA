
# # esegui la prima istruzione
# print("1 iscriversi alla selezione del corso")

# # esegui la seconda istruzione
# print("2 partecipare alla selezione")

# print("3 superare la selezione")

# if True:
#     print("Hai superato la selezione")
#     print("4 presentarsi in aula")
# else:
#     print("Non hai superato la selezione")
#     print("4 sei libero")


# counter = 0

# while 5 > 4:
#     counter = counter + 1
#     print("evviva", counter)
    
#     if counter == 50:
#         break


nome = input("Come ti chiami?")

anno_di_nascita = input("in che anno sei nato")

print(type(anno_di_nascita))

eta = 2026 - int(anno_di_nascita)

print("La tua età è: ", eta)

for carattere in nome:
    print(carattere, end="")
