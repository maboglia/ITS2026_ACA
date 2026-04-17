import sys


print(f"Versione di Python in uso: {sys.version}")
print(f"Argomenti passati allo script: {sys.argv}")

if len(sys.argv) != 3:
    print("Uso: python copia.py file_origine file_destinazione")
    sys.exit(1)

# nome = sys.argv[1]
# eta = int(sys.argv[2])

# print(nome, eta)

source_file = sys.argv[1]
destination_file = sys.argv[2]  

print(f"File di origine: {source_file}")
print(f"File di destinazione: {destination_file}")  
print("copia in corso...")



# x = [1,2,3]
# print(sys.getsizeof(x))