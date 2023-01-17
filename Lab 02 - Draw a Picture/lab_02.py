# Open the "arcade" library
import arcade

# Open up a window
# From the "arcade" library. use function called "open_window"
# Window title set to "Drawing Example"
# Window dimensions set to (width 800 and height 600)
arcade.open_window(800, 600, "Drawing Example")


# Set background color from library
arcade.set_background_color(arcade.color.BLUE)

# Ready to draw
arcade.start_render()

# Grass
# left of 0, right 799
# top of 300, bottom 0
arcade.draw_lrtb_rectangle_filled(0, 799, 200, 0, arcade.color.GO_GREEN)

# House base
# left 30, right 300
# top of 200, bottom of 150
arcade.draw_lrtb_rectangle_filled(30, 300, 200, 160, arcade.color.FAWN)

# House base second color
# left of 30, right of 300
# top of 300, bottom 170
arcade.draw_lrtb_rectangle_filled(30, 300, 300, 170, arcade.color.BONE)

# House door
# left of 140, right 180
# top of 220, bottom of 150
arcade.draw_lrtb_rectangle_filled(145, 185, 220, 160, arcade.color.BURNT_UMBER)

# House window (left)
# left of 70, right of 100
# top of 230, bottom of 200
arcade.draw_lrtb_rectangle_filled(70, 100, 230, 200, arcade.color.BROWN)

# House window (right)
# left of 220, right of 230
# top of 230, bottom of 200
arcade.draw_lrtb_rectangle_filled(230, 260, 230, 200, arcade.color.BROWN)

# Roof from triangle with 3 points
# (10, 300) (170, 400) (315, 300)
arcade.draw_triangle_filled(10, 300, 170, 400, 315, 300, arcade.color.BROWN)

# Lines on window (left)

# Lines on window (right)






arcade.finish_render()








# Keep window open
arcade.run()
