import random
#отрисовка
def rendering(x ,y, sign= 0, first = False):
    height = 4
    width = 4
    back = playing_field[x][y]
    playing_field[x][y] = sign if sign == 0 else"X"
    for i in range(height):
        if i != 0:
            playing_field[i][0] = i
        for j in range(width):
            if i and j != 0 and first:
                playing_field[i][j] = "*"
            if j != width - 1:
                print(playing_field[i][j], end='|')
            else:
                print(playing_field[i][j], end='')
        if i != height - 1:
            print("\n-------")
    print("\n")

    if back != playing_field[x][y]:
        if sign == 0:
            sign = "X"
        else:
            sign = 0
    return sign

#координаты пользователя
def request(sign):
    coordinates = input("\nВведите координаты для хода {}, через пробел и без лишних знаков, только целые числа через пробел: ".format(sign))
    if check(coordinates):
        return rendering(x, y, sign)
    else:
        return sign
#проверка введеных чисел
def check(coordinates):
    global x, y
    for s in coordinates:
        if s.isdigit():
            figure = int(s)
            if figure > 3 or figure < 1:
                print("Введённые вами числа не соответствуют диапазону поля, введите новые координаты")
                return False

        elif s == " ":
            pass
        else:
            print("Неправильный формат ввода, попробуйте ещё раз")
            return False
    x, y = map(int, coordinates.split())
    if playing_field[x][y] == "*":
        return True
    else:
        print("Данная ячейка занята!")
        return False

def mode():
    comp_personal = input("Вы будете играть с компьютером или с человеком, если с компьютером введите '1' или '2', если с человеком: ")
    if comp_personal.isdigit():
        return int(comp_personal)
    else:
        mode()
def comp(sign):
    x = random.randint(1,3)
    y = random.randint(1,3)
    coordinates = str(x) + " " +str(y)
    if check(coordinates):
        return rendering(x, y, sign)
    else:
        return sign
def win():
    if playing_field[1][1] == playing_field[1][2] == playing_field[1][3] != "*":
        print("Wins", playing_field[1][1])
        return True
    elif playing_field[1][1] == playing_field[2][1] == playing_field[3][1] != "*":
        print("Wins", playing_field[1][1])
        return True
    elif playing_field[2][1] == playing_field[2][2] == playing_field[2][3] != "*":
        print("Wins", playing_field[2][1])
        return True
    elif playing_field[1][2] == playing_field[2][2] == playing_field[3][2] != "*":
        print("Wins", playing_field[1][2])
        return True
    elif playing_field[3][1] == playing_field[3][2] == playing_field[3][3] != "*":
        print("Wins", playing_field[3][1])
        return True
    elif playing_field[1][3] == playing_field[2][3] == playing_field[3][3] != "*":
        print("Wins", playing_field[1][3])
        return True
    elif playing_field[1][1] == playing_field[2][2] == playing_field[3][3] != "*":
        print("Wins", playing_field[1][1])
        return True
    elif playing_field[1][3] == playing_field[2][2] == playing_field[3][1]!= "*":
        print("Wins", playing_field[1][3])
        return True



#приветствие
print("Привет, дорогой друг!\n Рад видеть тебя в игре'Крестики-нолики'\n Разработанной учеником онлайн-школы Скиллфэктори Кужбанова Исляма Баяубаевича")
input("Для продолжения нажмите кнопку 'Enter'")

# отрисовка поля
print("Начнём игру\n")
comp_personal = mode()

global playing_field
height = 4
width = 4
playing_field = [[s for s in range(width)] for i in range(height)]
sign = 1
sign = rendering(0,0,first=True)

# logic
while True:
    sign = request(sign)
    if comp_personal == 1:
        sign = comp(sign)

    if win():
        print("Спасибо за игру!")
        break



