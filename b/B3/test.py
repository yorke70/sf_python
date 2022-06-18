a = int(input("Введите число: "))
M = int(a / 1000)
D = int(a % 1000 / 500)
C = int(a % 500 / 100)
L = int(a % 100 / 50)
X = int(a % 50 / 10)
V = int(a % 10 / 5)
I = int(a % 5)

while a >= 1:
    if a >= 1000:
        print("M"*M)
        a = a % 1000
    elif 500 <= a < 900:
        print("D" * D)
        a = a % 500
    elif a >= 900:
        print("CM")
        a = a - 900
    elif 100 <= a < 400:
        print("C" * C)
        a = a % 100
    elif a >= 400:
        print("CD")
        a = a - 400
    elif 50 <= a < 90:
        print("L" * L)
        a = a % 50
    elif a >= 90:
        print("XC")
        a = a - 90
    elif 10 <= a < 40:
        print("X" * X)
        a = a % 10
    elif a >= 40:
        print("XL")
        a = a - 40
    elif 5 <= a < 9:
        print("V" + "I" * (a-5))
        a = a % 5 - 5
    elif a >= 9:
        print("IX")
        a = a % 5 - 5
    elif a < 4:
        print("I" * a)
        a = 0
    elif a == 4:
        print("IV")
        a = 0
