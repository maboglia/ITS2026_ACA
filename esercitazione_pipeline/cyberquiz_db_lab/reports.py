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