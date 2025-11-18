from shape import Shape

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
