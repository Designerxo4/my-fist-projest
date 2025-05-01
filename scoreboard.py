import turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(-350, 260)
        self.update_scoreboard()
        self.powerup_message_pen = turtle.Turtle()
        self.powerup_message_pen.hideturtle()
        self.powerup_message_pen.penup()
        self.powerup_message_pen.goto(0, 0)  # Center of the screen

    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}  Level: {self.level}", align="left", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.pen.goto(0, 0)
        self.pen.write("GAME OVER", align="center", font=("Arial", 36, "bold"))

    def display_powerup_message(self, message):
        self.powerup_message_pen.clear()  # Clear previous messages
        self.powerup_message_pen.write(message, align="center", font=("Arial", 24, "normal"))

    def start_again(self):
        self.pen.goto(0, 40)
        self.pen.write("Play Again?", align="center", font=("Arial", 24, "bold"))