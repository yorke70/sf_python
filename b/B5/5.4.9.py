L = [1, 2, 5, 0, -2]
def min(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min(L[1:]) else min(L[1:])
print(min(L))
