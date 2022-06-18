try:
    a = input("Введите число:\t")
    b = int(a)
except ValueError:
    print("Вы ввели неправильное число")
else:
    print(f"Вы ввели правильное число {b}")
finally:
    print("Выход из программы")
