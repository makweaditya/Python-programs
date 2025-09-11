import random

number = random.randint(0, 10)

print(number)

print("Guess a number between 0 to 10 in ten trials")

i = 0

while (i < 10):

    user_number = int(input("Guess a number :"))
    # print(user_number)

    if (user_number > number):
        print("Guess a lower number")
        i += 1
        # user_number = int(input("Guess a number"))


    elif (user_number < number):
        print("Guess a higher number")
        i += 1
        # user_number = int(input("Guess a number"))


    elif (user_number == number):
        print("Your guess is correct")
        break

if (user_number == number):
    print("You Won")
else:
    print("Your chances are over")
