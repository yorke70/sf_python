def chet(num):
    return num % 2 == 0 and num != 0


result = filter(chet, [-2, -1, 0, 1, -3, 2, -3])
result_list = list(result)
print(*result_list)
