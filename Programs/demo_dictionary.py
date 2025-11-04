student = {
    "name": "Aditya",
    "age": 22,
    "course": "Computer Engineering"
}

student2 = {"city": "Indore"}
student.update(student2)
print(student)

# print(student.items())


#
# for key in student:
#     print(key, ":", student[key])
# #
# for key, value in student.items():
#     print(key, "=", value)

# print(student)

# print(student.get("age"))
# print(student.get("course"))

# print(f"Before adding key and values {student}")
# student["email"] = "aditya@gmail.com"   # Add new key-value pair
# student["age"] = 23                     		# Update existing key
# print(f"After adding key and values {student}")
#
# student.clear()
# print(f"After clear operation {student}")

# temp = student.pop("email")
# student.popitem()
# del student["course"]
# print(student.keys())
# print(student.values())
# print(student.items())
