# to find the value of f(x):
# f(x) = x^2 + 5x + 3, if x > 2
#      = x + 3 if x <=2

x = int(input("enter the value of x :"))

if x > 2:
    f = ((pow(x,2)) + (5*x) + 3)

else:
    f = x + 3

print(f"Value of function f(x) {f}")


