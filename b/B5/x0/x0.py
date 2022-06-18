import random

play_field = [i for i in range(1, 10)]
print_field = ["-" for i in range(1, 10)]
win_comb = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7],
            [2, 5, 8], [3, 6, 9]]
first_comb = []
second_comb = []


def input_char():
    field_print(play_field)
    print(f'Куда поставим "{gm_char}"')
    char = ""
    while not char:
        char = input()
        if char.isdigit():
            char = int(char)
        else:
            char = ""
            print("Нужно ввести цифру")
        if char in play_field:
            play_field[char - 1] = gm_char
            print_field[char - 1] = gm_char
            first_comb.append(char)
            print(f'Ты поставил {gm_char} в поле {char}')
            field_print(print_field)
            print("===========")
        else:
            char = ""
            print("Нужно выбрать незанятое число от 1 до 9: ")


def field_print(field):
    count = 0
    a = ""
    for i in field:
        count += 1
        a += "|" + str(i)
        if count == 3:
            print(a + "|")
            a = ""
            count = 0


field_print(play_field)
gm_char = ""
i_char = ""
print("Это наше игровое поле", "===========", sep="\n")

while not gm_char:
    gm_char = input("Введите символ 'х' или '0' которым будем играть: ")
    if gm_char == "x" or gm_char == "0":
        if gm_char == "x":
            i_char = "0"
            print("===========", "Ты выбрал крестики", "===========", sep="\n")
        else:
            print("===========", "Ты выбрал нолики", "===========", sep="\n")
            i_char = "x"
        break
    else:
        gm_char = ""
        print("Нужно ввести только 'x' или '0', попробуй снова")


def i_step():
    step = 1
    a = ""
    while a not in play_field:
        a = random.randint(1, 9)
        step += 1
        if a in play_field:
            play_field[a - 1] = i_char
            print_field[a - 1] = i_char
            second_comb.append(a)
            break
        elif step > 5:
            break


def win(win_com, comb):
    check = set(comb)
    win_c = bool([True for i in win_com if len(check.intersection(i)) == 3])
    return win_c


def game():
    for step in range(1, 10, 2):
        input_char()
        i_step()
        if win(win_comb, first_comb):
            print(f'Победили "{gm_char}"!!!', field_print(print_field), sep="\n")
            break
        elif win(win_comb, second_comb):
            print(f'Победили "{i_char}"!!!', field_print(print_field), sep="\n")
            break
        elif step >= 9:
            print("Ничья")
            break


game()
