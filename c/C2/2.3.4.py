class Square:
    _side = None
    def __init__(self, side):
        self.side = side

    @property
    def square_side(self):
        return self.side ** 2

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value

sq1 = Square(2)
print(sq1.side)
print(sq1.square_side)
sq1.side = 4
print(sq1.side)
print(sq1.square_side)
