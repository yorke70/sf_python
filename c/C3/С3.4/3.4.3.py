import os

def cat_walk():
    cat = input("Введите адрес каталога: ")
    tree = os.walk(cat)
    for i in tree:
        print(i)

cat_walk()
