try:
    try:
        x = int(input("Enter number: "))
        print(10 / x)
    except ZeroDivisionError:
        print("Inner block: Division by zero")
except ValueError:
    print("Outer block: Invalid input")
