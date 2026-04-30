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