try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Division successful! Result =", result)
finally:
    print("Program execution complete.")
