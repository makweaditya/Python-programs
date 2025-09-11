# Minimum number in list

length = int(input(f"Enter the length of list"))
l = []

for i in range(0, length):
    number = int(input(f"enter the {i} number"))
    l.append(number)

print(l)

first_element = l[0]
i = 0
while (i < len(l)):
    if first_element > l[i]:
        first_element = l[i]
    i += 1
print(f"Smallest element in list is : {first_element}")
