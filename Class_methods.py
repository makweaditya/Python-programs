class Cars:

    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def displsy(self):
        print(f"The {self.brand} is of {self.color}")

    @classmethod
    def chage_wheels(cls,num):
        cls.wheels = num

    @staticmethod
    def welcome():
        print("Welcome to car showroom")

car1 = Cars('Honda','red')
car1.displsy()
car2 = Cars("Maruti", "White")
car2.displsy()
Cars.welcome()
Cars.chage_wheels(6)
print("Total wheels now:", Cars.wheels)


