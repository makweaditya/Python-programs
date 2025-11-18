# Armstrong Number Program

num = int(input("Enter a number: "))

# Convert number to string to count digits
order = len(str(num))

# Initialize sum
sum = 0

# Make a copy of num
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check if num is equal to sum
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
