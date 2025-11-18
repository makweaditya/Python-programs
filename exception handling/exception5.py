from InvalidAgeError import *

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeError
    else:
        print("Eligible to vote!")
except InvalidAgeError:
    print("You must be 18 or older to vote.")
