# class square
class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of square is:", self.side**2)
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width =width

    def area(self):
        print("Area of Rectangle is:", self.length*self.width )


Isquare = Square(5)
IRectangle = Rectangle (5, 2)




for shape in (Isquare, IRectangle):
    shape.area()