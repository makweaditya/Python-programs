try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful! Result =", result)
finally:
    print("Program execution complete.")
