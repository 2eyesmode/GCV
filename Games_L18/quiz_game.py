def quiz_game_main():
    dict_capital = [
        ("Столица Франции?", ["Лондон", "Берлин", "Париж"], 3),
        ("Столица Германии?", ["Лондон", "Берлин", "Венеция"], 2),
        ("Столица США?", ["Нью-Йорк", "Лос-Анджелес", "Вашингтон"], 3),
        ("Столица Греции?", ["Афины", "Стамбул", "Киев"], 1),
        ("Столица Норвегии?", ["Осло", "Порту", "Мюнхен"], 1)
    ]

    correct_answers = 0
    print("----- Игра: Викторина. -----")

    for question_country, list_city, correct_answer in dict_capital:
        while True:
            print(question_country)
            print(28 * "-")
            for num, city in enumerate(list_city, start=1):
                print(f"{num}. {city}")
            try:
                print(28 * "-")
                user_answer = int(input("Введите вариант ответа: "))
                print(28 * "-")
                if 1 <= user_answer <= len(list_city):
                    if user_answer == correct_answer:
                        print("Ответ правильный.\n")
                        correct_answers += 1
                        break
                    else:
                        print("Ответ неправильный.\n")
                        break
                else:
                    print("Неверный ввод. Выберите число от 1 до", len(list_city), "\n")
            except ValueError:
                print("Неверный ввод. Введите число.\n")

    print(f"Игра завершена. Вы дали {correct_answers} правильных ответа из 5.")

if __name__ == "__main__":
    print('Файл запущен напрямую')
    quiz_game()