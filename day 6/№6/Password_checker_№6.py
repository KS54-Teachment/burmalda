"""
Проект 3. Проверка надежности пароля.
Данные сохраняются в файл password_history.txt,
который создается в той же папке, где находится программа.
"""

from datetime import datetime
from pathlib import Path

# Путь к файлу истории рядом со скриптом
HISTORY_FILE = Path(__file__).parent / "password_history.txt"


def analyze_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Минимум 8 символов")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Добавьте строчные буквы")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Добавьте заглавные буквы")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Добавьте цифры")

    if any(c in "!@#$%^&*()-_=+[]{};:,.?/" for c in password):
        score += 1
    else:
        tips.append("Добавьте спецсимволы")

    return score, tips


def get_strength(score):
    if score <= 2:
        return "Слабый"
    elif score <= 4:
        return "Средний"
    return "Надежный"


def save_result(password, strength):
    """Сохраняет данные в текстовый файл."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.now():%Y-%m-%d %H:%M:%S} | "
            f"Пароль: {password} | Надежность: {strength}\n"
        )


def show_history():
    """Показывает историю проверок."""
    if not HISTORY_FILE.exists():
        print("История пока пуста.")
        return

    print("\n=== История проверок ===")
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        print(f.read())


def main():
    while True:
        print("\n1 - Проверить пароль")
        print("2 - Показать историю")
        print("3 - Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            password = input("Введите пароль: ").strip()

            if not password:
                print("Пароль не может быть пустым.")
                continue

            score, tips = analyze_password(password)
            strength = get_strength(score)

            print(f"\nНадежность: {strength}")
            print(f"Баллы: {score}/5")

            if tips:
                print("Рекомендации:")
                for tip in tips:
                    print("-", tip)

            save_result(password, strength)
            print(f"\nДанные сохранены в файл:\n{HISTORY_FILE}")

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод.")


if __name__ == "__main__":
    main()
