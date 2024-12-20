def text_quest():
    print(77 * "-")
    print("Игра: Текстовый квест.")
    print(77 * "-")
    print("Вы просыпаетесь в темной комнате замка. Перед вами две двери: левая и правая.")

    choice = input("Выберите действие (1 - Левая дверь, 2 - Правая дверь): ")

    if choice == "1":
        print(77 * "-")
        print("Вы входите в левую комнату и видите старинный сундук.")
        choice = input("Выберите действие (1 - Открыть сундук, 2 - Не открывать сундук и выйти): ")

        if choice == "1":
            print(77 * "-")
            print("В сундуке оказывается карта с указанием выхода из замка.")
            choice = input("Выберите действие (1 - Следовать по карте, 2 - Игнорировать карту и исследовать комнату): ")

            if choice == "1":
                print(77 * "-")
                print("Вы идете по карте и приходите к тайному проходу.")
                choice = input("Выберите действие (1 - Войти в проход, 2 - Оставить проход и вернуться назад): ")

                if choice == "1":
                    print(77 * "-")
                    print("Проход приводит вас к выходу из замка. Вы выиграли!")
                else:
                    print(77 * "-")
                    print("Вы оставляете проход и возвращаетесь назад. Вы проиграли.")
            else:
                print(77 * "-")
                print("Вы игнорируете карту и исследуете комнату. Вы проиграли.")
        else:
            print(77 * "-")
            print("Вы выходите из комнаты и попадаете в коридор с двумя новыми дверями.")
            choice = input("Выберите действие (1 - Первая дверь, 2 - Вторая дверь): ")

            if choice == "1":
                print(77 * "-")
                print("Вы входите в первую дверь и видите старого мага.")
                choice = input("Выберите действие (1 - Поговорить с магом, 2 - Игнорировать мага и выйти): ")

                if choice == "1":
                    print(77 * "-")
                    print("Маг дает вам волшебный ключ, который открывает все двери в замке.")
                    choice = input("Выберите действие (1 - Использовать ключ для выхода, 2 - Оставить ключ и искать дальше): ")

                    if choice == "1":
                        print(77 * "-")
                        print("Вы находите дверь, открываете ее ключом и выходите из замка. Вы выиграли!")
                    else:
                        print(77 * "-")
                        print("Вы оставляете ключ и продолжаете искать. Вы проиграли.")
                else:
                    print(77 * "-")
                    print("Вы игнорируете мага и выходите. Вы проиграли.")
            else:
                print(77 * "-")
                print("Вы входите во вторую дверь и видите зеркало, в котором отражается другая комната.")
                choice = input("Выберите действие (1 - Войти в зеркало, 2 - Разбить зеркало): ")

                if choice == "1":
                    print(77 * "-")
                    print("Вы проходите через зеркало и оказываетесь в другой части замка, где находите выход. Вы выиграли!")
                else:
                    print(77 * "-")
                    print("Зеркало разбивается, и вы оказываетесь в ловушке. Вы проиграли.")
    else:
        print(77 * "-")
        print("Вы входите в правую комнату и видите лестницу, ведущую вниз.")
        choice = input("Выберите действие (1 - Спуститься по лестнице, 2 - Остаться наверху): ")

        if choice == "1":
            print(77 * "-")
            print("Лестница ведет вас в подземелье, где вас поджидает дракон.")
            choice = input("Выберите действие (1 - Сражаться с драконом, 2 - Бежать от дракона): ")

            if choice == "1":
                print(77 * "-")
                print("Вы сражаетесь храбро, но дракон оказывается слишком сильным. Вы проиграли.")
            else:
                print(77 * "-")
                print("Вы бежите обратно по лестнице, но дверь наверху оказывается заперта. Вы в ловушке. Вы проиграли.")
        else:
            print(77 * "-")
            print("Вы решаете не спускаться по лестнице и находите потайную дверь за картиной.")
            choice = input("Выберите действие (1 - Войти в потайную дверь, 2 - Игнорировать дверь и вернуться назад): ")

            if choice == "1":
                print(77 * "-")
                print("Потайная дверь приводит вас к выходу из замка. Вы выиграли!")
            else:
                print(77 * "-")
                print("Вы игнорируете дверь и возвращаетесь назад. Вы проиграли.")

if __name__ == "__main__":
    text_quest()