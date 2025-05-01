import turtle
import random

# List of possible car colors
colors = ["red", "blue", "green", "yellow", "purple", "black"]

class Car:
    def __init__(self):
        self.car = turtle.Turtle()
        self.car.shape("square")
        self.car.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the shape to look like a car
        self.car.penup()
        self.car.color(random.choice(colors))  # Randomly choose a car color
        self.car.goto(400, random.randint(-250, 250))  # Start the car at the right edge of the screen

    def move(self, speed):
        self.car.setx(self.car.xcor() - speed)  # Move the car to the left at the given speed
        if self.car.xcor() < -400:  # If the car moves off the left side
            self.reset_position()  # Reset the car's position to the right side

    def reset_position(self):
        self.car.goto(400, random.randint(-250, 250))  # Reset the car to the right side with a new y-position
