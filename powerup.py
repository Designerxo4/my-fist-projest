import turtle
import random

# Dictionary to associate power-up types with their names and effects
power_up_types = {
    "speed": ("Speed Boost", "Increases your speed temporarily"),
    "invincibility": ("Invincibility", "You are invincible for a short time"),
    "slowdown": ("Slow Down", "Slows down cars temporarily")
}

class PowerUp:
    def __init__(self):
        self.power_up = turtle.Turtle()
        self.power_up.shape("circle")
        self.power_up.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.power_up.penup()
        self.power_up.color(random.choice(["gold", "silver", "green"]))
        self.power_up_type = random.choice(list(power_up_types.keys()))
        self.reset_position()

    def move(self, speed):
        self.power_up.setx(self.power_up.xcor() - speed)
        if self.power_up.xcor() < -400:
            self.reset_position()

    def reset_position(self):
        self.power_up.goto(random.randint(400, 600), random.randint(-250, 250))

    def hide(self):
        self.power_up.hideturtle()

    def show(self):
        self.power_up.showturtle()

    def get_position(self):
        return self.power_up.position()

    def get_name(self):
        return power_up_types[self.power_up_type][0]  # Get the name of the power-up

    def get_description(self):
        return power_up_types[self.power_up_type][1]  # Get the description of the power-up
