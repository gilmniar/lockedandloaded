def out():
    print(f"  0 1 2")
    for i, row in enumerate(field):
        row_str = f"{i} {' '.join(row)}"
        print(row_str)

def inp():
    while True:
        coord = input("Сделайте ход ").split()

        if len(coord) != 2:
            print("Введите две координаты")
            continue

        x, y = coord

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x >2 or 0 > y or y > 2:
            print("Координаты вне диапазона")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y

def iswin():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["x", "x", "x"]:
            print("Победили крестики!")
            return True
        elif symbols == ["o", "o", "o"]:
            print("Победили нолики!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["x", "x", "x"]:
            print("Победили крестики!")
            return True
        elif symbols == ["o", "o", "o"]:
            print("Победили нолики!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
        if symbols == ["x", "x", "x"]:
            print("Победили крестики!")
            return True
        elif symbols == ["o", "o", "o"]:
            print("Победили нолики!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2 - i])
        if symbols == ["x", "x", "x"]:
            print("Победили крестики!")
            return True
        elif symbols == ["o", "o", "o"]:
            print("Победили нолики!")
            return True
    return False




def hello():
    print(f"Игра крестики нолики\n")
    print(f"Вводите координаты x(строка) y(столбец) и стараетесь победить!\n")

hello()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    out()

    if count % 2 == 1:
        print("Ходят крестики\n")
    else:
        print("Ходят нолики\n")

    x, y = inp()

    if count % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "o"

    if iswin():
        break

    if count == 9:
        print("Ничья")
        break
