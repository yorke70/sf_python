def dec_func(func):
    a = {}
    def wrapper(num):
        nonlocal a
        if num not in a:
            a[num] = func(num)
            print(f"Кэширование результата: {a[num]}")
        else:
            print(f"Возвращение из кэша: {a[num]}")
        print(f"Значения кэша {a}")
        return a[num]
    return wrapper


@dec_func
def f(n):
    return n * 123456789

for i in range(5):
    f(i)

