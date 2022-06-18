def fact(i):
    if i == 1:
        return i
    return i * fact(i - 1)

def fact_num(fact):
    a = str(fact)
    return len(a)

print(fact_num(fact(100)))
