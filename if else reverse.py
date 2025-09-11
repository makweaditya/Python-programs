# enter a number (more than 2 digit)
# btain the reverese of that number
# Now sum that number
# now check whether the number obtained in sum is in the input number or not
a = input("Enter a number")

b = a[::-1]

print(b)
sum = 0
for i in b:
    sum = sum + int(i)

print(sum)

for j in str(sum):
    if j in a:
        print(f"Yes {j} number is present")
    else:
        print(f"{j} number not present")
