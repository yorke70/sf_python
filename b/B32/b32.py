str = None
while True:
    str = input("Введите число: ")
    if str.isdigit():
        num = int(str)
        break
    else:
        print("Необходимо ввести число, только число")
        print("---")

check = int(input("Введите искомую цифру: "))
while num >= 1:
    if num % 10 == check or num == check:
        print(f"Искомая цифра {check} в числе {str} найдена!")
        break
    else:
        num = num // 10
if num < 1:
    print(f"Искомая цифра {check} в числе {str} не найдена!")
