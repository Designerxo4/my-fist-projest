import turtle
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
from powerup import PowerUp

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.tracer(0)

# Create instances of CarManager, Player, Scoreboard, and PowerUp
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
power_up = PowerUp()

# Set up keyboard controls
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

# Main game loop
game_is_on = True
power_up_active = None
power_up_start_time = 0

while game_is_on:
    car_manager.create_car()
    car_manager.move_cars()
    power_up.move(5)

    # Check for collision
    if car_manager.check_collision(player):
        game_is_on = False
        scoreboard.game_over()
        scoreboard.start_again()

    # Check if the player reached the top
    if player.player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_score()
        scoreboard.increase_level()
        car_manager.increase_speed()

    # Check for power-up collection
    if player.player.distance(power_up.get_position()) < 20:
        power_up_name = power_up.get_name()
        power_up_description = power_up.get_description()
        player.apply_power_up(power_up.power_up_type)
        power_up.hide()
        power_up_active = power_up.power_up_type
        power_up_start_time = time.time()

        # Display the power-up info on the screen
        scoreboard.display_powerup_message(f"Collected: {power_up_name} - {power_up_description}")

    # Check if power-up effect should end
    if power_up_active and time.time() - power_up_start_time > 5:  # 5 seconds duration
        player.remove_power_up(power_up_active)
        power_up_active = None
        power_up.reset_position()
        power_up.show()

    # Clear the power-up message after a delay
    if power_up_active and time.time() - power_up_start_time > 1:  # Clear after 1 second
        scoreboard.powerup_message_pen.clear()

    # Update the screen
    screen.update()
    time.sleep(0.05)  # Control the speed of the game loop

# Keep the window open
screen.mainloop()
