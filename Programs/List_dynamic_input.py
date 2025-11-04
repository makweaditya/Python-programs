# Take number of elements from user
n = int(input("Enter number of elements: "))

# Create empty list
my_list = []

# Loop to take dynamic input
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

print("Your list is:", my_list)
