def e(): # вычисление экспоненты с точностью n
    n = 1
    while True:
        yield (1 + 1 / n) ** n
        n += 1
