a = list(map(int, input("Ввести числа через пробел: ").split()))
print(not any(a)) #возвращает True, если все элементы равны 0, иначе False
