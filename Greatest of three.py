num = print("enter a three digit number")

num1 = input("enter first number")
num2 = input("enter second number")
num3 = input("enter third number")

big = (num1 if (num1>num3) else num3) if (num1 > num2) else (num2 if (num2 > num3) else num3)
print(big)

if (int(num1) > int(num2)) and (int(num1) > int(num3)):
    print(f"{num1} is greater")

elif int(num2) > int(num3):
    print(f"{num2} is greater")

else:
    print(f"{num3} is greater")


