class Car:
    wheels = 4

    def __init__(self, model, color):
        self.model = model
        self.color = color
        print("Inside constructor")

    def show(self):
        print(f"Model: {self.model}, {self.color},{self.wheels}")

    def __del__(self):
        print("inside destructor")

c1 = Car("Tata","White")
c1.show()
temp = Car.wheels
print(temp)
# c2 = Car("Maruti", "Black")

