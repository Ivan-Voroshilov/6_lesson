
class Road:

    _length = None
    _width = None
    _mass = 25
    _thickness = 5

    def __init__(self, length, width):
        Road._length = length
        Road._width = width

    def final(self):
        return self._length * self._width * self._mass * self._thickness


u_len = int(input('Length \n'))
u_width = int(input('Width \n'))
print(Road(u_len, u_width).final())
