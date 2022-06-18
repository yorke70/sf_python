def num_gen(start = 1, step = 1, stop = None):
    counter = start
    while True or counter <= stop:
        yield counter
        counter += step

# for i in num_gen(1, 1, 5):
#     print(i)

c = iter(num_gen())
print(next(c))
print(next(c))
print(next(c))
