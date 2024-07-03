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
