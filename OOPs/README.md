# Object-Oriented Programing Example
# Car Showroom Application

## Overview

This project demonstrates a simple Car Showroom application with functionalities to calculate car horsepower, total price including tax, and checking the availability of car models within a specified price range.

## Class-Based Implementation: CarShowroom

### Description

The `CarShowroom` class provides methods to manage car specifications and perform calculations related to car pricing and horsepower.

### Methods

- `__init__(self) -> None`: Initializes the CarShowroom object with default values.
- `cal_hp(self, car_torque: int, car_rpm: int) -> float`: Calculates the horsepower of the car based on torque and RPM.
- `cal_total(self, car_tax: int) -> int`: Calculates the total price of the car including tax.
- `set_cp(self, car_price: int) -> None`: Sets the price of the car.
- `get_cp(self) -> int`: Retrieves the price of the car.
- `set_hp(self, hp: float) -> None`: Sets the horsepower of the car.
- `get_hp(self) -> float`: Retrieves the horsepower of the car.
- `set_total(self, total: int) -> None`: Sets the total price of the car including tax.
- `get_total(self) -> int`: Retrieves the total price of the car including tax.
- `check_model(self, car_name: str) -> str`: Checks if a car model is available and within the specified price range.
- `car_avail(self, car_name: str) -> str`: Checks if a specific car model is available in the showroom.

### Example Usage

```python
# Initialize CarShowroom object
car = CarShowroom()

# Calculate and set car horsepower
hp = car.cal_hp(145, 4600)
car.set_hp(hp)
print(f"Horsepower: {car.get_hp()}")

# Set company price of the car
car.set_cp(2000000)
print(f"Car Price: {car.get_cp()}")

# Calculate total price including tax
total = car.cal_total(50000)
car.set_total(total)
print(f"Total price including tax: {car.get_total()}")

# Example usage of check_model function
is_valid_model = car.check_model("Toyota")
print(f"Is this car in your budget? {is_valid_model}")

# Example usage of car_avail function
is_car_available = car.car_avail("Toyota")
print(f"Is the 'Toyota' model available? {is_car_available}")
