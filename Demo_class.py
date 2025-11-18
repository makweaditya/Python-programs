class Car:
    # ---------- Class Variable ----------
    wheels = 4   # common to all cars

    # ---------- Constructor ----------
    def __init__(self, model, color):
        # Instance Variables
        self.model = model
        self.color = color
        print(f"Car {self.model} created.")

    # ---------- Instance Method ----------
    def display(self):
        print(f"Model: {self.model}, Color: {self.color}, Wheels: {Car.wheels}")

    # ---------- Another Method ----------
    def start(self):
        print(f"{self.model} is starting...")

    # ---------- Destructor ----------
    def __del__(self):
        print(f"Car {self.model} destroyed.")


# ---------- Object Creation ----------
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# ---------- Accessing Methods ----------
car1.display()
car2.display()
car1.start()

# ---------- Accessing Class Variable ----------
print("Total wheels in cars:", Car.wheels)
