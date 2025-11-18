# Parent Class
class Shape:
    def __init__(self, color="Black", borderWidth=1.0):
        self.__color = color
        self.__borderWidth = borderWidth

    # Getter and Setter for color
    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    # Getter and Setter for borderWidth
    def getBorderWidth(self):
        return self.__borderWidth

    def setBorderWidth(self, borderWidth):
        self.__borderWidth = borderWidth


# Child Class 1: Rectangle
class Rectangle(Shape):
    def __init__(self, length=0.0, width=0.0, color="Black", borderWidth=1.0):
        super().__init__(color, borderWidth)
        self.__length = length
        self.__width = width

    # Getters and Setters
    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width


# Child Class 2: Circle
class Circle(Shape):
    def __init__(self, radius=0.0, color="Black", borderWidth=1.0):
        super().__init__(color, borderWidth)
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius


# Child Class 3: Triangle
class Triangle(Shape):
    def __init__(self, base=0.0, height=0.0, color="Black", borderWidth=1.0):
        super().__init__(color, borderWidth)
        self.__base = base
        self.__height = height

    def getBase(self):
        return self.__base

    def setBase(self, base):
        self.__base = base

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height


# ---------- Example Usage ----------
# if __name__ == "__main__":

rect = Rectangle(length=10, width=5, color="Blue", borderWidth=2)
circle = Circle(radius=7, color="Red", borderWidth=1.5)
tri = Triangle(base=6, height=8, color="Green", borderWidth=1)

print("Rectangle:", rect.getColor(), rect.getLength(), rect.getWidth())
print("Circle:", circle.getColor(), circle.getRadius())
print("Triangle:", tri.getColor(), tri.getBase(), tri.getHeight())
