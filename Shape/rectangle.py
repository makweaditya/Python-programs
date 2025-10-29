from shape import Shape

class Rectangle(Shape):
    def __init__(self, length=0.0, width=0.0, color="Black", borderWidth=1.0):
        super().__init__(color, borderWidth)
        self.__length = length
        self.__width = width

    def getLength(self):
        return self.__length
    def setLength(self, length):
        self.__length = length

    def getWidth(self):
        return self.__width
    def setWidth(self, width):
        self.__width = width
