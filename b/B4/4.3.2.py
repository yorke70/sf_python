def mult(*num):
    result = 1
    for i in num:
        result *= i
    return result

print(mult(1))
print(mult(1, 2, 3))
