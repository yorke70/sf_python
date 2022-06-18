def sum_c(n):
    if n < 10:
        return n
    return n % 10 + sum_c(n // 10)

print(sum_c(125))
