array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)): # проходим по всему массиву
    idx_max = i # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        count += 1
        if array[j] > array[idx_max]:
            idx_max = j

    if i != idx_max: # если индекс не совпадает с минимальным, меняем
            array[i], array[idx_max] = array[idx_max], array[i]

print(array, count)
