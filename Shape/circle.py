from shape import Shape

class Circle(Shape):
    def __init__(self, radius=0.0, color="Black", borderWidth=1.0):
        super().__init__(color, borderWidth)
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius