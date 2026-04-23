# Scheda informativa – Libreria **Turtle** (Python)


## 1) Cos’è Turtle?


La libreria **turtle** è un modulo grafico di Python progettato per insegnare la programmazione in modo semplice e visivo.
Permette di disegnare sullo schermo usando una “tartaruga” (un cursore grafico) che si muove e traccia linee.


📌 È molto usata nella didattica perché aiuta a comprendere:


* coordinate e geometria
* cicli e condizioni
* funzioni
* concetti base di grafica


---


## 2) A cosa serve Turtle?


Con Turtle si possono creare:


* figure geometriche (quadrati, cerchi, triangoli)
* disegni complessi (stelle, spirali, mandala)
* semplici animazioni
* mini giochi didattici (labirinti, pong semplificato)


---


## 3) Come funziona Turtle?


La tartaruga:


* parte al centro dello schermo (coordinate 0,0)
* è orientata verso destra (0°)
* si muove avanti/indietro
* ruota a destra o sinistra
* può alzare o abbassare la penna


---


## 4) Comandi fondamentali


### Creazione ambiente


```python
import turtle
t = turtle.Turtle()
```


### Movimento


| Comando       | Descrizione                 |
| ------------- | --------------------------- |
| `forward(x)`  | avanti di x pixel           |
| `backward(x)` | indietro di x pixel         |
| `left(a)`     | ruota a sinistra di a gradi |
| `right(a)`    | ruota a destra di a gradi   |


Esempio:


```python
t.forward(100)
t.left(90)
t.forward(50)
```


---


## 5) Penna: disegnare o non disegnare


| Comando           | Descrizione                    |
| ----------------- | ------------------------------ |
| `penup()`         | solleva la penna (non disegna) |
| `pendown()`       | abbassa la penna (disegna)     |
| `pensize(n)`      | imposta lo spessore            |
| `pencolor("red")` | cambia colore linea            |


Esempio:


```python
t.pencolor("blue")
t.pensize(4)
t.forward(80)
```


---


## 6) Colori e riempimenti


| Comando               | Descrizione        |
| --------------------- | ------------------ |
| `fillcolor("yellow")` | colore riempimento |
| `begin_fill()`        | inizio riempimento |
| `end_fill()`          | fine riempimento   |


Esempio:


```python
t.fillcolor("green")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
```


---


## 7) Posizionamento con coordinate


Turtle lavora su un piano cartesiano:


* X positivo → destra
* X negativo → sinistra
* Y positivo → alto
* Y negativo → basso


| Comando      | Descrizione         |
| ------------ | ------------------- |
| `goto(x, y)` | sposta la tartaruga |
| `setx(x)`    | cambia solo x       |
| `sety(y)`    | cambia solo y       |
| `home()`     | torna al centro     |


Esempio:


```python
t.penup()
t.goto(-100, 50)
t.pendown()
t.circle(40)
```


---


## 8) Disegnare cerchi e archi


```python
t.circle(50)
```


* 50 è il raggio (pixel)
* valore negativo → cerchio verso l’altro lato


---


## 9) Velocità e animazione


| Comando        | Descrizione           |
| -------------- | --------------------- |
| `speed(n)`     | velocità da 0 a 10    |
| `hideturtle()` | nasconde la tartaruga |
| `showturtle()` | mostra la tartaruga   |


Esempio:


```python
t.speed(10)
t.hideturtle()
```


---


## 10) Scrivere testo sullo schermo


```python
t.write("Ciao!", font=("Arial", 16, "bold"))
```


---


# 11) Esempi didattici


## Esempio 1: Quadrato


```python
import turtle
t = turtle.Turtle()


for i in range(4):
    t.forward(100)
    t.left(90)


turtle.done()
```


---


## Esempio 2: Stella a 5 punte


```python
import turtle
t = turtle.Turtle()


for i in range(5):
    t.forward(150)
    t.right(144)


turtle.done()
```


---


## Esempio 3: Spirale


```python
import turtle
t = turtle.Turtle()
t.speed(0)


for i in range(100):
    t.forward(i * 2)
    t.left(20)


turtle.done()
```


---


# 12) Eventi e interazione (mouse e tastiera)


Turtle permette anche di gestire input interattivi.


### Esempio: muovere con tasti


```python
import turtle
t = turtle.Turtle()


def avanti():
    t.forward(20)


def sinistra():
    t.left(15)


def destra():
    t.right(15)


turtle.listen()
turtle.onkey(avanti, "Up")
turtle.onkey(sinistra, "Left")
turtle.onkey(destra, "Right")


turtle.done()
```


---


# 13) Funzioni utili per la didattica


| Comando            | Descrizione                                         |
| ------------------ | --------------------------------------------------- |
| `clear()`          | cancella il disegno ma mantiene la posizione        |
| `reset()`          | cancella e riporta la tartaruga allo stato iniziale |
| `bgcolor("black")` | cambia colore sfondo                                |
| `title("Disegno")` | titolo finestra                                     |


---


# 14) Errori tipici


📌 Errori frequenti:


* dimenticare `turtle.done()` (la finestra si chiude subito)
* confondere gradi e pixel
* non usare `penup()` quando si vuole spostarsi senza disegnare
* cicli infiniti che bloccano la finestra grafica


---


# 15) Punti didattici fondamentali


Turtle è perfetta per insegnare:


* **cicli** (`for`, `while`)
* **funzioni**
* **variabili**
* **coordinate cartesiane**
* **angoli e geometria**
* **eventi e input da tastiera**
* concetto di **procedura grafica**


---


# 16) Conclusione


La libreria **turtle** è uno strumento semplice ma potente per imparare la programmazione attraverso la grafica.
