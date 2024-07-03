# Car Specifications and Calculations

This project demonstrates simple car specification management and calculations, including horsepower and total price calculations. It also checks the availability of car models within a specified price range.

## Functions

### `car_specification(car_price: int) -> dict`
Creates a dictionary containing the car price and a list of car names.

**Parameters:**
- `car_price` (int): The price of the car.

**Returns:**
- dict: A dictionary with car price and car names.

### `calculate_hp(car_torque: int, car_RPM: int) -> float`
Calculates the horsepower of a car given the torque and RPM.

**Parameters:**
- `car_torque` (int): The torque of the car.
- `car_RPM` (int): The RPM of the car.

**Returns:**
- float: The calculated horsepower.

### `calculate_total_price(car, car_tax: int) -> int`
Calculates the total price of the car including tax.

**Parameters:**
- `car` (dict): A dictionary containing car specifications.
- `car_tax` (int): The tax amount to be added to the car price.

**Returns:**
- int: The total price of the car including tax.

### `check_model(car, car_name: str) -> bool`
Checks if the car model is available and within the specified price range.

**Parameters:**
- `car` (dict): A dictionary containing car specifications.
- `car_name` (str): The name of the car model to check.

**Returns:**
- bool: `True` if the car model is available and within the price range, `False` otherwise.

## Usage

```python
def car_specification(car_price: int):
    return {
        "car_price": car_price,
        "car_name": ["Honda", "Toyota", "Suzuki", "Hyundai", "Changan", "Glory", "Haval", "KIA", "BMW"]
       }

def calculate_hp(car_torque: int, car_RPM: int) -> float:
    return car_torque * (car_RPM / 5252)

def calculate_total_price(car, car_tax: int) -> int:
    return car["car_price"] + car_tax

def check_model(car, car_name: str) -> bool:
    if car["car_price"] >= 5000000 and car["car_price"] <= 100000000:
        return car_name in car["car_name"]
    return False

if __name__ == "__main__":
     car = car_specification(25000000)
     print(car)

     car_hp = calculate_hp(145, 4300)
     print(f"Car HP: {car_hp}")

     total = calculate_total_price(car, 500000)
     print(f"Total price is: {total}")

     model_check = check_model(car, "Honda")
     print(f"Is the car model available and within price range? {'Yes' if model_check else 'No'}")
