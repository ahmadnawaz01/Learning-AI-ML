from abc import ABC, abstractmethod

# 1. ABSTRACTION (The Blueprint)
# We use ABC (Abstract Base Class) to define a template that cannot be instantiated.
class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

# 2. CLASS & INHERITANCE
# 'Car' inherits from 'Vehicle'
class Car(Vehicle):
    # Class Attribute (Shared by all instances)
    wheels = 4

    # 3. CONSTRUCTOR & INSTANCE ATTRIBUTES
    def __init__(self, brand, model, price):
        self.brand = brand          # Public attribute
        self._model = model        # PROTECTED attribute (suggested internal use)
        self.__price = price       # PRIVATE attribute (ENCAPSULATION - hidden)

    # 4. ENCAPSULATION (Getter and Setter)
    # Allows controlled access to private data (__price)
    def get_price(self):
        return f"${self.__price}"

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

    # 5. POLYMORPHISM (Method Overriding)
    def fuel_type(self):
        return "Petrol or Diesel"

    # Instance Method
    def display_info(self):
        return f"This is a {self.brand} {self._model}."

    # 6. DUNDER / MAGIC METHODS
    # Changes how the object is printed
    def __str__(self):
        return f"Car Object: {self.brand}"

# 7. MULTI-LEVEL INHERITANCE
class ElectricCar(Car):
    def __init__(self, brand, model, price, battery_capacity):
        # 'super()' calls the constructor of the parent class (Car)
        super().__init__(brand, model, price)
        self.battery = battery_capacity

    # Polymorphism: Overriding the fuel_type for ElectricCar
    def fuel_type(self):
        return "Electricity"

# --- EXECUTION & TESTING ---

# Creating Objects (Instantiating)
my_tesla = ElectricCar("Tesla", "Model S", 80000, "100kWh")
my_toyota = Car("Toyota", "Camry", 30000)

print(my_tesla.display_info())          # Method from parent Car
print(f"Fuel: {my_tesla.fuel_type()}")  # Overridden method
print(f"Wheels: {my_tesla.wheels}")     # Class attribute

# Testing Encapsulation
print(f"Price: {my_toyota.get_price()}")
my_toyota.set_price(32000)
print(f"New Price: {my_toyota.get_price()}")

# Testing Magic Method (__str__)
print(my_toyota)