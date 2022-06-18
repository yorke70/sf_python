def count_decorator(func):
    count = 0
    def dec_func(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f"{func} была выполнена {count} раз")
    return dec_func

@count_decorator
def function(arg):
    print(arg)

for i in range(5):
    function(i)
