def repeat_list(n):
    list = n.copy()
    while True:
        value = list.pop(0)
        list.append(value)
        yield value


iter_list = iter(repeat_list([1, 2, 3]))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
