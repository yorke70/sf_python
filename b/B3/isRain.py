temperature = int(input("Введите температуру в формате целого числа:"))
isRain = input("Введите, идет ли дождь, в формате True\False:")
isRain_max = input("Введите, сильный ли дождь, в формате True\False:")
if 20 < temperature < 30:
    if isRain:
        print("Надеть футболку, шорты и дождевик!")
    else:
        print("Надеть футболку и шорты")
elif temperature >=30:
    print("Остаться дома, жарко")
else:
    if 0 < temperature <=20:
        if isRain:
            if isRain_max:
                print("Надеть пальто, резиновые сапоги, взять зонт!")
            else:
                print("Надеть пальто и дождевик!")
        else:
            print("Надеть пальто!")
    else:
        print("Надеть пуховик!")
