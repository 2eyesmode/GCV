import random

def game_hangman():
    word_list = ["обучение", "программирование", "компьютер", "профессия", "автомобиль", "крепость", "синхрофазотрон"]
    word_from_list = random.choice(word_list)   # Случайно выбранное слово из списка.
    word_from_list_letters = []                 # Список для хранения угаданных букв.
    count_attempt = 0
    max_attempt = 6
    guessed_word = ['*'] * len(word_from_list)  # Список для хранения текущего состояния угаданного слова.

    print("------------- Игра: Виселица.-------------")
    print("У вас есть 6 попыток, чтобы угадать слово.")

    while count_attempt < max_attempt:
        print_word = ''.join(guessed_word)
        print("\nТекущее состояние слова:", print_word)
        print("Неправильные попытки:", count_attempt)

        letter = input("Введите букву: ").lower()

        if len(letter) != 1 or not 'а' <= letter <= 'я':
            print("Пожалуйста, введите только одну букву.")
            continue

        if letter in word_from_list_letters:
            print("Вы уже использовали эту букву. Попробуйте другую.")
            continue

        word_from_list_letters.append(letter)

        if letter in word_from_list:
            print("Правильно!")
            for i, char in enumerate(word_from_list):
                if char == letter:
                    guessed_word[i] = letter
        else:
            count_attempt += 1
            print("Неправильно!")

        if '*' not in guessed_word:
            print("\nПоздравляю! Вы угадали слово:", word_from_list)
            break

    else:
        print("\nК сожалению, вы не угадали слово. Загаданное слово было:", word_from_list)

if __name__ == "__main__":
    game_hangman()