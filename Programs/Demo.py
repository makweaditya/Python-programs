class Employee:
    name = "Aditya" # class variable
    def display(self):
        name = "Mincoders" # instance variable
        print("This is display method of class")
        print(f"THe name is : {name}")

    # print(f"THe name is : {name}")

emp1 = Employee()
emp1.display()
# print(f"THe name is : {emp1.name}")
# print(f"The name of employee is {emp1.name}")
