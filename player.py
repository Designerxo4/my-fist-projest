import turtle

class Player:
    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.player.penup()
        self.player.goto(0, -250)  # Starting position at the bottom of the screen
        self.player.setheading(90)  # Face upwards
        self.is_invincible = False
        self.speed_boost = False

    def move_up(self):
        if self.player.ycor() < 280:
            self.player.sety(self.player.ycor() + (30 if self.speed_boost else 20))

    def move_down(self):
        if self.player.ycor() > -280:
            self.player.sety(self.player.ycor() - (30 if self.speed_boost else 20))

    def move_left(self):
        if self.player.xcor() > -380:
            self.player.setx(self.player.xcor() - (30 if self.speed_boost else 20))

    def move_right(self):
        if self.player.xcor() < 380:
            self.player.setx(self.player.xcor() + (30 if self.speed_boost else 20))

    def get_position(self):
        return self.player.position()

    def reset_position(self):
        self.player.goto(0, -250)

    def apply_power_up(self, power_up_type):
        if power_up_type == "speed":
            self.speed_boost = True
        elif power_up_type == "invincibility":
            self.is_invincible = True

    def remove_power_up(self, power_up_type):
        if power_up_type == "speed":
            self.speed_boost = False
        elif power_up_type == "invincibility":
            self.is_invincible = False
