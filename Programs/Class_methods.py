class Cars:

    wheels = 4

    def __init__(self, brand, color):

        self.brand = brand
        self.color = color

    def display(self):
        print(f"The {self.brand} is of {self.color} color")

    @classmethod
    def change_wheels(cls,num):
        cls.wheels = num

    @staticmethod
    def welcome():
        print("Welcome to car showroom")

car1 = Cars('Honda','red')
car1.display()
car2 = Cars("Maruti", "White")
car2.display()
Cars.welcome()
Cars.change_wheels(6)
print("Total wheels now:", Cars.wheels)


