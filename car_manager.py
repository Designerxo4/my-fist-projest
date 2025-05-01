import random
from car import Car

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = 5  # Starting speed of the cars

    def create_car(self):
        if random.randint(1, 20) == 1:
            new_car = Car()
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move(self.car_speed)

    def increase_speed(self):
        self.car_speed += 2  # Increase speed as the level increases

    def check_collision(self, player):
        for car in self.cars:
            if car.car.distance(player.get_position()) < 20 and not player.is_invincible:
                return True
        return False
