class Square:
    def __init__(self, side):
        self.side = side if side > 0 else NonPositiveDigitException


class NonPositiveDigitException(ValueError):
    print("Неправильно указана сторона квадрата")

    
a = Square(-1)