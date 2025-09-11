length = int(input(f"Enter the length of list"))
l = []
print("Input a sorted list")
for i in range(0, length):
    number = int(input(f"enter the {i} number"))
    l.append(number)

print(l)

item = int(input("Enter a number to insert"))
i = length - 1

l.append(None)

while (l[i] > item and i >= 0):
    l[i + 1] = l[i]
    i -= 1
l[i + 1] = item
print(l)
