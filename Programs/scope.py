# Global variable
x = 10

def outer_function():
    # Enclosing variable (function scope)
    y = 20

    def inner_function():
        # Local variable
        z = 30
        print("Inside inner_function:")
        print("x (global):", x)  # can access global variable
        print("y (enclosing):", y)  # can access outer function variable
        print("z (local):", z)  # local to this function

    inner_function()

outer_function()

print("\nOutside functions:")
print("x (global):", x)  # accessible
# print(y)
# print(z)
