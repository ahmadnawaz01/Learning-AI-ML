class Employee:
    # Class Attribute
    company_name = "TechCorp"
    bonus_percentage = 0.10

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.__salary = salary  # Private attribute

    # 1. @property (The Getter)
    # Allows you to access a method like an attribute (no brackets needed)
    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # 2. @property.setter
    # Allows you to "assign" a value to a method
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # 3. @staticmethod
    # Does not take 'self' or 'cls'. It's just a regular function 
    # that lives inside the class because it's logically related.
    @staticmethod
    def is_workday(day):
        # 5 is Saturday, 6 is Sunday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # 4. @classmethod
    # Takes 'cls' instead of 'self'. It can modify the CLASS itself,
    # or be used as a "Factory Method" to create objects in a new way.
    @classmethod
    def change_bonus(cls, amount):
        cls.bonus_percentage = amount

    @classmethod
    def from_string(cls, emp_str):
        # Creates an employee object from a string like "John-Doe-5000"
        first, last, salary = emp_str.split("-")
        return cls(first, last, int(salary))

# --- EXECUTION ---

# Testing @property
emp = Employee("Ahmad", "Nawaz", 50000)
print(f"Email: {emp.email}")  # No () needed!

# Testing @fullname.setter
emp.fullname = "Ali Khan"
print(f"Updated First Name: {emp.first}")

# Testing @staticmethod
import datetime
my_date = datetime.date(2026, 3, 26) # Thursday
print(f"Is work day? {Employee.is_workday(my_date)}")

# Testing @classmethod (Factory Method)
new_emp_str = "Sara-Ahmed-60000"
emp2 = Employee.from_string(new_emp_str)
print(f"New Emp Fullname: {emp2.fullname}")

# Testing @classmethod (Modify Class state)
Employee.change_bonus(0.15)
print(f"New Bonus: {Employee.bonus_percentage}")