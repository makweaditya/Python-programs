nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Even numbers are:")
for n in nums:
    if n % 2 == 0:
        print(n)
