class Student:
    def __init__(self, name, marks):
        self.__name = name       # private variable
        self.__marks = marks     # private variable

    # Getter method
    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

# Using the class
s1 = Student("Aditya", 85)

print("Name:", s1.get_name())
<<<<<<< HEAD
# print("Marks:", s1.get_marks())
=======
print("Marks:", s1.get_marks())
>>>>>>> f569f3210f1c23a0bfc55d057b8953ede2b40b76

s1.set_marks(90)
print("Updated Marks:", s1.get_marks())

<<<<<<< HEAD

# print(s1.__marks)
# print(s1.name)
=======
# Trying direct access
# print(s1.__marks)  # ❌ AttributeError (Data hidden)
>>>>>>> f569f3210f1c23a0bfc55d057b8953ede2b40b76
