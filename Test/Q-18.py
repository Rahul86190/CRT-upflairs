class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")

class Car(Vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color)
        self.model = model

    def display_car_info(self):
        self.display_info()
        print(f"Model: {self.model}")

my_car = Car("Toyota", "Red", "Bugati")
my_car.display_car_info()