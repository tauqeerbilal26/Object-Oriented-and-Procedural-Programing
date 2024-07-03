class CarShowroom:
    def __init__(self) -> None:
        self._car_price = 0
        self.__hp = 0
        self.__total = 0
        self._car_name = ["Honda", "Toyota", "Suzuki", "Hyundai", "Changan", "Glory", "Haval", "KIA", "BMW"]

    def cal_hp(self, car_torque: int, car_rpm: int) -> float:
        return car_torque * (car_rpm / 5252)

    def cal_total(self, car_tax: int) -> int:
        return self._car_price + car_tax

    def set_cp(self, car_price: int) -> None:
        if car_price <= 500000:
            raise ValueError("Car price can not be less than 5 lakhs")
        self._car_price = car_price

    def get_cp(self) -> int:
        return self._car_price

    def set_hp(self, hp: float) -> None:
        self.__hp = hp

    def get_hp(self) -> float:
        return self.__hp
    
    def set_total(self, total: int) -> None:
        self.__total = total

    def get_total(self) -> int:
        return self.__total

    def check_model(self, car_name: str) -> str:
        if 500000 <= self._car_price <= 10000000 and car_name in self._car_name:
            return "Yes"
        return "No"
    
    def car_avail(self, car_name: str) -> str:
        return "Yes" if car_name in self._car_name else "No"


car = CarShowroom()
# Car Engine Horsepower
hp = car.cal_hp(145, 4600)
car.set_hp(hp)
print(f"Horsepower: {car.get_hp()}")

# Company price of car
car.set_cp(2000000)
print(f"Car Price: {car.get_cp()}")

# Assuming a sale tax value here
total = car.cal_total(50000)  
car.set_total(total)
print(f"Total price including tax: {car.get_total()}")

# Example usage of check_model function
is_valid_model = car.check_model("Toyota")
print(f"Is this car in your budget? {is_valid_model}")

# Example usage of car_avail function
is_car_available = car.car_avail("Toyota")
print(f"Is the 'Toyota' model available? {is_car_available}")
