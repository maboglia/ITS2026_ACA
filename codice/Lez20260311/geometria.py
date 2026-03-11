from punto import Punto
from segmento import Segmento
from triangolo import Triangolo

A = Punto(2, 2)
B = Punto(6, 2)
C = Punto(2, 5)

print(A)
print(B)
print(C)

AB = Segmento(A, B)
AC = Segmento(A, C)
BC = Segmento(B, C)

print(f"La lunghezza del segmento AB e: {AB.lunghezza()}")
print(f"La lunghezza del segmento AC e: {AC.lunghezza()}")
print(f"La lunghezza del segmento BC e: {BC.lunghezza()}")

t1 = Triangolo(A, B, C)

t2 = Triangolo(Punto(5,5), Punto(9,9), Punto(15,6))

print(t2.perimetro())
print(t2.area())
print(t2)