import random

def game_guess_number():
    secret_number = random.randint(1, 100)
    print("-----------------Игра: Угадай число.----------------")
    print("Угадай число от 1 до 100.")
    attempts = 6  # количество попыток
    count_attempts = []
    print("У вас 6 попыток, чтобы угадать число от 1 до 100.")
    print(52 * "-")
    for attempt in range(1, attempts+1):
        while True:  # проверяем корректность ввода
            try:
                user_num = int(input("Введи число от 1 до 100. Попробуй угадать число: "))
                if 1 <= user_num <= 100:
                    break
                else:
                    print("Пожалуйста, введите число от 1 до 100.")
            except ValueError:
                print("Неверный ввод. Введи число от 1 до 100.")
        count_attempts += [user_num] # количество выполненных попыток
        if user_num == secret_number:
            print(*count_attempts)
            print(f"Отлично! Вы угадали число: '{secret_number}' - с '{len(count_attempts)}' попытки!")
            break
        elif user_num < secret_number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
    else:
        print(52 * "-")
        print(f"К сожалению, вы не угадали число. Загаданное число было: {secret_number}")

    print("Количество попыток:", count_attempts)

if __name__ == '__main__':
    print('Файл запущен напрямую')
    game_guess_number()