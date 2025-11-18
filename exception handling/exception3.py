try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
<<<<<<< HEAD
except ValueError:
    print("Please enter a valid number.")
=======
>>>>>>> 5d1c80eedd7a680ebcdad51955b90c91ef42a6ee
else:
    print("Division successful! Result =", result)
finally:
    print("Program execution complete.")
