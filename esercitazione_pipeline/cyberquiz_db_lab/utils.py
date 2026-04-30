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