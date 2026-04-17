import os

#os.chdir("../")

# Informazioni directory
print(f"Directory corrente: {os.getcwd()}")
print(f"Contenuto directory: {os.listdir('.')}")


# studenti_file = open("studenti.txt", "r", encoding="utf-8", newline="\n")
# lettura = studenti_file.read()
# for riga in lettura.splitlines():
#     os.mkdir(riga)


# studenti_file.close()

# os.mkdir("fatta_in_fad")  
# os.makedirs("a/b/c")  
# os.rmdir("fatta_in_fad") 

for elem in os.listdir('.'):
    print(elem)