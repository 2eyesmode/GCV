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
            guess_number()
            print()
        if choice == "2":
            ssp()
            print()
        if choice == "3":
            quiz()
            print()
        if choice == "4":
            gallows()
            print()
        if choice == "5":
            text_quest()
            print()
        if choice == "6":
            sapper()
            print()

