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