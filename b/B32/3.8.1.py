test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]
max_value = 0
for i in test_matrix:
    for j in range(len(i)):
        if i[j] > max_value:
            max_value = i[j]
print(max_value)
