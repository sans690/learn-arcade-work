""" Lab 7 - User Control """
import random

# importing the arcade library
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 2


# creates a class called Ball
class Ball:
    """ Initializer """

    # attributes of class Ball, setting them  equal to no value allows them to be set later
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.change_x = 0
        self.change_y = 0
        self.radius = 0
        self.color = None


# make_ball is method in the class Ball
def make_ball():
    # assigning the class to a variable, this creates an instance
    ball = Ball()
    # ball instance, start x position
    ball.position_x = 200
    # ball instance, start y position
    ball.position_y = 300
    # ball instance, radius
    ball.radius = 20
    # ball instance, color
    ball.color = arcade.color.RED
    # creates the ball from function of the arcade class and uses make_ball method values
    # in class ball
    arcade.draw_circle_filled(ball.position_x, ball.position_y, ball.radius, ball.color)
    # returns the ball values back to the make_ball method in the ball class, calling make_ball allows the values to
    # remain represented
    return ball


# method in class Ball that updates the position of the ball instance
def update_ball(self):
    # change the position of the ball based on what is happening to the x
    self.ball.position_x += self.ball.change_x
    # change the position of the ball based on what is happening to the y
    self.ball.position_y += self.ball.change_y


# MyGame is child class to arcade.Window parent class
class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # make mouse not visible in window, set_mouse_visible is a function of arcade, false = invisible
        self.set_mouse_visible(False)

    # make it impossible to move outside of window

    # method in the MyGame that is defined but takes function from parent class(arcade)
    def on_draw(self):
        arcade.start_render()
        # set the background of the window
        arcade.set_background_color(arcade.color.GRAY)
        # calls the make_ball method in the class Ball
        make_ball()

    def update_ball(self, delta_time: float):
        self.ball.update_ball()

    # # method defined in the MyGame
    #  takes input of key being pressed
    def on_key_press(self, key: int, modifier: int):
        # if the left key is pressed
        if key == arcade.key.LEFT:
            # the change in x is effected takes the value of constant movement speed
            # negative movement will move the ball left when it equals the change in x
            self.ball.change_x = -MOVEMENT_SPEED
        # if not left
        elif key == arcade.key.RIGHT:
            # the change in x is effected takes the value of constant movement speed
            # positive movement will move the ball right when it equals the change in x
            self.ball.change_x = MOVEMENT_SPEED
        # if not right or left
        elif key == arcade.key.DOWN:
            # the change in y is effected takes the value of constant movement speed
            # negative movement will move the ball down when it equals the change in y
            self.ball.change_y = -MOVEMENT_SPEED
        # if not up, right, or left
        elif key == arcade.key.UP:
            # the change in y is effected takes the value of constant movement speed
            # positive movement will move the ball up when it equals the change in y
            self.ball.change_y = MOVEMENT_SPEED

    # method defined in the MyGame
    # detects when the user releases the key
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT or arcade.key.RIGHT:
            # the current x position does NOT change
            self.ball.change_x = 0
        elif key == arcade.key.DOWN or arcade.key.UP:
            # the current y position does NOT change
            self.ball.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
