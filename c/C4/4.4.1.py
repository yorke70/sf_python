def rec_f(i):
    if i == 0:
        return
    else:
        print("До выполнения функции ", i)
        rec_f(i - 1)
        print("После выполнения функции ", i)

rec_f(5)
