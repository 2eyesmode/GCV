from guess_number import game_guess_number
from quiz_game import quiz_game_main
from rock_paper_scissors import game_paper_scissors
from hangman import game_hangman
from text_adventure import text_quest


def main():
    while True:
        print("\\nДобро пожаловать в Game Hub!")
        print("1. Угадай число")
        print("2. Камень, ножницы, бумага")
        print("3. Викторина")
        print("4. Виселица")
        print("5. Текстовый квест")
        print("6. Сапер")
        print("7. Выход")
        choice = input("Выберите игру (1-6): ")

        if choice == "1":
            game_guess_number())
            print("")
        elif choice == "2":
            game_paper_scissors()
            print("")
        elif choice == "3":
            quiz_game_mai()
            print("")
        elif choice == "4":
            game_hangman()()
            print("")
        elif choice == "5":
            text_quest()
            print("")
        elif choice == "6":
# 6.Сапер
            print("")
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Некорректный ввод. Выберите действие от 0 до 6 из меню.")



