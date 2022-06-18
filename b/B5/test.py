# a = None # пустая строка
# b = a or 1
# print(b)
def linear_solve(a, b):
    return b / a
print(linear_solve(9, 9))

iter_obj = iter("Hello!")
for i in range(8):
    print(next(iter_obj))
