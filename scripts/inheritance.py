class Rectangle:
    def __init__(self, base, h):
        self.base = base
        self.h = h

    def area(self):
        return self.base * self.h
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


if __name__ == '__main__':
    rectangle = Rectangle(3, 4)
    print(rectangle.area())
    square = Square(6)
    print(square.area())
