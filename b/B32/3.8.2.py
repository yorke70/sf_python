test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]

row = len(test_matrix)
col = 0
for line in test_matrix:
    if len(line) == row:
        col += 1
print(row == col)
print(test_matrix)
