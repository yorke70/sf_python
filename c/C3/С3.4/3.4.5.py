import random
with open('numbers.txt', 'w', encoding='utf8') as a:
    for i in range(20):
        temp = random.randint(1, 1000)
        a.writelines(str(temp)+"\n")
with open('numbers.txt', 'r', encoding='utf8') as a:
    min_int = max_int = int(a.readline())
    for line in a:
        temp = int(line)
        if temp > max_int:
            max_int = temp
        elif temp < min_int:
            min_int = temp
    # print(max_int, min_int)
    with open('output.txt', 'w', encoding='utf8') as out:
        out.writelines(str(min_int)+"\n")
        out.writelines(str(max_int)+"\n")
        out.writelines("Сумма минимума и максимума = " + str(min_int + max_int)
                       + '\n')

with open('output.txt', encoding='utf8') as a:
    for line in a:
        print(line, end='')
