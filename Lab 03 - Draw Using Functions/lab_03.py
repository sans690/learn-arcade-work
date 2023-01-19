import arcade

screen_width = 1000
screen_height = 800


# Draw face
# Circle
def draw_face(x, y):
    arcade.draw_circle_filled(90 + x, 100 + y, 60, arcade.color.YELLOW)

    # Draw Eyebrow
    arcade.draw_line(50 + x, 120 + y, 70 + x, 110 + y, arcade.color.BLACK, 6)
    arcade.draw_line(110 + x, 110 + y, 130 + x, 120 + y, arcade.color.BLACK, 6)
    # Draw Eyes
    arcade.draw_circle_filled(60 + x, 105 + y, 8, arcade.color.BLACK)
    arcade.draw_circle_filled(120 + x, 105 + y, 8, arcade.color.BLACK)

    # Draw Mouth
    arcade.draw_arc_outline(90 + x, 75 + y, screen_width - 950, screen_height / 40, arcade.color.BLACK, 0, 180, 8)

    # Draw Glasses
    arcade.draw_rectangle_outline(60 + x, 105 + y, screen_width / 30, screen_height / 35, arcade.color.BLACK, 3)
    arcade.draw_rectangle_outline(120 + x, 105 + y, screen_width / 30, screen_height / 35, arcade.color.BLACK, 3)
    arcade.draw_line(75 + x, 105 + y, 105 + x, 105 + y, arcade.color.BLACK, 3)

def main():
    arcade.open_window(screen_width, screen_height, "Drawing Example")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    draw_face(106, 362)
    draw_face(325, 250)
    draw_face(614, 622)
    draw_face(821, 255)

    # To run and finish program
    arcade.finish_render()
    arcade.run()


main()
