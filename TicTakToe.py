def game():
    rules()
    board = create_grid()
    print_grid(board)
    role_1, role_2 = assign_role()
    overfill(board, role_1, role_2)


first_player = input('Игрок 1, введите Ваше имя: ')
second_player = input('Игрок 2, введите Ваше имя: ')
# Запрашиваем никнеймы
print("\n")


def rules():
    # Выводим правила игры
    print("Привет! Добро пожаловать в игру 'Крестики-нолики!'")
    print("\n")
    print("Правила игры:")
    print(f"{first_player} и {second_player}, по очереди ставят на свободные клетки поля 3×3 знаки -")
    print("один всегда крестики, другой всегда нолики.")
    print("Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.")
    print("\n")


def create_grid():
    # Создаем игровое поле
    print("Это игровое поле:")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def assign_role():
    # Присваиваем игроку роль
    role_1 = input(
        f"{first_player}, ты хочешь играть за крестики (напишите 'X') или за нолики (напишите 'O')? ").upper()

    if role_1 == "X":
        role_2 = "O"
        print(f"{second_player}, ты будешь за нолики.")

    elif role_1 == "O":
        role_2 = "X"
        print(f"{second_player}, ты будешь за крестики.")
        print("\n")
    else:
        print("Неверное значение. Попробуйте еще раз.")

        assign_role()

    return role_1, role_2


def start_game(board, role_1, role_2, count):
    # Начинаем игру
    player = None
    # Выбираем чей ход
    if count % 2 == 0:
        player = role_1
    elif count % 2 == 1:
        player = role_2
    print("Сейчас ходят ", player + "ки")
    row = int(input("Выберите строку:"
                    "[верхняя строка: введите 0, средняя строка: введите 1, нижняя строка: введите 2]:"))
    column = int(input("Выберите колонку:"
                       "[левая колонка: введите 0, средняя колонка: введите 1, правая колонка: введите 2]:"))

    # Проверка на корректность введенной координаты
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        out_of_board(row, column)
        row = int(input("Выберите строку:"
                        "[верхняя строка: введите 0, средняя строка: введите 1, нижняя строка: введите 2]:"))
        column = int(input("Выберите колонку:"
                           "[левая колонка: введите 0, средняя колонка: введите 1, правая колонка: введите 2]:"))

        # Проверка на свободную ячейку
    while (board[row][column] == role_1) or (board[row][column] == role_2):
        wrong_place(board, role_1, role_2, row, column)
        row = int(input("Выберите строку:"
                        "[верхняя строка: введите 0, средняя строка: введите 1, нижняя строка: введите 2]:"))
        column = int(input("Выберите колонку:"
                           "[левая колонка: введите 0, средняя колонка: введите 1, правая колонка: введите 2]:"))

        # Рисуем символ на игровом поле
    if player == role_1:
        board[row][column] = role_1

    else:
        board[row][column] = role_2

    return board


def overfill(board, role_1, role_2):
    count = 1
    winner = True
    # Проверяем свободные клетки на поле
    while count < 10 and winner:
        start_game(board, role_1, role_2, count)
        print_grid(board)

        if count == 9:
            print("Свободные клетки кончились. Ничья.")
            if winner:
                print("Игра окончена.")

        # Проверка на победу
        winner = victory(board, role_1, role_2, count)
        count += 1

    if not winner:
        print("Игра окончена.")


def out_of_board(row, column):
    # Оповещаем игрока о неверном вводе координат
    print("Неверный выбор клетки. Попробуйте еще раз. ")


def print_grid(board):
    # Распечатываем игровое поле для игроков
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for i in range(rows):
        print(board[i][0], " |", board[i][1], "|", board[i][2])
        print("---+---+---")
    return board


def victory(board, role_1, role_2, count):
    # Поздравляем игрока с победой
    winner = True
    # Проверяем строки
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] == role_1:
            winner = False
            print(f"{first_player}, " + role_1 + "ки, победили!")

        elif board[row][0] == board[row][1] == board[row][2] == role_2:
            winner = False
            print(f"{second_player}, " + role_2 + "ки, победили!")

    # Проверяем колонки
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == role_1:
            winner = False
            print(f"{first_player}, " + role_1 + "ки, победили!")
        elif board[0][col] == board[1][col] == board[2][col] == role_2:
            winner = False
            print(f"{second_player}, " + role_2 + "ки, победили!")

    # Проверяем диагонали
    if board[0][0] == board[1][1] == board[2][2] == role_1:
        winner = False
        print(f"{first_player}, " + role_1 + "ки, победили!")

    elif board[0][0] == board[1][1] == board[2][2] == role_2:
        winner = False
        print(f"{second_player}, " + role_2 + "ки, победили!")

    elif board[0][2] == board[1][1] == board[2][0] == role_1:
        winner = False
        print(f"{first_player}, " + role_1 + "ки, победили!")

    elif board[0][2] == board[1][1] == board[2][0] == role_2:
        winner = False
        print(f"{second_player}, " + role_2 + "ки, победили!")

    return winner


# Оповещаем, что ячейка занята
def wrong_place(board, role_1, role_2, row, column):
    print("Клетка, которую Вы выбрали, уже занята. Выберите другую. ")


game()
