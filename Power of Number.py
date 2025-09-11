# Power of a number

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
c = 1
for i in range(1, num2 + 1):
     c = c * num1
print(f"{num1} to power {num2} is {c}")