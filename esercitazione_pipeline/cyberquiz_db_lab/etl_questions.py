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