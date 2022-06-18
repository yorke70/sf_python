a = 1201
def reverse_num(a):
    b = str(a)
    return b[::-1]
print(reverse_num(a))

def mirror_rec(a, b=0):
    return mirror_rec(a // 10, b * 10 + a % 10) if a else b
print(mirror_rec(a))
