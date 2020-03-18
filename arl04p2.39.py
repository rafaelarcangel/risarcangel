"""R. IÑIGO S. ARCANGEL
   DATALOG Lab04
   Feb. 12, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""


from abc import ABC, abstractmethod

class Polygon(ABC):

    def __init__(self, lengths_of_sides):
        self.number_of_sides = lengths_of_sides

    def print_num_sides(self):
        print('There are ' + str(self.number_of_sides) + ' sides.')




class Triangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  # list of three numbers

    def get_area(self):
        '''return the area of the triangle using the semi-perimeter method'''
        a, b, c = self.lengths_of_sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__([side, side, side])


class Octagon(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 4, lengths_of_sides)

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        '''Return the perimeter of the polygon.'''
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x + y) * 2

class Pentagon(Polygon):
    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 5, self.number_of_sides

class Hexagon(Polygon):
    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 6, self.number_of_sides
    def area(self):
        a, b = self.length_of_sides[0], self.length_of_sides[1]
        return a * b
    def perimeter(self):
        p1, p2 = self.length_of_sides
        return (p1+p2)*2


class Rectangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 4)
        self.lengths_of_sides = lengths_of_sides  # list of two numbers

    def get_area(self):
        '''return the area of the rectangle: length x width'''
        x, y = self.lengths_of_sides
        return x * y

class Square(Rectangle):

    def __init__(self, side):
        Rectangle.__init__(self, [side, side])




print("Triangle")
tri = Triangle([3, 4, 5])
tri.print_num_sides()
print(tri.get_area())


print("----------")
print("Square")
s = Square(8)
s.print_num_sides()
print(s.lengths_of_sides)
print(s.get_area())


print("----------")
print("Rectangle")
r = Rectangle([5])
r.print_num_sides()

print("-----------")
print("Equilateral Triangle")

e = EquilateralTriangle(5)
e.print_num_sides()

print("------------")
p = Pentagon([5])
p.print_num_sides()
print(tri.get_area())

