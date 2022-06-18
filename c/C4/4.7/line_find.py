def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return f"Индекс искомого элемента в списке {i}"
    return False

def count(array, element):
    count = 0
    for i, a in enumerate(array):
        if a == element:
            count += 1
            print(f"Индекс искомого элемента в списке {i}")
    return f"Количество элементов в списке {count}"


array = list(map(int, input("Создать список чисел: ").split()))
element = int(input("Ввести число: "))

print(find(array, element))

