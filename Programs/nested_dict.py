students = {
    "s1": {"name": "Aditya", "age": 22},
    "s2": [1,2.0,"Ravi"]
}


# print(students["s2"]["age"])   # Output: Aditya
temp = students.pop("s2")
print(temp)

for i in range(0,len(temp)):
    print(temp[i])
