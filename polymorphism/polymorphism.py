class Shape:
    def area(self):
        print("Area of shape")

class Rectangle(Shape):
    def area(self):
        print("Area = length × width")

class Circle(Shape):
    def area(self):
        print("Area = π × r²")

s = Shape()
r = Rectangle()
c = Circle()

s.area()
r.area()
c.area()

# for obj in (s, r, c):
#     obj.area()  # Calls different 'area' methods

