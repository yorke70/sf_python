array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0:
        count += 1
        if not key < array[j]:
            break
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key


print(array, count)
