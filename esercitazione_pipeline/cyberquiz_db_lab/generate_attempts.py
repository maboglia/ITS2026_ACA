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