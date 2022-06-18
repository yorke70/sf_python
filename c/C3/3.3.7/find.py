from func import *

radius = int(input("Введите радиус круга: "))
a, b = input("Введите ширину и высоту прямоугольника: ").split()
width, hight = int(a), int(b)

def main():
    if cicle_are(radius) > rectangle_are(width, hight):
        print(f"Площадь круга с радиусом {radius} "
              f"больше площади прямоугольника со сторонами {width}, {hight}")
    elif cicle_are(radius) == rectangle_are(width, hight):
        print("Площади фигур равны")
    else:
        print(f"Площадь круга с радиусом {radius} "
              f"меньше площади прямоугольника со сторонами {width}, {hight}")


if __name__ == "__main__":
    main()
