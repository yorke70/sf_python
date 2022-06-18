#a = int(input("Ввести число: "))
b = []
for a in range(1, 999):
    if all([a % 2 == 0,
           a % 3 == 0,
           type(a) == int,
           100 <= a <= 999]):
        b.append(a)
#        print(f"Число {a} удовлетворяет условиям")
#    else:
#       print(f"Число {a} не удволетворяет всем условиям")
print(len(b))
#print(*b, sep="\n")
