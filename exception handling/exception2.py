try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(f'the output is: {result}')
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number.")

