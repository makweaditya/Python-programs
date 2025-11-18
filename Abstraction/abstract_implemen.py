from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def abc(self):
        print("This is method of abstact class")

class Circle(Shape):

    def area(self):
        print("this is area method of abstract class circle")

    def abc(self):
        print("this is abc method of sub class circle")


obj = Circle()
obj.area()
obj.abc()
