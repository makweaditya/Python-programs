class Shape:
    def __init__(self, color="Black", borderWidth=1.0):
        self.__color = color
        self.__borderWidth = borderWidth

    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color

    def getBorderWidth(self):
        return self.__borderWidth
    def setBorderWidth(self, borderWidth):
        self.__borderWidth = borderWidth
