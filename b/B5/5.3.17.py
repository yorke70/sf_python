L = [i for i in range(10)]
M = [j for j in range(10, 0, -1)]
N = [i * j for i, j in zip(L, M)]
print(*N)
