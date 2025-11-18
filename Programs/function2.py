num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

def add(a,b):
    # temp = a + b
    # return (temp)
    return(a+b)

def subtract(a,b):
    return(a-b)

def div(a,b):
    return(a/b)

def mul(a,b):
    return(a*b)

temp1 = add(num1,num2)
print(f"The addition of {num1} and {num2} is : {temp1}")

temp2 = subtract(num1,num2)
print(f"The subtraction of {num1} and {num2} is : {temp2}")

temp3 = div(num1,num2)
print(f"The division of {num1} and {num2} is : {temp3}")

temp4 = mul(num1,num2)
print(f"The multiplication of {num1} and {num2} is : {temp4}")
