class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):
        super().show()
        print("This is Child class method")

# Creating object
obj = Child()
obj.show()
