# This class will encapsulate the
# attributes related to a car, specifically its year model, make, and current speed. The

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # Initial speed is set to 0

    def accelerate(self):
        self.__speed += 5  # Increase speed by 5

    def brake(self):
        self.__speed -= 5  # Decrease speed by 5
        if self.__speed < 0:  # Ensure speed does not go below 0
            self.__speed = 0

    def get_speed(self):
        return self.__speed  # Return the current speed

# Demonstration of the Car class
if __name__ == "__main__":
    my_car = Car(2023, "Toyota")  # Create a Car object

    # Accelerate the car five times
    for _ in range(5):
        my_car.accelerate()
        print(f"Current speed after accelerating: {my_car.get_speed()} mph")

    # Brake the car five times
    for _ in range(5):
        my_car.brake()
        print(f"Current speed after braking: {my_car.get_speed()} mph")

# Caleb Saari 4/3/25 Wk10 Program 2: Car Class