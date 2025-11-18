# Fibonacci Series using Recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Input from user
num = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
for i in range(num):
    print(fibonacci(i), end=" ")
