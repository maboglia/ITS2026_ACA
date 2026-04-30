# Struttura del progetto

Di seguito trovi un **template pronto** (progetto completo) con file `.py` separati per una pipeline **ETL JSON → SQLite** + generazione dataset tentativi + esecuzione query/report.

Struttura consigliata:

```
cyberquiz_db_lab/
│
├── main.py
├── db.py
├── schema.sql
├── etl_questions.py
├── etl_attempts.py
├── generate_attempts.py
├── reports.py
├── utils.py
├── data/
│   ├── questions.json
│   └── attempts.json
└── cyberquiz.db
```

---

# 1) schema.sql

📄 `schema.sql`

```sql
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS attempt_answers;
DROP TABLE IF EXISTS attempts;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    difficulty INTEGER NOT NULL CHECK(difficulty BETWEEN 1 AND 5),
    question_text TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_option TEXT NOT NULL CHECK(correct_option IN ('A','B','C','D')),

    FOREIGN KEY (category_id) REFERENCES categories(id)
        ON DELETE CASCADE
);

CREATE TABLE attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    started_at TEXT NOT NULL DEFAULT (datetime('now')),
    ended_at TEXT,
    duration_seconds INTEGER NOT NULL DEFAULT 0 CHECK(duration_seconds >= 0),
    score INTEGER NOT NULL DEFAULT 0 CHECK(score >= 0),

    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
);

CREATE TABLE attempt_answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    attempt_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    user_answer TEXT NOT NULL CHECK(user_answer IN ('A','B','C','D')),
    is_correct INTEGER NOT NULL CHECK(is_correct IN (0,1)),

    FOREIGN KEY (attempt_id) REFERENCES attempts(id)
        ON DELETE CASCADE,

    FOREIGN KEY (question_id) REFERENCES questions(id)
        ON DELETE CASCADE
);

-- Trigger: aggiorna score automaticamente
DROP TRIGGER IF EXISTS trg_update_score;
CREATE TRIGGER trg_update_score
AFTER INSERT ON attempt_answers
BEGIN
    UPDATE attempts
    SET score = score + NEW.is_correct
    WHERE id = NEW.attempt_id;
END;

-- Vista statistiche utenti
DROP VIEW IF EXISTS v_user_stats;
CREATE VIEW v_user_stats AS
SELECT
    u.id AS user_id,
    u.username,
    COUNT(a.id) AS attempts_count,
    ROUND(AVG(a.score), 2) AS avg_score,
    MAX(a.score) AS best_score
FROM users u
LEFT JOIN attempts a ON a.user_id = u.id
GROUP BY u.id, u.username;
```

---

# 2) db.py

📄 `db.py`

```python
import sqlite3

DB_FILE = "cyberquiz.db"


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(schema_file="schema.sql"):
    conn = get_connection()
    with open(schema_file, "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
    conn.close()
```

---

# 3) utils.py

📄 `utils.py`

```python
import json


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def normalize_answer(ans):
    ans = ans.strip().upper()
    if ans not in ["A", "B", "C", "D"]:
        raise ValueError("Risposta non valida, deve essere A/B/C/D")
    return ans
```

---

# 4) etl_questions.py

📄 `etl_questions.py`

```python
from db import get_connection
from utils import load_json, normalize_answer


def upsert_category(conn, category_name):
    cur = conn.cursor()

    cur.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
    row = cur.fetchone()
    if row:
        return row["id"]

    cur.execute("INSERT INTO categories(name) VALUES(?)", (category_name,))
    return cur.lastrowid


def import_questions(json_file="data/questions.json"):
    data = load_json(json_file)

    conn = get_connection()
    cur = conn.cursor()

    inserted = 0

    for q in data:
        category = q["category"].strip()
        difficulty = int(q["difficulty"])
        question_text = q["question"].strip()

        if difficulty < 1 or difficulty > 5:
            raise ValueError(f"Difficulty non valida: {difficulty}")

        category_id = upsert_category(conn, category)

        correct_option = normalize_answer(q["answer"])

        options = q["options"]

        cur.execute("""
            INSERT INTO questions(
                category_id, difficulty, question_text,
                option_a, option_b, option_c, option_d,
                correct_option
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            category_id,
            difficulty,
            question_text,
            options["A"], options["B"], options["C"], options["D"],
            correct_option
        ))

        inserted += 1

    conn.commit()
    conn.close()

    print(f"[OK] Importate {inserted} domande da {json_file}")


if __name__ == "__main__":
    import_questions()
```

---

# 5) generate_attempts.py

📄 `generate_attempts.py`

Questo genera un dataset `attempts.json` realistico (utenti + tentativi + risposte).

```python
import random
from datetime import datetime, timedelta

from utils import save_json, load_json


def generate_attempts(
    questions_file="data/questions.json",
    output_file="data/attempts.json",
    users_count=10,
    attempts_count=200,
    questions_per_attempt=10
):
    questions = load_json(questions_file)

    users = [f"user{i+1}" for i in range(users_count)]
    attempts = []

    base_time = datetime.now() - timedelta(days=20)

    for attempt_id in range(1, attempts_count + 1):
        username = random.choice(users)

        start = base_time + timedelta(minutes=random.randint(0, 60 * 24 * 20))
        duration = random.randint(30, 180)  # secondi
        end = start + timedelta(seconds=duration)

        selected_questions = random.sample(questions, questions_per_attempt)

        answers = []
        score = 0

        for q in selected_questions:
            correct = q["answer"]

            # probabilità di risposta corretta dipende dalla difficulty
            diff = q["difficulty"]
            prob_correct = 0.85 - (diff * 0.12)

            if random.random() < prob_correct:
                user_answer = correct
                is_correct = 1
            else:
                user_answer = random.choice(["A", "B", "C", "D"])
                is_correct = 1 if user_answer == correct else 0

            score += is_correct

            answers.append({
                "question_id": q["id"],
                "user_answer": user_answer,
                "is_correct": is_correct
            })

        attempts.append({
            "attempt_id": attempt_id,
            "username": username,
            "started_at": start.strftime("%Y-%m-%d %H:%M:%S"),
            "ended_at": end.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_seconds": duration,
            "score": score,
            "answers": answers
        })

    save_json(output_file, attempts)
    print(f"[OK] Generato {output_file} con {attempts_count} tentativi.")


if __name__ == "__main__":
    generate_attempts()
```

---

# 6) etl_attempts.py

📄 `etl_attempts.py`

Carica attempts e risposte in DB.

```python
from db import get_connection
from utils import load_json, normalize_answer


def upsert_user(conn, username):
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    if row:
        return row["id"]

    cur.execute("INSERT INTO users(username) VALUES(?)", (username,))
    return cur.lastrowid


def import_attempts(json_file="data/attempts.json"):
    data = load_json(json_file)

    conn = get_connection()
    cur = conn.cursor()

    attempts_inserted = 0
    answers_inserted = 0

    for a in data:
        username = a["username"]
        user_id = upsert_user(conn, username)

        cur.execute("""
            INSERT INTO attempts(user_id, started_at, ended_at, duration_seconds, score)
            VALUES (?, ?, ?, ?, ?)
        """, (
            user_id,
            a["started_at"],
            a["ended_at"],
            a["duration_seconds"],
            0  # score verrà calcolato dal trigger
        ))

        attempt_db_id = cur.lastrowid
        attempts_inserted += 1

        for ans in a["answers"]:
            question_id = int(ans["question_id"])
            user_answer = normalize_answer(ans["user_answer"])
            is_correct = int(ans["is_correct"])

            cur.execute("""
                INSERT INTO attempt_answers(attempt_id, question_id, user_answer, is_correct)
                VALUES (?, ?, ?, ?)
            """, (attempt_db_id, question_id, user_answer, is_correct))

            answers_inserted += 1

    conn.commit()
    conn.close()

    print(f"[OK] Importati {attempts_inserted} tentativi")
    print(f"[OK] Importate {answers_inserted} risposte")


if __name__ == "__main__":
    import_attempts()
```

---

# 7) reports.py

📄 `reports.py`

Contiene query tipiche richieste nell’esercitazione.

```python
from db import get_connection


def show_top_users(limit=5):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT username, avg_score, best_score, attempts_count
        FROM v_user_stats
        ORDER BY avg_score DESC
        LIMIT ?
    """, (limit,))

    print("\n=== TOP USERS ===")
    for row in cur.fetchall():
        print(dict(row))

    conn.close()


def show_worst_questions(limit=10):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT q.id, q.question_text,
               ROUND((1 - AVG(aa.is_correct)) * 100, 2) AS wrong_pct
        FROM attempt_answers aa
        JOIN questions q ON aa.question_id = q.id
        GROUP BY q.id, q.question_text
        ORDER BY wrong_pct DESC
        LIMIT ?
    """, (limit,))

    print("\n=== DOMANDE PIÙ SBAGLIATE ===")
    for row in cur.fetchall():
        print(f"[{row['id']}] {row['wrong_pct']}% - {row['question_text']}")

    conn.close()


def show_category_accuracy():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name,
               ROUND(AVG(aa.is_correct) * 100, 2) AS correct_pct
        FROM attempt_answers aa
        JOIN questions q ON aa.question_id = q.id
        JOIN categories c ON q.category_id = c.id
        GROUP BY c.name
        ORDER BY correct_pct DESC
    """)

    print("\n=== ACCURACY PER CATEGORIA ===")
    for row in cur.fetchall():
        print(f"{row['name']}: {row['correct_pct']}%")

    conn.close()


if __name__ == "__main__":
    show_top_users()
    show_worst_questions()
    show_category_accuracy()
```

---

# 8) main.py

📄 `main.py`

Punto di avvio del laboratorio.

```python
from db import init_db
from etl_questions import import_questions
from generate_attempts import generate_attempts
from etl_attempts import import_attempts
import reports


def main():
    while True:
        print("\n=== CYBERQUIZ DB LAB ===")
        print("1) Inizializza Database (schema.sql)")
        print("2) Importa domande da questions.json")
        print("3) Genera attempts.json (simulazione)")
        print("4) Importa attempts.json nel DB")
        print("5) Report: Top utenti")
        print("6) Report: Domande più sbagliate")
        print("7) Report: Accuracy per categoria")
        print("0) Esci")

        choice = input("Scelta: ").strip()

        if choice == "1":
            init_db()
            print("[OK] Database inizializzato.")

        elif choice == "2":
            import_questions()

        elif choice == "3":
            generate_attempts()

        elif choice == "4":
            import_attempts()

        elif choice == "5":
            reports.show_top_users()

        elif choice == "6":
            reports.show_worst_questions()

        elif choice == "7":
            reports.show_category_accuracy()

        elif choice == "0":
            break

        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    main()
```

---

# 9) Come usare il progetto

### 1) Metti `questions.json` in `data/`

(il dataset da 50 domande che ti ho già dato)

### 2) Esegui

```bash
python main.py
```

Poi esegui nell’ordine:

1. inizializza DB
2. importa domande
3. genera attempts.json
4. importa attempts
5. lancia report

---

## Cosa hai imparato con questo progetto?

* ETL con normalizzazione
* caricamento su schema relazionale
* uso di PK/FK
* trigger e viste
* query con join e aggregazioni
* analisi dati su dataset “cyber”
