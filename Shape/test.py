from rectangle import Rectangle
from circle import Circle
from triangle import Triangle

if __name__ == "__main__":
    rect = Rectangle(length=10, width=5, color="Blue", borderWidth=2)
    circle = Circle(radius=7, color="Red", borderWidth=1.5)
    tri = Triangle(base=6, height=8, color="Green", borderWidth=1)

    print("Rectangle:", rect.getColor(), rect.getLength(), rect.getWidth())
    print("Circle:", circle.getColor(), circle.getRadius())
    print("Triangle:", tri.getColor(), tri.getBase(), tri.getHeight())
