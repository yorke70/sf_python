import math

PI = math.pi


def cicle_are(radius):
    return PI * radius ** 2


def rectangle_are(width, hight):
    return width * hight


if __name__ == "__main__":
    assert round(cicle_are(5), 1) == 78.5
    assert rectangle_are(4, 5) == 20
