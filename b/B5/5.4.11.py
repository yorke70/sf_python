S = 5
N = 131
def equal(N, S): # Сравнивает сумму цифр первого числа и второе
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)
print(equal(N, S))
